from flask import Flask, request , jsonify, send_file
from flask_cors import CORS  
import subprocess
import sys
import os
import torch
import torchvision.transforms as transforms
from PIL import Image
import torchvision.models as models
import torch.nn as nn
import torch.nn.functional as F
import io
import datetime
import jwt
from functools import wraps
import bcrypt
from database import init_db, get_user

app = Flask(__name__)
CORS(app)  # ✅ อนุญาตให้ React เรียก API ได้

datestart = ""
datestop = ""
periodday = ""
mode = ""

app.config['SECRET_KEY'] = 'your_secret_key'  # ใช้สำหรับเข้ารหัส JWT

# เรียกใช้งาน database
init_db()


# Middleware ตรวจสอบ token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = get_user(data['username'])
            if not current_user:
                return jsonify({'error': 'User not found!'}), 403
        except:
            return jsonify({'error': 'Token is invalid!'}), 403
        return f(current_user, *args, **kwargs)
    return decorated

# API Login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = get_user(username)
    if not user or user['password'] != password:
        return jsonify({'error': 'Invalid credentials'}), 401
    
    token = jwt.encode({'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, 
                       app.config['SECRET_KEY'], algorithm="HS256")
    return jsonify({'token': token.decode('utf-8'), 'role': user['role']})

# API Protected Route
@app.route('/protected', methods=['GET'])
@token_required
def protected_route(current_user):
    return jsonify({'message': 'This is a protected route', 'user': current_user})


# ---------------------------- RPA Part
@app.route('/run_rpa', methods=['POST'])
def run_rpa():
    try:
        data = request.json
        row = str(data.get("row", "")).strip()
        column = str(data.get("column", "")).strip()
        month1 = str(data.get("month1", "")).strip()
        year1 = str(data.get("year1", "")).strip()
        periodday = str(data.get("periodday", "")).strip()
        mode = str(data.get("mode", "")).strip()

        if mode == "st":
            if not all([row, column, month1, year1, periodday]):
                return jsonify({"error": "❌ Missing parameters"}), 400

            print(f"📌 Running RPA with params: {row}, {column}, {month1}, {year1}, {periodday}")

            if os.name == "nt":  # Windows
                subprocess.Popen(
                    [sys.executable, "rpa_pullperiodst.py", row, column, month1, year1, periodday],
                    creationflags=subprocess.CREATE_NEW_CONSOLE  # ✅ เปิดหน้าต่างใหม่
            )

            return jsonify({"message": "✅ RPA started successfully"}), 200
        
        elif mode == "ld":
            if not all([row, column, month1, year1, periodday]):
                return jsonify({"error": "❌ Missing parameters"}), 400

            print(f"📌 Running RPA with params: {row}, {column}, {month1}, {year1}, {periodday}")

            if os.name == "nt":  # Windows
                subprocess.Popen(
                    [sys.executable, "rpa_pullperiodld.py", row, column, month1, year1, periodday],
                    creationflags=subprocess.CREATE_NEW_CONSOLE  # ✅ เปิดหน้าต่างใหม่
            )

            return jsonify({"message": "✅ RPA started successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.layer = nn.Linear(512, 10)  # ตัวอย่างโมเดล

    def forward(self, x):
        return self.layer(x)

# โหลดโมเดลที่เทรนแล้ว
model = models.resnet50()  
num_ftrs = model.fc.in_features  # จำนวน input features ของ Fully Connected layer
model.fc = nn.Linear(num_ftrs, 3)  # แก้ไขให้ตรงกับจำนวน output ของโมเดลที่เทรน

# โหลด state_dict จาก checkpoint
checkpoint = torch.load("resnet50_checkpoint_0.pth", map_location=torch.device('cpu'))
model.load_state_dict(checkpoint["model_state_dict"])  # ใช้เฉพาะ model_state_dict

model.eval()  # ตั้งค่าเป็นโหมดทดสอบ

transform = transforms.Compose([
    transforms.Resize((224, 224)),  # ปรับขนาดให้ตรงกับที่โมเดลใช้
    transforms.ToTensor(),
])

@app.route('/predict', methods=['POST'])
def getdateshow():
    global datestart
    global datestop
    global periodday
    global mode

    data = request.json
    datestart = str(data.get("datestart", "")).strip()
    datestop = str(data.get("datestop", "")).strip()
    periodday = str(data.get("periodday", "")).strip()
    mode = str(data.get("mode", "")).strip()

    # แปลงวันที่
    try:
        start_date = datetime.datetime.strptime(datestart, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(datestop, "%Y-%m-%d").date()
    except ValueError:
        return jsonify({"error": "Invalid date format"}), 400

    # โหลดรายการรูปภาพตามวันที่
    image_dir = "C:/Users/Ratti/Documents/IceCreamDetection/StandingContract/IMAGE_file"  # เปลี่ยนเป็น path ที่เก็บรูปภาพ
    image_paths = load_images_by_date(image_dir, start_date, end_date)

    return jsonify({
        "message": "บันทึก",
        "datestart": datestart,
        "datestop": datestop,
        "periodday": periodday,
        "mode": mode,
        "images": image_paths
    })

def load_images_by_date(root_dir, start_date, end_date):
    image_paths = []
    for folder in sorted(os.listdir(root_dir)):
        folder_path = os.path.join(root_dir, folder)
        try:
            folder_date = datetime.datetime.strptime(folder, "%Y-%m-%d").date()
        except ValueError:
            continue

        if start_date <= folder_date <= end_date:
            for file in os.listdir(folder_path):
                if file.lower().endswith((".png", ".jpg", ".jpeg")):
                    image_paths.append(os.path.join(folder, file))

    return image_paths

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    img = Image.open(file).convert('RGB')
    img = transform(img)
    img = img.unsqueeze(0)  # เพิ่มมิติสำหรับ batch

    # ทำนายผล
    with torch.no_grad():
        output = model(img)
        prediction = output.argmax(dim=1).item()  # ค่าผลลัพธ์ที่มีค่าสูงสุด

    return jsonify({"prediction": prediction})

@app.route('/classify', methods=['POST'])
def classify_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    img = Image.open(file).convert('RGB')
    img = transform(img).unsqueeze(0)  # เพิ่มมิติ batch

    with torch.no_grad():
        output = model(img)
        prediction = output.argmax(dim=1).item()

    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # ✅ ต้องมีเพื่อรัน Flask
