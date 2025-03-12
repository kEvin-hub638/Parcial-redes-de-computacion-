# Simulación del Funcionamiento de TCP Tahoe

Este ejercicio desarrolla una simulación sencilla del comportamiento de la ventana de congestión (**cwnd**) en **TCP Tahoe** utilizando **Python**. Su propósito es ilustrar cómo **TCP** ajusta dinámicamente la ventana de congestión en respuesta a eventos de éxito y pérdida de paquetes, simulando los mecanismos de **Slow Start** y la reacción ante congestión en la red.

## Descripción

La simulación se basa en los siguientes principios:
- **Ventana de Congestión (cwnd):** Se inicializa con un valor de 1.
- **Transmisiones:** Se simulan **20 envíos** de datos.
- **Eventos durante la transmisión:**
  - **Éxito:** Con una probabilidad del **80%**, la ventana de congestión aumenta en 1.
  - **Pérdida:** Con una probabilidad del **20%**, se simula la pérdida de un paquete y **cwnd** se restablece a 1, replicando la respuesta de **TCP Tahoe** ante la congestión.

## Estructura del Código

El código se encuentra en un único archivo **Python** y está organizado de la siguiente manera:
- **Importación de módulos:** Se emplea el módulo `random` para modelar el comportamiento aleatorio de las transmisiones.
- **Función `simular_tcp_tahoe()`:**  
  - Inicializa la ventana de congestión (**cwnd**).  
  - Define el número total de transmisiones y las probabilidades de éxito y falla.  
  - Realiza un ciclo de **20 transmisiones**, determinando de manera aleatoria si la transmisión es exitosa o si se produce una pérdida.  
  - Muestra en pantalla el estado de cada transmisión junto con el valor actualizado de **cwnd**.  


## Ejemplo de Salida

![imagen13](https://github.com/ALMA3112/Parcial-redes-de-computacion-/blob/main/Imagenes/imagen_2025-03-12_005542478.png)
