@echo off
REM BIMS Chatbot Quick Start Script for Windows

echo.
echo ========================================
echo   BIMS FAQ Chatbot - Quick Start
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo [1/4] Python found: 
python --version

REM Check if virtual environment exists
if not exist "venv" (
    echo.
    echo [2/4] Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
)

echo [2/4] Virtual environment ready

REM Activate virtual environment
echo [3/4] Activating virtual environment...
call venv\Scripts\activate.bat

REM Install requirements
echo [4/4] Installing dependencies...
pip install -q -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install requirements
    echo Try running: pip install -r requirements.txt
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Starting BIMS Chatbot...
echo ========================================
echo.
echo Server will run on: http://localhost:5000
echo.
echo Open your browser and go to that address
echo.
echo Press Ctrl+C to stop the server
echo.

python chatbot.py
pause
