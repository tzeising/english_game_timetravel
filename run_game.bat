@echo off
echo Starting The Time Guardian: Lila's Quest...
echo.
python main.py
if %errorlevel% neq 0 (
    echo.
    echo Error: Failed to start game!
    echo Make sure Python is installed and dependencies are met.
    echo Run: pip install -r requirements.txt
    echo.
    pause
)