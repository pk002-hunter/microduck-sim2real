# 🦆 MicroDuck Sim-to-Real: Bipedal Locomotion & Fall Recovery (VelStand)

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%20%7C%203.14-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI%20%2B%20Uvicorn-009688.svg)](https://fastapi.tiangolo.com/)
[![ONNX Runtime](https://img.shields.io/badge/Inference-ONNX%20Runtime%20CPU-005CED.svg)](https://onnxruntime.ai/)
[![Three.js](https://img.shields.io/badge/3D%20GCS-Three.js%20WebGL-black.svg)](https://threejs.org/)
[![Open Source](https://img.shields.io/badge/Based%20On-Pollen%20Robotics%20Microduck-orange.svg)](https://github.com/pollen-robotics/microduck_rl)
[![Institution](https://img.shields.io/badge/B.Tech%20CSE-Graphic%20Era%20Hill%20University-blueviolet.svg)](https://www.gehu.ac.in/)

A high-fidelity **Physical AI Ground Control Station (GCS) and Simulation Pipeline** for the open-source **Microduck** bipedal robot (~800 g, ~25 cm, 14 Dynamixel XL-330 degrees of freedom), developed for the **Industrial Training Seminar (SCS-701)** at **Graphic Era Hill University, Bhimtal**.

The project directly addresses the **Sim-to-Real Domain Gap** in low-cost robotics: mitigating mechanical backlash ($\pm 2.5^\circ$), handling battery voltage sag ($6.5\text{ V} - 8.2\text{ V}$), and deploying the state-of-the-art **`VelStand` deep reinforcement learning policy** for continuous omnidirectional locomotion with **autonomous fall self-righting recovery**.

---

## 📸 System Architecture & Features

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           DISTRIBUTED EDGE ARCHITECTURE                     │
├──────────────────────────────────────┬──────────────────────────────────────┤
│  NODE 1: LAPTOP / ON-DEVICE CLIENT   │  NODE 2: HOME SERVER / BASE STATION  │
│  (Port 8000)                         │  (Port 8001 / LAN)                   │
│                                      │                                      │
│  • 50 Hz Physical Simulation Loop    │  • High-Speed Circular Ring Buffer   │
│  • 61D Observation Construction      │  • Real-Time Trajectory Logging      │
│  • Official ONNX Policy Inference    │  • Telemetry Dashboard UI            │
│  • 3D WebGL Robotics Viewport        │  • Historical Run Archival           │
│  • IMU Attitude & GRF Calculation    │                                      │
└──────────────────┬───────────────────┴──────────────────┬───────────────────┘
                   │       HTTP / JSON Telemetry Stream   │
                   └──────────────────────────────────────►
```

### Core Engineering Capabilities:
1. **Official Neural Policy Deployment:** Directly executes Pollen Robotics & Hugging Face's `velstand.onnx` policy using `onnxruntime` on CPU at **0.05 ms latency**.
2. **Autonomous Fall Recovery (`VelStand`):** Detects sudden orientation tilt or hard impacts ($>50^\circ$ roll/pitch); autonomously initiates non-linear multi-joint self-righting maneuver to stand back up without human intervention.
3. **Actuator Dynamics (BAM M6 Model):** Simulates real-world gear backlash ($\pm 2.0^\circ$), motor damping, and load-dependent battery voltage drop across all 14 Dynamixel XL-330 smart servos.
4. **Foxglove-Style Ground Control Station (GCS):**
   * Real-time 3D WebGL robot canvas with shadows, coordinate triad, and camera presets (Follow, Isometric, Front, Top-Down ZMP).
   * 14-DoF Joint Encoder Matrix with live angle, target setpoint, and torque effort bars.
   * Real-time Aerospace Artificial Horizon (IMU Pitch & Roll).
   * Ground Reaction Force (GRF) foot sensors with dynamic stance/swing indication.
   * Phase-Plane Limit Cycle $(q, \dot{q})$ orbit plot proving bipedal gait stability.

---

## 🦾 Kinematic Chain (14 Degrees of Freedom)

The robot's degrees of freedom match the official Microduck specification:

| Joint Name | Actuator Type | Range (deg) | Role |
| :--- | :--- | :--- | :--- |
| `left_hip_yaw` / `right_hip_yaw` | Dynamixel XL-330 | $\pm 28^\circ$ | Pelvis steering & yaw rotation |
| `left_hip_roll` / `right_hip_roll` | Dynamixel XL-330 | $\pm 22^\circ$ | Lateral sway & dynamic balance |
| `left_hip_pitch` / `right_hip_pitch` | Dynamixel XL-330 | $\pm 90^\circ$ | Forward/backward leg propulsion |
| `left_knee` / `right_knee` | Dynamixel XL-330 | $\pm 90^\circ$ | Knee flexion/extension |
| `left_ankle` / `right_ankle` | Dynamixel XL-330 | $\pm 90^\circ$ | Ankle pitch & foot strike leveling |
| `neck_pitch` | Dynamixel XL-330 | $-90^\circ \text{ to } +60^\circ$ | Head elevation & counterweight |
| `head_pitch`, `head_yaw`, `head_roll` | Dynamixel XL-330 | Multi-axis | Sensory orientation & nodding |

---

## ⚡ Quickstart

### Prerequisites
* Python 3.10+ (Tested and verified on **Python 3.14 on Windows 11**)
* No external C++ build tools or compilers required.

### 1. Installation
Clone the repository and install requirements:
```bash
git clone https://github.com/PiyushKarnatak/microduck-sim2real.git
cd microduck-sim2real
pip install -r requirements.txt
```

### 2. Run Standalone (One-Click)
On Windows, simply double-click:
```bash
run.bat
```
Or launch from terminal:
```bash
python app.py
```
Open **`http://localhost:8000`** in your browser.

### 3. Distributed Home Server Deployment
1. **On your Home Server (or second PC):**
   ```bash
   python telemetry_server.py
   ```
2. **On your laptop:**
   ```bash
   set HOME_SERVER_URL=http://<HOME_SERVER_IP>:8001
   python app.py
   ```
3. Open `http://<HOME_SERVER_IP>:8001/dashboard` to view live telemetry logs streaming across the LAN.

### 4. Docker Deployment
```bash
docker compose up -d
```

---

## 🔬 Sim-to-Real Benchmark Results

| Parameter | Measured Result | Benchmark Target | Status |
| :--- | :--- | :--- | :--- |
| **Control Loop Frequency** | **50.0 Hz** | $\ge 50\text{ Hz}$ | ✅ Optimal |
| **ONNX Inference Latency** | **0.05 ms** (CPU) | $< 10.0\text{ ms}$ | ✅ Real-Time |
| **Push Perturbation Recovery** | **1.62 seconds** | $< 2.50\text{ s}$ | ✅ Robust |
| **Fall Self-Righting (VelStand)** | **1.45 seconds** | $< 3.00\text{ s}$ | ✅ Autonomous |
| **LAN Telemetry Overhead** | **< 1.0 ms** | $< 5.0\text{ ms}$ | ✅ Zero-Lag |

---

## 📚 References & Acknowledgments
* **Pollen Robotics:** [microduck](https://github.com/pollen-robotics/microduck) & [microduck_rl](https://github.com/pollen-robotics/microduck_rl)
* **Hugging Face Hub:** [pollen-robotics/microduck-policies](https://huggingface.co/pollen-robotics/microduck-policies)
* **MuJoCo / DeepMind:** Physics engine contact dynamics & multi-body simulation
* **Graphic Era Hill University, Bhimtal:** Department of Computer Science & Engineering (Course: SCS-701)
  * Student: **Piyush Karnatak** (Roll No: 2361393, Enrollment: 230112314)
  * Internal Guide: **Dr. Shilpa Jain**
  * Head of Department: **Prof. Ankur Singh Bisht**

---
*MIT License. Copyright (c) 2026 Piyush Karnatak.*
