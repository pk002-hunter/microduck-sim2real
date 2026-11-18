"""
MicroDuck Edge Telemetry Logger & Base Station (Port 8001)
Simulates the Home Server / Central Fleet Logger receiving 50 Hz telemetry over LAN.
"""

import time
import collections
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="MicroDuck Telemetry Server", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory circular buffer (last 1000 telemetry packets)
_logs = collections.deque(maxlen=1000)

@app.post("/log")
async def receive_telemetry(request: Request):
    try:
        packet = await request.json()
        packet["rx_timestamp"] = round(time.time(), 3)
        _logs.append(packet)
        return {"status": "ok", "buffer_count": len(_logs)}
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})

@app.get("/api/logs")
def get_logs():
    return JSONResponse(content=list(_logs))

@app.get("/dashboard", response_class=HTMLResponse)
def serve_dashboard():
    total_pkts = len(_logs)
    last_12 = list(_logs)[-12:][::-1]

    rows_html = ""
    for p in last_12:
        t = p.get("t", 0.0)
        mode = p.get("state_mode", "WALK")
        att = p.get("attitude", {})
        pitch = att.get("pitch", 0.0)
        roll = att.get("roll", 0.0)
        pwr = p.get("power", {})
        v = pwr.get("voltage_v", 7.9)
        i = pwr.get("current_a", 0.8)
        sys_info = p.get("system", {})
        lat = sys_info.get("onnx_latency_ms", 0.05)
        
        mode_color = "#00ff88" if mode == "WALK" else ("#ff3366" if mode == "FALLEN" else "#ffb300")

        rows_html += f"""
        <tr>
          <td>{t:.2f} s</td>
          <td style="color:{mode_color}; font-weight:bold;">{mode}</td>
          <td>P: {pitch:.1f}° | R: {roll:.1f}°</td>
          <td>{v:.2f} V</td>
          <td>{i:.2f} A</td>
          <td style="color:#00e5ff;">{lat:.2f} ms</td>
        </tr>
        """

    html = f"""<!DOCTYPE html>
<html>
<head>
  <title>MicroDuck Edge Base Station | Telemetry Stream</title>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="1">
  <style>
    body {{ background: #07090e; color: #f0f6fc; font-family: 'Consolas', monospace; padding: 24px; }}
    h1 {{ color: #00e5ff; font-size: 1.25rem; display: flex; align-items: center; gap: 8px; }}
    .badge {{ background: #121824; border: 1px solid #1b2332; border-radius: 4px; padding: 6px 14px; display: inline-block; font-size: 0.8rem; margin: 12px 0; color: #00ff88; }}
    table {{ width: 100%; border-collapse: collapse; margin-top: 14px; font-size: 0.8rem; }}
    th {{ background: #0d1118; color: #8b949e; text-align: left; padding: 10px 14px; border-bottom: 2px solid #00e5ff; }}
    td {{ padding: 8px 14px; border-bottom: 1px solid #161e2e; }}
    tr:hover td {{ background: #111722; }}
    .footer {{ margin-top: 20px; font-size: 0.72rem; color: #8b949e; }}
  </style>
</head>
<body>
  <h1>🦆 MICRODUCK EDGE BASE STATION (HOME SERVER)</h1>
  <div class="badge">PACKETS LOGGED: {total_pkts} | RATE: 50 Hz STREAMING OVER LAN | NODE STATUS: HEALTHY</div>
  <table>
    <thead>
      <tr>
        <th>Sim Time</th><th>State Mode</th><th>IMU Attitude</th>
        <th>Bus Voltage</th><th>Motor Current</th><th>ONNX Latency</th>
      </tr>
    </thead>
    <tbody>
      {rows_html if rows_html else '<tr><td colspan="6" style="text-align:center;color:#8b949e;">Awaiting telemetry stream from laptop node...</td></tr>'}
    </tbody>
  </table>
  <div class="footer">Telemetry sink endpoint: POST /log | Auto-refreshing at 1 Hz</div>
</body>
</html>"""
    return HTMLResponse(content=html)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("telemetry_server:app", host="0.0.0.0", port=8001, reload=False, log_level="info")
