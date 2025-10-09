from openai import OpenAI
import cv2
import base64
import socket
import time
import datetime  


def log_event(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] - {message}")


port1 = 6103
port2 = 6104
ipa = '192.168.3.23'

messages = [
    {"role": "system",
     "content": "I need you to divide the image into 4 quadrants, and when I ask about the location, you should answer only with the quadrant, without comments, for example, 'Lower right'."}
]


# --- Función para recibir la imagen ---
def client():
    log_event("Iniciando función para recibir imagen.")
    host = ipa
    puerto = port1

    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        log_event(f"Intentando conectar al servidor de imágenes en {host}:{puerto}...")
        cliente_socket.connect((host, puerto))
        log_event(f"Conectado exitosamente al servidor de imágenes.")

        with open("Image_received.jpg", "wb") as archivo:
            log_event("Recibiendo datos de la imagen...")
            while True:
                datos = cliente_socket.recv(1024000)
                if not datos:
                    break
                archivo.write(datos)
        log_event("Imagen recibida y guardada como 'Image_received.jpg'.")
    except Exception as e:
        log_event(f"Error al conectar o recibir la imagen: {e}")
    finally:
        cliente_socket.close()
        log_event("Socket del cliente de imágenes cerrado.")


# --- Ejecución principal ---
log_event("Programa iniciado.")
client()

log_event("Configurando cliente de OpenAI.")
client = OpenAI(
    api_key="***" #Coloca aquí tu ID de OpenAI
)


def image_to_base64(file_path):
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


log_event("Codificando la imagen a Base64.")
image_base64 = image_to_base64("Image_received.jpg")

while True:
    log_event("Esperando mensaje del usuario...")
    input_message = input("Esperando el mensaje: ")
    log_event(f"Mensaje recibido: '{input_message}'")

    log_event("Enviando petición a la API de OpenAI...")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": input_message},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{image_base64}",
                        }
                    },
                ],
            }
        ],
    )

    content = response.choices[0].message.content
    log_event(f"Respuesta de ChatGPT recibida: '{content}'")
    print("Respuesta de ChatGPT: " + content)

    global g_sock

    if content == "1":
        log_event("Condición '1' detectada. Preparando para enviar comandos.")
        angle = [1, 1, 1, 1, 1, 1]


        def connect_tcp_server(ip, port):
            global g_sock
            log_event(f"Conectando al servidor del robot en {ip}:{port}")
            g_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            g_sock.connect((ip, port))
            log_event("Conectado al robot.")
            time.sleep(1)

            data = "$20" + str(100 * angle[0]) + "0" + str(90 * angle[1]) + "0" + str(35 * angle[2]) + "0" + str(
                80 * angle[3]) + "0" + str(90 * angle[4]) + str(180 * angle[5]) + "#"
            log_event(f"Enviando comando 1: {data}")
            b_data = bytes(data, encoding="utf8")
            g_sock.send(b_data)
            time.sleep(5)

            data = "$200" + str(95 * angle[0]) + str(150 * angle[1]) + "0" + str(25 * angle[2]) + "00" + str(
                6 * angle[3]) + "0" + str(90 * angle[4]) + str(160 * angle[5]) + "#"
            log_event(f"Enviando comando 2: {data}")
            b_data = bytes(data, encoding="utf8")
            g_sock.send(b_data)
            time.sleep(1)


        def waitClose(sock):
            sock.close()
            log_event("Socket del robot cerrado.")


        if __name__ == '__main__':
            ip = ipa
            port = port2
            try:
                connect_tcp_server(ip, port)
            except KeyboardInterrupt:
                waitClose(g_sock)
                log_event("Programa interrumpido por el usuario.")

    elif content == "2":
        log_event("Condición '2' detectada. Preparando para enviar comandos.")
        angle = [1, 1, 1, 1, 1, 1]


        def connect_tcp_server(ip, port):
            global g_sock
            log_event(f"Conectando al servidor del robot en {ip}:{port}")
            g_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            g_sock.connect((ip, port))
            log_event("Conectado al robot.")
            time.sleep(1)

            data = "$200" + str(85 * angle[0]) + "0" + str(90 * angle[1]) + "0" + str(35 * angle[2]) + "0" + str(
                80 * angle[3]) + "0" + str(90 * angle[4]) + str(180 * angle[5]) + "#"
            log_event(f"Enviando comando 1: {data}")
            b_data = bytes(data, encoding="utf8")
            g_sock.send(b_data)
            time.sleep(5)

            data = "$200" + str(95 * angle[0]) + str(150 * angle[1]) + "0" + str(25 * angle[2]) + "00" + str(
                6 * angle[3]) + "0" + str(90 * angle[4]) + str(160 * angle[5]) + "#"
            log_event(f"Enviando comando 2: {data}")
            b_data = bytes(data, encoding="utf8")
            g_sock.send(b_data)
            time.sleep(1)


        def waitClose(sock):
            sock.close()
            log_event("Socket del robot cerrado.")


        if __name__ == '__main__':
            ip = ipa
            port = port2
            try:
                connect_tcp_server(ip, port)
            except KeyboardInterrupt:
                waitClose(g_sock)
                log_event("Programa interrumpido por el usuario.")

    elif content == "3":
        log_event("Condición '3' detectada. Preparando para enviar comandos.")
        angle = [1, 1, 1, 1, 1, 1]


        def connect_tcp_server(ip, port):
            global g_sock
            log_event(f"Conectando al servidor del robot en {ip}:{port}")
            g_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            g_sock.connect((ip, port))
            log_event("Conectado al robot.")
            time.sleep(1)

            data = "$20" + str(104 * angle[0]) + "0" + str(92 * angle[1]) + "0" + str(15 * angle[2]) + "0" + str(
                85 * angle[3]) + "0" + str(90 * angle[4]) + str(180 * angle[5]) + "#"
            log_event(f"Enviando comando 1: {data}")
            b_data = bytes(data, encoding="utf8")
            g_sock.send(b_data)
            time.sleep(5)

            data = "$200" + str(95 * angle[0]) + str(150 * angle[1]) + "0" + str(25 * angle[2]) + "00" + str(
                6 * angle[3]) + "0" + str(90 * angle[4]) + str(160 * angle[5]) + "#"
            log_event(f"Enviando comando 2: {data}")
            b_data = bytes(data, encoding="utf8")
            g_sock.send(b_data)
            time.sleep(1)


        def waitClose(sock):
            sock.close()
            log_event("Socket del robot cerrado.")


        if __name__ == '__main__':
            ip = ipa
            port = port2
            try:
                connect_tcp_server(ip, port)
            except KeyboardInterrupt:
                waitClose(g_sock)
                log_event("Programa interrumpido por el usuario.")

    elif content == "4":
        log_event("Condición '4' detectada. Preparando para enviar comandos.")
        angle = [1, 1, 1, 1, 1, 1]


        def connect_tcp_server(ip, port):
            global g_sock
            log_event(f"Conectando al servidor del robot en {ip}:{port}")
            g_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            g_sock.connect((ip, port))
            log_event("Conectado al robot.")
            time.sleep(1)

            data = "$200" + str(80 * angle[0]) + "0" + str(90 * angle[1]) + "0" + str(15 * angle[2]) + "0" + str(
                80 * angle[3]) + "0" + str(90 * angle[4]) + str(180 * angle[5]) + "#"
            log_event(f"Enviando comando 1: {data}")
            b_data = bytes(data, encoding="utf8")
            g_sock.send(b_data)
            time.sleep(5)

            data = "$200" + str(95 * angle[0]) + str(150 * angle[1]) + "0" + str(25 * angle[2]) + "00" + str(
                6 * angle[3]) + "0" + str(90 * angle[4]) + str(160 * angle[5]) + "#"
            log_event(f"Enviando comando 2: {data}")
            b_data = bytes(data, encoding="utf8")
            g_sock.send(b_data)
            time.sleep(1)


        def waitClose(sock):
            sock.close()
            log_event("Socket del robot cerrado.")


        if __name__ == '__main__':
            ip = ipa
            port = port2
            try:
                connect_tcp_server(ip, port)
            except KeyboardInterrupt:
                waitClose(g_sock)
                log_event("Programa interrumpido por el usuario.")