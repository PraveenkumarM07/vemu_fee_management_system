@echo off
echo Installing Fee Management System Dependencies
echo ============================================
echo.

REM Change to the directory where this batch file is located
cd /d "%~dp0"

echo Current directory: %CD%
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python and try again
    pause
    exit /b 1
)

echo Installing required packages...
echo.

REM Install packages one by one to see progress
echo Installing Flask...
pip install Flask==2.3.3

echo Installing Flask-SQLAlchemy...
pip install Flask-SQLAlchemy==3.0.5

echo Installing Flask-Migrate...
pip install Flask-Migrate==4.0.5

echo Installing Flask-CORS...
pip install Flask-CORS==4.0.0

echo Installing Werkzeug...
pip install Werkzeug==2.3.7

echo Installing requests...
pip install requests==2.31.0

echo Installing python-dotenv...
pip install python-dotenv==1.0.0

echo Installing gunicorn...
pip install gunicorn==23.0.0

echo Installing psycopg2-binary (PostgreSQL driver)...
pip install psycopg2-binary==2.9.7

echo Installing PyMySQL...
pip install PyMySQL==1.1.0

echo Installing cryptography...
pip install cryptography==41.0.4

echo.
echo ============================================
echo Installation completed!
echo.
echo You can now run the application using:
echo 1. Double-click run_app.bat, or
echo 2. Run: python main.py
echo.
pause
