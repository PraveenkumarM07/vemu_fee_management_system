@echo off
echo Fee Management System
echo ====================
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

REM Check if main.py exists
if not exist "main.py" (
    echo Error: main.py not found in current directory
    echo Current directory: %CD%
    pause
    exit /b 1
)

echo Starting Fee Management System...
echo.

REM Run the application
python main.py

echo.
echo Application stopped.
pause
