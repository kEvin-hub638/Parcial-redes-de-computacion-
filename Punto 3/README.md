# Simulación del Comportamiento de TCP Tahoe

Este ejercicio implementa una simulación básica del comportamiento de la ventana de congestión (cwnd) en TCP Tahoe utilizando Python. El objetivo es demostrar cómo TCP ajusta la ventana de congestión en función de eventos de éxito y pérdida de paquetes, simulando el proceso de Slow Start y la reacción ante la congestión en la red.

## Descripción

La simulación se basa en los siguientes conceptos:
- Ventana de Congestión (cwnd): Inicialmente se establece en 1.
- Transmisiones: Se simulan 20 transmisiones de datos.
- Eventos de Transmisión:
  - Éxito: Con una probabilidad del 80%, se incrementa el valor de cwnd en 1.
  - Pérdida: Con una probabilidad del 20%, se simula la pérdida de un paquete y la ventana de congestión se reinicia a 1, emulando el comportamiento de TCP Tahoe ante la congestión.

## Estructura del Código

El código se encuentra en un único archivo Python y está organizado de la siguiente manera:
- Importación de módulos: Se utiliza el módulo random para simular el comportamiento aleatorio de las transmisiones.
- Función simular_tcp_tahoe():
  - Inicializa la ventana de congestión (cwnd).
  - Define el número total de transmisiones y las probabilidades de éxito y pérdida.
  - Ejecuta un ciclo de 20 transmisiones en el que se decide aleatoriamente si la transmisión es exitosa o falla.
  - Imprime el estado de cada transmisión junto con el valor actualizado de cwnd.

## Ejemplo de Salida

![imagen13](https://github.com/ALMA3112/Parcial-redes-de-computacion-/blob/main/Imagenes/imagen_2025-03-12_005542478.png)
