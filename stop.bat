@echo off
title Stop MicroDuck Simulation
echo ========================================================
echo   Shutting Down MicroDuck Simulation and Telemetry Sink
echo ========================================================
echo.

echo [1/3] Terminating processes on Port 8000 (FastAPI Locomotion Engine)...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":8000" ^| findstr "LISTENING"') do (
    echo       Killing PID %%a on Port 8000...
    taskkill /F /PID %%a >nul 2>&1
)

echo [2/3] Terminating processes on Port 8001 (Telemetry Base Station)...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":8001" ^| findstr "LISTENING"') do (
    echo       Killing PID %%a on Port 8001...
    taskkill /F /PID %%a >nul 2>&1
)

echo [3/3] Closing Server Terminal Windows...
taskkill /F /FI "WINDOWTITLE eq MicroDuck Sim Server*" >nul 2>&1
taskkill /F /FI "WINDOWTITLE eq Telemetry Server*" >nul 2>&1

echo.
echo ========================================================
echo   [OK] MicroDuck Simulation and Telemetry cleanly stopped.
echo   Ports 8000 and 8001 are now free.
echo ========================================================
echo.
exit /b 0
