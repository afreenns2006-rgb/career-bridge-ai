#!/bin/bash
# Career Bridge AI - Quick Start Script for Linux/macOS
# This script sets up and runs Career Bridge AI

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║         Career Bridge AI - Quick Start                         ║"
echo "║       An AI-Powered Student Career Guidance Platform          ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3.9+ from https://www.python.org"
    exit 1
fi

echo "✅ Python is installed"
python3 --version
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "❌ Error: Failed to create virtual environment"
        exit 1
    fi
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

echo ""
echo "🔧 Activating virtual environment..."
source venv/bin/activate

echo ""
echo "📚 Installing dependencies..."
python3 -m pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Error: Failed to install dependencies"
    echo "Try running: pip install -r requirements.txt"
    exit 1
fi

echo "✅ Dependencies installed successfully"
echo ""

echo "═════════════════════════════════════════════════════════════════"
echo "🚀 Starting Career Bridge AI..."
echo "═════════════════════════════════════════════════════════════════"
echo ""
echo "📱 The application will open at: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the application"
echo ""

# Run Streamlit app
streamlit run app.py
