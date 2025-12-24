#!/bin/bash

# Django Ecommerce Setup Script for Mac/Linux
# This script will set up the entire project

echo ""
echo "===================================="
echo "Django Ecommerce Setup for Mac/Linux"
echo "===================================="
echo ""

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org"
    exit 1
fi

echo "[1/5] Python found:"
python3 --version

# Create virtual environment
echo ""
echo "[2/5] Creating virtual environment..."
if [ -d "env" ]; then
    echo "Virtual environment already exists"
else
    python3 -m venv env
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to create virtual environment"
        exit 1
    fi
    echo "Virtual environment created successfully"
fi

# Activate virtual environment
echo ""
echo "[3/5] Activating virtual environment..."
source env/bin/activate

# Upgrade pip and install requirements
echo ""
echo "[4/5] Installing dependencies..."
python -m pip install --upgrade pip
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

# Create .env file
echo ""
echo "[5/5] Setting up environment configuration..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo ".env file created. Please edit it with your MySQL credentials:"
    echo "  - MYSQL_DATABASE=ecommerce_db"
    echo "  - MYSQL_USER=your_username"
    echo "  - MYSQL_PASSWORD=your_password"
    echo "  - MYSQL_HOST=127.0.0.1"
else
    echo ".env file already exists"
fi

# Summary
echo ""
echo "===================================="
echo "Setup Complete!"
echo "===================================="
echo ""
echo "Next steps:"
echo "1. Edit .env file with your MySQL credentials"
echo "2. Create MySQL database (see MYSQL_SETUP.md)"
echo "3. Run: python manage.py migrate"
echo "4. Run: python manage.py createsuperuser"
echo "5. Run: python manage.py runserver"
echo ""
echo "To activate virtual environment in the future, run:"
echo "  source env/bin/activate"
echo ""
