# coding=utf-8
import socket
import os
import time
from Arm_Lib import Arm_Device
import cv2
import datetime


def log_event(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] - {message}")


port1 = 6103
port2 = 6104

global g_init
g_init = False

log_event("Iniciando el programa y conexión con el brazo robótico.")
Arm = Arm_Device()

log_event("Moviendo el brazo a la posición inicial 1.")
Arm.Arm_serial_servo_write6(80, 130, 25, 10, 90, 130, 2000)
time.sleep(2)

log_event("Moviendo el brazo a la posición inicial 2.")
Arm.Arm_serial_servo_write6(95, 170, 5, 4, 90, 160, 2000)
time.sleep(2)

log_event("Iniciando captura de imagen con la cámara.")
cap = cv2.VideoCapture(1)
leido, frame = cap.read()

if leido == True:
    cv2.imwrite("captura1.jpg", frame)
    log_event("Foto tomada y guardada como 'captura1.jpg'.")
else:
    log_event("Error: No se pudo acceder a la cámara.")
cap.release()
log_event("Cámara liberada.")


def servidor():
    host = '0.0.0.0'
    puerto = port1

    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((host, puerto))
    servidor_socket.listen(1)
    log_event(f"Servidor de imágenes esperando conexión en {host}:{puerto}...")

    conn, addr = servidor_socket.accept()
    log_event(f"Conexión para enviar imagen establecida desde: {addr}")

    try:
        with open("captura1.jpg", "rb") as archivo:
            log_event("Enviando imagen 'captura1.jpg'...")
            chunk = archivo.read(1024000)
            conn.sendall(chunk)
            time.sleep(5)
        log_event("Imagen enviada correctamente.")
    except FileNotFoundError:
        log_event("Error: El archivo 'captura1.jpg' no se encontró.")
    except Exception as e:
        log_event(f"Error al enviar la imagen: {e}")
    finally:
        conn.close()
        servidor_socket.close()
        log_event("Servidor de imágenes cerrado.")
        time.sleep(5)


servidor()


def getLocalip():
    ip = os.popen("/sbin/ifconfig eth0 | grep 'inet' | awk '{print $2}'").read().strip()
    if not ip:
        ip = os.popen("/sbin/ifconfig wlan0 | grep 'inet' | awk '{print $2}'").read().strip()
    return ip if ip else 'x.x.x.x'


def Analysis(socket, cmd):
    log_event(f"Analizando comando recibido: {cmd}")
    try:
        check = cmd[1:3]
        if check == '20' and len(cmd) == 22:
            s1_angle = int(cmd[3:6])
            s2_angle = int(cmd[6:9])
            s3_angle = int(cmd[9:12])
            s4_angle = int(cmd[12:15])
            s5_angle = int(cmd[15:18])
            s6_angle = int(cmd[18:21])
            log_event(
                f"Comando válido. Moviendo servomotores a: S1={s1_angle}, S2={s2_angle}, S3={s3_angle}, S4={s4_angle}, S5={s5_angle}, S6={s6_angle}")
            Arm.Arm_serial_servo_write6(s1_angle, s2_angle, s3_angle, s4_angle, s5_angle, s6_angle, 2000)
        else:
            log_event("Error: Formato de comando incorrecto.")
    except Exception as e:
        log_event(f"Error al procesar el comando: {e}")


def start_tcp_server(ip, port):
    global g_init, g_socket
    g_init = True
    log_event("Iniciando servidor TCP para recibir comandos.")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((ip, port))
    sock.listen(5)
    while True:
        conn, address = sock.accept()
        g_socket = conn
        log_event(f"Cliente de comandos conectado desde: {address}")
        while True:
            try:
                cmd = g_socket.recv(1024).decode(encoding="utf-8")
                if not cmd:
                    log_event("Cliente de comandos desconectado.")
                    break

                index1 = cmd.find("$")
                index2 = cmd.find("#")
                if index1 >= 0 and index2 > index1:
                    Analysis(g_socket, cmd[index1:index2 + 1])
            except (ConnectionResetError, BrokenPipeError):
                log_event("Error de conexión con el cliente, se ha desconectado abruptamente.")
                break


def waitClose():
    global g_init, g_socket
    g_init = False
    if 'g_socket' in globals() and g_socket:
        g_socket.close()
    log_event("Socket cerrado.")


if __name__ == '__main__':
    try:
        port = port2
        if g_init == False:
            while True:
                log_event("Obteniendo dirección IP local...")
                ip = getLocalip()
                log_event(f"IP obtenida: {ip}:{port}")
                if ip != "x.x.x.x":
                    break
                time.sleep(1)
        start_tcp_server(ip, port)
    except KeyboardInterrupt:
        waitClose()
        log_event("Programa cerrado por el usuario (Ctrl+C).")
        pass