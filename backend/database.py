import sqlite3

DATABASE = "users.db"

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # สร้างตาราง users ถ้ายังไม่มี
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')
    
    # เพิ่มข้อมูลตัวอย่างถ้ายังไม่มี
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", [
            ("Dev", "010", "Dev"),
            ("Admin", "0", "Admin"),
            ("U1", "1", "User")
        ])
        conn.commit()
    
    conn.close()

def get_user(username):
    """ ดึงข้อมูลผู้ใช้จากฐานข้อมูล """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT username, password, role FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    if user:
        return {"username": user[0], "password": user[1], "role": user[2]}
    return None
