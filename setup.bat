@echo off
REM Django Ecommerce Setup Script for Windows
REM This script will set up the entire project

echo.
echo ====================================
echo Django Ecommerce Setup for Windows
echo ====================================
echo.

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

echo [1/5] Python found: 
python --version

REM Create virtual environment
echo.
echo [2/5] Creating virtual environment...
if exist env (
    echo Virtual environment already exists
) else (
    python -m venv env
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo Virtual environment created successfully
)

REM Activate virtual environment
echo.
echo [3/5] Activating virtual environment...
call env\Scripts\activate.bat

REM Upgrade pip and install requirements
echo.
echo [4/5] Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

REM Create .env file
echo.
echo [5/5] Setting up environment configuration...
if not exist .env (
    copy .env.example .env
    echo .env file created. Please edit it with your MySQL credentials:
    echo   - MYSQL_DATABASE=ecommerce_db
    echo   - MYSQL_USER=your_username
    echo   - MYSQL_PASSWORD=your_password
    echo   - MYSQL_HOST=127.0.0.1
) else (
    echo .env file already exists
)

REM Summary
echo.
echo ====================================
echo Setup Complete!
echo ====================================
echo.
echo Next steps:
echo 1. Edit .env file with your MySQL credentials
echo 2. Create MySQL database (see MYSQL_SETUP.md)
echo 3. Run: python manage.py migrate
echo 4. Run: python manage.py createsuperuser
echo 5. Run: python manage.py runserver
echo.
echo To activate virtual environment in the future, run:
echo   env\Scripts\activate.bat
echo.
pause
