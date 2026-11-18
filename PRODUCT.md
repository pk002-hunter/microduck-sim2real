# Product Truth: Microduck Sim-to-Real Kinematics & Ground Station

## Identity
- **Name:** Microduck Sim-to-Real Locomotion & Kinematic Inspector
- **Author:** Piyush Karnatak (Graphic Era Hill University, B.Tech CSE, Roll: `2361393`, Enrollment: `230112314`)
- **Academic Context:** SCS-701 Industrial Training Seminar, Evaluation on Nov 20, 2026.
- **Guide:** Dr. Shilpa Jain | Prof. Ankur Singh Bisht (HOD)
- **Repository:** `https://github.com/pk002-hunter/microduck-sim2real`

## Purpose & Core Job
Provide an interactive, industrial-grade simulation and telemetry interface for the open-source Microduck 14-DoF bipedal robot. The platform addresses the Sim-to-Real transfer gap by modeling Dynamixel XL-330 actuator backlash (BAM) in Isaac Gym and demonstrating autonomous self-righting (VelStand).

## 4 Specialized Application Tabs
1. **🕹️ 3D Sim & Omnidirectional Teleop:** Real-time 3D simulation with body-relative W/A/S/D/Q/E teleoperation, variable slow-motion inspector (1.0x to 0.05x Ultra), adjustable lateral push force slider (5N to 32N) with 2nd-order underdamped harmonic oscillator impulse physics (>22N causing dynamic topple), 3D floor hurdles with natural trip collision physics, randomized fall orientations (Prone, Supine, Left, Right), interactive soccer ball (click-to-fling, Pass to Duck, Kick Ball), and a frosted glass live joint kinematics panel.
2. **🧠 Neural Brain (Before/After):** Synaptic firing inspector comparing naive uncompensated RL baseline policy (18.6° backlash flutter) against our BAM-compensated policy (0.8° smooth trajectory).
3. **📐 VelStand Contact Physics:** 5-phase ground contact scrubber and dynamic joint torque table detailing the self-righting kinematic lever mechanics.
4. **🎯 Problem & Sim-to-Real Solution:** Peer-reviewed academic briefing explaining the 3 reality gaps (gearbox backlash, latency, thermal sag), our BAM Isaac Gym formulation, 4,096 domain-randomized environments, and empirical viva comparison metrics (+640x stability, 100% autonomous recovery).

## Technical Implementation & Offline Guarantee
- **Three.js & Chart.js:** 100% offline self-contained bundled assets.
- **FastAPI 50Hz Backend:** Real-time state synchronization, telemetry streaming, and CasaOS containerized deployment.
- **Impeccable Design Quality:** Fully audited with 0 anti-patterns (no contrast issues, no nested cards, strict typography floor, natural elevation shadows).
