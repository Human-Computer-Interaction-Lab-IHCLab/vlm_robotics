# Control determinista + LLM/VLM informado por simetría para manipulación robótica de objetos (DOFBOT educativo)

🎥 **Video demostrativo**  
[![IA generativa y robótica: el DOFBOT informado por simetría](https://img.youtube.com/vi/3aAaTQduSoA/0.jpg)](https://youtu.be/3aAaTQduSoA)  
*Haz clic en la imagen para verlo en YouTube.*

**[🌐 Read this in English / Leer en inglés](README.md)**

---

## 📚 Cita

Si utilizas o haces referencia a este repositorio, por favor cita el artículo publicado:

> **Gudiño-Lau, J., Durán-Fonseca, M., Anido-Rifón, L. E., & Santana-Mancilla, P. C.**  
> *A Symmetry-Informed Multimodal LLM-Driven Approach to Robotic Object Manipulation: Lowering Entry Barriers in Mechatronics Education.*  
> **Symmetry**, 17(10), 1756. [https://doi.org/10.3390/sym17101756](https://doi.org/10.3390/sym17101756)

---

Este repositorio proporciona un **marco híbrido reproducible** que integra un **modelo de lenguaje e imagen (LLM/VLM)** como módulo de razonamiento semántico con **cinemática inversa determinista** para la manipulación robótica de objetos.  
El sistema se implementa en el brazo robótico educativo **Yahboom DOFBOT** y demuestra cómo la simetría puede aplicarse **como principio de diseño**, más que como una característica aprendida.

> Diseñado con fines **educativos y de investigación**, este proyecto busca reducir las barreras de entrada en la educación en mecatrónica mostrando cómo la IA generativa puede interactuar con el control robótico determinista.

---

## 🧩 Descripción general

### Lado del robot (`MainRobot.py`)
- Inicializa y calibra el brazo robótico.  
- Captura una imagen de cámara y la expone a través de dos servidores TCP:  
  - **Servidor de imágenes** en el puerto `6103`.  
  - **Servidor de comandos** en el puerto `6104`.

### Lado del cliente (`RuedaColorEs.py`)
- Se conecta al servidor de imágenes del robot para obtener el último fotograma.  
- Envía tanto **texto como imagen** a un modelo multimodal de OpenAI (`gpt-4o`).  
- Interpreta la respuesta del modelo (por ejemplo, “abajo a la derecha”) y envía los comandos de movimiento correspondientes al robot mediante TCP.

---

## ⚙️ Requisitos

### Hardware
- Brazo robótico Yahboom DOFBOT de 6 grados de libertad (o compatible)  
- Cámara USB o CSI  
- Conexión de red local entre el robot y el cliente  

## ⚖️ Licencia

Este proyecto se publica bajo la Licencia MIT, que permite su uso, modificación y redistribución con fines educativos y de investigación.  
onsulta el archivo [LICENSE](LICENSE) para más detalles.
