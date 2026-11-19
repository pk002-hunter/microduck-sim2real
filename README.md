# 🦆 MicroDuck Sim-to-Real: Bipedal Locomotion & Fall Recovery (VelStand)

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%20%7C%203.14-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI%20%2B%20Uvicorn-009688.svg)](https://fastapi.tiangolo.com/)
[![ONNX Runtime](https://img.shields.io/badge/Inference-ONNX%20Runtime%20CPU-005CED.svg)](https://onnxruntime.ai/)
[![Three.js](https://img.shields.io/badge/3D%20GCS-Three.js%20WebGL-black.svg)](https://threejs.org/)
[![Open Source](https://img.shields.io/badge/Based%20On-Pollen%20Robotics%20Microduck-orange.svg)](https://github.com/pollen-robotics/microduck_rl)
[![Institution](https://img.shields.io/badge/B.Tech%20CSE-Graphic%20Era%20Hill%20University-blueviolet.svg)](https://www.gehu.ac.in/)

A high-fidelity **Physical AI Ground Control Station (GCS) and Simulation Pipeline** for the open-source **Microduck** bipedal robot (~800 g, ~25 cm, 14 Dynamixel XL-330 degrees of freedom), developed for the **Industrial Training Seminar (SCS-701)** at **Graphic Era Hill University, Bhimtal**.

The project directly solves the **Sim-to-Real Domain Gap** in low-cost bipedal robots: mitigating mechanical gear backlash ($\pm 2.0^\circ$), handling battery voltage sag ($6.5\text{ V} - 8.2\text{ V}$), and deploying the state-of-the-art **`VelStand` deep reinforcement learning policy** for omnidirectional locomotion with **autonomous fall self-righting recovery**.

---

## 📸 Ground Control Station & Simulation Interface

![Microduck 3D Teleoperation & Ground Control Station](docs/images/01_sim_teleop_dashboard.png)
*Figure 1: Ground Control Station (GCS) featuring high-fidelity Microduck CAD model, omnidirectional D-pad teleoperation dock, 14-DoF joint encoder glass dock, 4-phase gait indicators, and live motor audio synthesizer.*

---

## 🚀 Key Engineering Highlights

### 1. Dynamic Walking & Autonomous Fall Recovery (`VelStand`)
The robot achieves stable dynamic walking via 50 Hz closed-loop control and recovers autonomously from severe falls without human intervention.

| 50Hz Dynamic Stride Gait | 5-Phase Autonomous Fall Recovery (Stage 3 Knee Lever) |
| :---: | :---: |
| ![Microduck Dynamic Walking Gait](docs/images/02_motory_walking_gait.png) | ![Microduck Fall Recovery](docs/images/03_velstand_fall_recovery.png) |
| *Figure 2: 50Hz dynamic bipedal walking gait with real-time joint HUD callouts and limit-cycle phase portrait.* | *Figure 3: VelStand Stage 3 knee-lever push exerting 18.4 N normal reaction force to lift Center of Mass.* |

---

### 2. Neural Policy & Synaptic Firing Inspector
Directly compare the **Naive Baseline RL policy** against our **BAM Backlash-Compensated Policy** under live sensory perturbations.

| Trained Policy (BAM Compensated) | Baseline RL (Uncompensated Chatter) |
| :---: | :---: |
| ![Trained Policy with Smooth Torque](docs/images/04_neural_actor_policy.png) | ![Baseline RL with 28Hz Noise Chatter](docs/images/05_neural_baseline_chatter.png) |
| *Figure 4: BAM-compensated policy exhibiting coherent harmonic synaptic waves and smooth knee torque ($<0.32\text{ N}\cdot\text{m}$).* | *Figure 5: Naive RL exhibiting severe 28 Hz control chatter and high gear deadband flutter ($18.6^\circ$).* |

#### Dual Actor-Critic Architecture & 61D Input Tensor Inspector
| Critic Value Function $V(s)$ Evaluation | 61D Observation Input Tensor Inspector |
| :---: | :---: |
| ![Critic Value Function](docs/images/06_neural_critic_value.png) | ![61D Input Inspector Tooltip](docs/images/07_61d_tensor_inspector.png) |
| *Figure 6: Critic network $[61 \rightarrow 256 \rightarrow 128 \rightarrow 64 \rightarrow 1]$ evaluating expected discounted state return ($V = +48.6$).* | *Figure 7: Interactive hover inspector detailing 61D observation vector (Input Group #8: BAM Backlash State $\Delta_{\text{bam}}$).* |

---

### 3. Contact Physics & Technical Kinematic Schematic
![VelStand Contact Physics Schematic](docs/images/08_contact_physics_schematic.png)
*Figure 8: Microduck 2D technical orthographic drawing illustrating multi-contact ground reaction forces ($18.4\text{ N}$ knee contact vs. $24.8\text{ N}$ sole plant) across the 5 VelStand stages.*

---

### 4. Sim-to-Real Problem Statement & Academic Solution
![Sim-to-Real Problem & Solution](docs/images/09_sim2real_problem_solution.png)
*Figure 9: Comprehensive breakdown of the Backlash Actuator Model (BAM M6), motor impedance equations, and GEHU SCS-701 seminar specifications.*

---

## 🏗️ Distributed System Architecture

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
git clone https://github.com/pk002-hunter/microduck-sim2real.git
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

### 3. Graceful Shutdown (One-Click)
To safely stop the simulation server, backend processes, and clean up ports:
```bash
stop.bat
```

### 4. Distributed Home Server Deployment
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

### 5. Docker Deployment
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

## 🎓 Industrial Training & Certification (SCS-701)
* **Training Program:** [Hugging Face Deep Reinforcement Learning Course](https://huggingface.co/learn/deep-rl-course/unit0/introduction) (Completed by Piyush Karnatak, Instructor: Thomas Simonini)
* **Official Certificate:** [Certificate of Completion](docs/presentation/certificate.png)
* **Seminar Presentation:** [`docs/presentation/Piyush_Industrial_Training_Final.pptx`](docs/presentation/Piyush_Industrial_Training_Final.pptx) — 15-slide comprehensive evaluation presentation built on Canva Modern Burgundy/Gold design principles.
* **Formal Word Report:** [`docs/presentation/Piyush_Industrial_Training_Report_SCS701.docx`](docs/presentation/Piyush_Industrial_Training_Report_SCS701.docx) — Formal 7th Semester training report compliant with Graphic Era Hill University guidelines.

---

## 📚 References & Academic Details
* **Pollen Robotics:** [microduck](https://github.com/pollen-robotics/microduck) & [microduck_rl](https://github.com/pollen-robotics/microduck_rl)
* **Hugging Face Hub:** [pollen-robotics/microduck-policies](https://huggingface.co/pollen-robotics/microduck-policies)
* **MuJoCo / DeepMind:** Physics engine contact dynamics & multi-body simulation
* **Graphic Era Hill University, Bhimtal:** Department of Computer Science & Engineering (Course: SCS-701)
  * Student: **Piyush Karnatak** (Roll No: 2361393, Enrollment: 230112314)
  * Internal Guide: **Dr. Shilpa Jain**
  * Head of Department: **Prof. Ankur Singh Bisht**

---
*MIT License. Copyright (c) 2026 Piyush Karnatak.*
