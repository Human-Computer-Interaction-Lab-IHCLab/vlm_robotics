# Symmetry-Informed LLM/VLM + Deterministic Control for Robotic Object Manipulation (Educational DOFBOT)

**[📘 Read this in Spanish / Leer en español](README_ES.md)**

---

This repository provides a **reproducible hybrid framework** that integrates a **multimodal Large Language Model (LLM/VLM)** as a semantic reasoning module with **deterministic inverse kinematics** for robotic object manipulation.  
The system is implemented on the **Yahboom DOFBOT** educational arm and demonstrates how symmetry can be applied **as a design principle** rather than a learned feature.

> Designed for **educational and research purposes**, this project aims to lower entry barriers in mechatronics education by showing how generative AI can interact with deterministic robotic control.

---

## 🧩 Overview

### Robot Side (`MainRobot.py`)
- Initializes and homes the robotic arm.
- Captures a camera image and exposes it through two TCP servers:
  - **Image Server** on port `6103`.
  - **Command Server** on port `6104`.

### Client Side (`RuedaColorEs.py`)
- Connects to the robot’s image server to retrieve the latest frame.
- Sends both **text and image** to an OpenAI multimodal model (`gpt-4o`).
- Interprets the model’s reply (e.g., “lower right”) and sends the corresponding motion commands to the robot via TCP.

---

## ⚙️ Requirements

### Hardware
- Yahboom DOFBOT 6-DoF arm (or compatible)
- Camera (USB/CSI)
- Local network connection between robot and client

### Software
- Python 3.8+
- Packages:
  ```bash
  pip install opencv-python openai
