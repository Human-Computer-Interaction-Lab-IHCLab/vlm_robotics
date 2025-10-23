# Symmetry-Informed LLM/VLM + Deterministic Control for Robotic Object Manipulation (Educational DOFBOT)

🎥 **Video**  
[![Generative AI Meets Robotics: The Symmetry-Informed DOFBOT](https://img.youtube.com/vi/2ACQrcsiW0E/0.jpg)](https://youtu.be/2ACQrcsiW0E)  
*Click the image to watch on YouTube.*

**[📘 Read this in Spanish / Leer en español](README_ES.md)**

---

## 📚 Citation

If you use or reference this repository, please cite the published paper:

> **Gudiño-Lau, J., Durán-Fonseca, M., Anido-Rifón, L. E., & Santana-Mancilla, P. C.**  
> *A Symmetry-Informed Multimodal LLM-Driven Approach to Robotic Object Manipulation: Lowering Entry Barriers in Mechatronics Education.*  
> **Symmetry**, 17(10), 1756. [https://doi.org/10.3390/sym17101756](https://doi.org/10.3390/sym17101756)

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
- Yahboom DOFBOT 6-DoF robotic arm (or compatible)  
- USB or CSI camera  
- Local network connection between robot and client  


## ⚖️ License

This project is released under the **MIT License**, allowing free use, modification, and redistribution for educational and research purposes.  
See the [LICENSE](LICENSE) file for details.
