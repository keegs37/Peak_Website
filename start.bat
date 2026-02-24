@echo off
echo Starting PEAK Internet local server...

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH.
    echo Please install Python to run the local server.
    pause
    exit /b 1
)

:: Start the server in the background
start "PEAK Internet Server" /MIN cmd /c "title PEAK_SERVER & python -m http.server 8000"

echo Server started at http://localhost:8000
echo Use stop.bat to stop the server.
pause
