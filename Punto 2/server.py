import socket
import threading
import time  #Importa el modulo time para registrar tiempos (control de velocidad)

HOST ="127.0.0.1"
PORT = 2010

MAX_CONEXIONES = 10
MAX_MENSAJES_SEGUNDO = 5
MAX_LONGITUD_MENSAJE = 1000

clientes =[] #Lista que almacena los sockets de los clientes conectaods
tiempo_mensaje = {} #Diccionario para registrar los tiempos de envio de mensajes para cada cliente

def cliente(socket_cliente, direccion_cliente):
    print(f"[+] Conexion establecida con {direccion_cliente}")
    clientes.append(socket_cliente)
    tiempo_mensaje[direccion_cliente] = [] #Inicializa la lista de tiempos para este ciente

    socket_cliente.send("Por favor, envia tu  nombre:". encode('utf-8'))
    nombre_cliente = socket_cliente.recv(1024).decode('utf-8')
    print(f"[+] {direccion_cliente} se ha identificado como {nombre_cliente}")

    while True:
        try:
            mensaje = socket_cliente.recv(1024).decode('utf-8')#Recibe el mensaje del cliente

            #Validacion: si el mensaje excede la longitud maxima permitida, se desconecta al cliente
            if len(mensaje) > MAX_LONGITUD_MENSAJE:
                print(f"[-] {direccion_cliente} envio un mensaje demasido largo. Desconectando...")
                socket_cliente.send("Error: Mensaje demasiado largo.".encode('utf-8'))
                socket_cliente.close()
                break

            tiempo = time.time()
            tiempo_mensaje[direccion_cliente].append(tiempo)
            # Mantiene solo los tiempos de los mensajes enviados en el último segundo
            tiempo_mensaje[direccion_cliente]=[
                t for t in tiempo_mensaje[direccion_cliente] if tiempo - t < 1
            ]

            # Si se excede el límite de mensajes por segundo, se notifica y se desconecta el cliente
            if len(tiempo_mensaje[direccion_cliente]) > MAX_MENSAJES_SEGUNDO:
                print(f"[-] {direccion_cliente} exedio el limite de mensajes por segundo. Desconectando...")
                socket_cliente.send("Error: Demasiados mensajes en poco tiempo.".encode('utf-8'))
                socket_cliente.close()
                break

            # Si el mensaje es "salir", se interpreta como una solicitud de desconexión
            if mensaje.lower() == "salir":
                print(f"[-] {direccion_cliente} se ha desconectado. ")
                clientes.remove(socket_cliente)
                socket_cliente.close()
                break

            print(f"Mensaje de {nombre_cliente} ({direccion_cliente}: {mensaje})")
            broadcast(f"{nombre_cliente}: {mensaje}", socket_cliente)# Reenvia mensaje a los demas clientes

        except Exception as e:
            print(f"[-] Error con {direccion_cliente}: {e}")
            clientes.remove(socket_cliente)
            socket_cliente.close()
            break

def broadcast(mensaje, sender_socket=None):
    for cliente in clientes:
         # Evita enviar el mensaje al socket que lo originó
        if cliente != sender_socket:
            try:
                cliente.send(mensaje.encode('utf-8'))
            except:
                cliente.close()
                clientes.remove(cliente)

def mensaje_servidor():
    while True:
        mensaje = input()
        if mensaje.lower() == "salir":
            parar_servidor()
            break
        broadcast(f"Servidor:{mensaje}")

def parar_servidor():
    broadcast("El servidor se esta cerrando. Desconectando...")

    for cliente in clientes:
        cliente.close()

    print(f"[!] Servidor cerrado.")
    exit()

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen(MAX_CONEXIONES)
    print(f"[*] Sevidor escuchando en {HOST}:{PORT} (Maximo de conexiones: {MAX_CONEXIONES})")

    # Inicia un hilo para permitir al servidor enviar mensajes manualmente
    servidor_thread = threading.Thread(target= mensaje_servidor)
    servidor_thread.start()

    try:
        while True:
            # Verifica que no se supere el límite de conexiones
            if len(clientes) >= MAX_CONEXIONES:
                print("[!] Limite de conexiones alcanzado. Rechazando nuevas conexiones.")
                continue

            socket_cliente,direccion_cliente = servidor.accept()
            # Crea un hilo para manejar la comunicación con el cliente conectado
            thread = threading.Thread(target= cliente, args=(socket_cliente, direccion_cliente))
            thread.start()
            print(f"[+] Conexiones activas: {len(clientes)}")
    
    except KeyboardInterrupt:
        # Permite detener el servidor con CTRL+C
        print("\n[!] Deteniendo el sevidor...")
        parar_servidor()

if __name__ == "__main__":
    iniciar_servidor()
