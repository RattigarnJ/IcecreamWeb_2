@echo off
setlocal

REM Activate Python virtual environment
call venv\Scripts\activate

REM Start backend (Flask/FastAPI/etc.) in a new terminal
cd backend
start cmd /k "python app.py"

cd ..
REM Start frontend (ReactJS) in a new terminal
cd frontend
start cmd /k "npm start"

endlocal
