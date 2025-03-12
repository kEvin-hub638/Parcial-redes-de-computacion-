import socket
import threading

HOST = input("Ingresa la IP del servidor: ")
PORT = 2010

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

def recibir_mensajes():
    while True:
        try:
            mensaje = cliente.recv(1024).decode('utf-8')
            print(mensaje)
        except Exception as e:
            # En caso de error (por ejemplo, desconexión), muestra el error y cierra el socket
            print(f"[-] Error al recibir mensajes: {e}")
            cliente.close()
            break

def enviar_mensaje():
    nombre_cliente = input("Ingresa tu nombre: ")
    cliente.send(nombre_cliente.encode('utf-8'))

    while True:
        # Lee el mensaje ingresado por el usuario
        mensaje= input()
        try:
            cliente.send(mensaje.encode('utf-8'))
            # Si el usuario ingresa "salir", se cierra el socket y se rompe el bucle
            if mensaje.lower() == "salir":
                cliente.close()
                break
        except Exception as e:
            # En caso de error al enviar el mensaje, muestra el error y cierra el socket
            print(f"[-] Error al enviar mensajes: {e}")
            cliente.close()
            break

# Crea un hilo para recibir mensajes y lo inicia
recibir_thread = threading.Thread(target= recibir_mensajes)
recibir_thread.start()

# Crea un hilo para enviar mensajes y lo inicia
enviar_thread = threading.Thread(target= enviar_mensaje)
enviar_thread.start()