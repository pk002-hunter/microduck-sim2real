@echo off
cd /d "%~dp0"
echo Starting MicroDuck Simulation...
start "MicroDuck Sim Server" python app.py
timeout /t 2 /nobreak
start "Telemetry Server" python telemetry_server.py
timeout /t 1 /nobreak
start http://localhost:8000
echo Both servers started. Browser opening...
