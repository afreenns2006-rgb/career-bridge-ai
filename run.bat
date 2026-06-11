@echo off
REM Career Bridge AI - Quick Start Script for Windows
REM This script sets up and runs Career Bridge AI

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║         Career Bridge AI - Quick Start                         ║
echo ║       An AI-Powered Student Career Guidance Platform          ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Error: Python is not installed or not in PATH
    echo Please install Python 3.9+ from https://www.python.org
    pause
    exit /b 1
)

echo ✅ Python is installed
python --version
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo ❌ Error: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo ✅ Virtual environment created
) else (
    echo ✅ Virtual environment already exists
)

echo.
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo 📚 Installing dependencies...
python -m pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo ❌ Error: Failed to install dependencies
    echo Try running: pip install -r requirements.txt
    pause
    exit /b 1
)

echo ✅ Dependencies installed successfully
echo.

echo ═════════════════════════════════════════════════════════════════
echo 🚀 Starting Career Bridge AI...
echo ═════════════════════════════════════════════════════════════════
echo.
echo 📱 The application will open at: http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.

REM Run Streamlit app
streamlit run app.py

pause
