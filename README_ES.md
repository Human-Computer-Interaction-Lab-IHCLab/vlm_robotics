# Sistema híbrido informado por simetría basado en LLM/VLM para manipulación robótica educativa

**[📘 Read this in English / Leer en inglés](README.md)**

Este repositorio contiene un sistema reproducible que integra un **modelo multimodal de lenguaje (LLM/VLM)** como sensor semántico con **control determinista basado en cinemática inversa**, aplicado a un brazo robótico **Yahboom DOFBOT**.

El proyecto demuestra cómo la **razonamiento generativo** puede combinarse con algoritmos deterministas para ejecutar tareas de manipulación de objetos, aplicando la **simetría como principio de diseño** en lugar de una característica aprendida.

---

## 🌐 Arquitectura general

- **Lado del robot (`MainRobot.py`):**  
  Inicia el brazo, captura una imagen de la cámara y levanta dos servidores TCP:
  - **Servidor de imagen** en el puerto **6103**  
  - **Servidor de comandos** en el puerto **6104**

- **Lado del cliente (`RuedaColorEs.py`):**  
  Descarga la imagen, la envía junto con un mensaje de texto al modelo multimodal de OpenAI (`gpt-4o`) y, según la respuesta (por ejemplo, “abajo derecha”), envía los comandos de movimiento correspondientes al servidor del robot.

---

## ⚙️ Requisitos

**Hardware**
- Brazo robótico DOFBOT (o equivalente de 6 GDL)
- Cámara USB o CSI conectada al robot

**Software**
- Python 3.8 o superior
- Librerías:
  ```bash
  pip install opencv-python openai
