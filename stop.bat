@echo off
echo Stopping PEAK Internet local server...

:: Find and kill the process with window title PEAK_SERVER
taskkill /FI "WINDOWTITLE eq Administrator:  PEAK_SERVER*" /F >nul 2>&1
taskkill /FI "WINDOWTITLE eq PEAK_SERVER*" /F >nul 2>&1

:: Also try to kill any python process running http.server on port 8000
for /f "tokens=5" %%a in ('netstat -aon ^| find "0.0.0.0:8000" ^| find "LISTENING"') do (
    taskkill /F /PID %%a >nul 2>&1
)

echo Server stopped.
pause
