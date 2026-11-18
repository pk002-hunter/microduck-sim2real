# Product Truth: Microduck Sim-to-Real Kinematics & Ground Station

## Identity
- **Name:** Microduck Sim-to-Real Locomotion & Kinematic Inspector
- **Author:** Piyush Karnatak (Graphic Era Hill University, B.Tech CSE, Roll: 2361393)
- **Academic Context:** SCS-701 Industrial Training Seminar, Evaluation on Nov 20, 2026.
- **Guide:** Dr. Shilpa Jain | Prof. Ankur Singh Bisht (HOD)

## Purpose & Core Job
Provide an interactive, industrial-grade simulation and telemetry interface for the open-source Microduck 14-DoF bipedal robot. The platform addresses the Sim-to-Real transfer gap by modeling Dynamixel XL-330 actuator backlash (BAM) and demonstrating autonomous self-righting (VelStand).

## Users & Situations
- **Primary User:** Robotics student & evaluators during seminar demonstration.
- **Job:** Inspect individual leg kinematics in variable slow-motion (1.0x to 0.05x Ultra Slo-Mo), analyze neural synaptic firing differences between baseline and backlash-compensated policies, and examine ground contact physics during recovery from falls.

## Platform & Constraints
- **Platform:** Web (WebGL Three.js frontend + FastAPI 50 Hz physics engine + CasaOS Docker container on Ubuntu Server 192.168.1.15).
- **Offline Guarantee:** 100% functional without external internet connectivity using bundled Three.js and Chart.js assets.
- **Hardware Target:** Low-power CPU inference (ONNX Runtime, 0.05ms execution).
