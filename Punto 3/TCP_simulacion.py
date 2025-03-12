import random

def simular_tcp_tahoe():
    # Inicializar la ventana de congestión (cwnd)
    cwnd = 1
    
    # Número de transmisiones a simular
    num_transmisiones = 20
    # Probabilidad de éxito y pérdida
    probabilidad_exito = 0.8  # 80% de éxito
    probabilidad_perdida = 0.2  # 20% de pérdida
    
    # Simulación de transmisiones
    for i in range(1, num_transmisiones + 1):
        # Simular si la transmisión es exitosa o se pierde
        if random.random() < probabilidad_exito:
            # Transmisión exitosa: incrementar cwnd
            cwnd += 1
            print(f"Transmisión {i}: Éxito - cwnd = {cwnd}")
        else:
            # Pérdida de paquete: reiniciar cwnd a 1
            cwnd = 1
            print(f"Transmisión {i}: Pérdida - cwnd = {cwnd}")

simular_tcp_tahoe()