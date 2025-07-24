@echo off
echo ===============================================
echo    THE TIME GUARDIAN - AUTOMATIC INSTALLER
echo ===============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH!
    echo.
    echo Please install Python from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo [1/5] Python found!
echo.

REM Create project structure
echo [2/5] Setting up project structure...
python setup_project.py
if %errorlevel% neq 0 (
    echo ERROR: Failed to set up project structure
    pause
    exit /b 1
)
echo.

REM Install dependencies
echo [3/5] Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo.

REM Create assets
echo [4/5] Creating game assets...
python create_assets.py
if %errorlevel% neq 0 (
    echo WARNING: Could not create assets, but game may still run
)
echo.

REM Test installation
echo [5/5] Testing installation...
python test_installation.py
echo.

echo ===============================================
echo           INSTALLATION COMPLETE!
echo ===============================================
echo.
echo Press any key to start the game...
pause >nul

REM Start the game
cls
python main.py