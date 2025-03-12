## 1. Introducción
El propósito de este punto es simular una arquitectura de cliente-servidor utilizando **sockets** en **Python**, demostrando la capacidad de gestionar múltiples conexiones simultáneamente. Se implementaron dos programas:  
- **Servidor:** Escucha en el puerto **2010**, acepta conexiones y responde a los clientes.  
- **Cliente:** Se conecta al servidor, envía un mensaje identificándose y espera una confirmación.  

Este ejercicio tiene como finalidad evidenciar el manejo de conexiones **TCP** y la implementación de comunicación bidireccional, aspecto clave en redes de computadoras.  

## 2. Objetivos
- Diseñar un servidor **TCP** que pueda aceptar múltiples conexiones de clientes utilizando **hilos**.  
- Desarrollar un cliente que establezca conexión con el servidor y envíe su identificación.  
- Comprobar la comunicación entre cliente y servidor, asegurando que cada mensaje transmitido sea recibido y respondido correctamente.  
- Realizar pruebas con al menos cuatro clientes en ejecución simultánea para demostrar la estabilidad del sistema.  

## 3. Descripción del Sistema
- **Servidor**  
  - **Puerto de escucha:** **2010**.  
  - **Gestión de múltiples conexiones:** Se emplea **threading** para manejar cada cliente de manera independiente.  
  - **Proceso de conexión:** Al conectarse un cliente, se le solicita su nombre, luego se reciben mensajes y se envía una respuesta de confirmación.  
  - **Administración de mensajes:** Se implementan controles para la longitud de los mensajes y la frecuencia de envío, evitando posibles sobrecargas en el servidor.  
  - **LocalHost:** Para conectar computadoras diferentes, es necesario configurar la IP de los otros dispositivos en **192.168.0.10**.  

- **Cliente**  
  - **Establecimiento de conexión:** Se conecta a **localHost** en el puerto **2010**.  
  - **Interacción:** Solicita el nombre del usuario, envía un mensaje de presentación y muestra en consola la respuesta del servidor.  
  - **Comunicación persistente:** Permite el envío de múltiples mensajes y finaliza la conexión cuando se introduce el comando de salida.  

## 4. Pruebas Realizadas
- **Prueba de Conexión Simultánea:** Se ejecutaron cuatro instancias del cliente al mismo tiempo, verificando que el servidor acepta y responde a cada conexión sin fallas.  
- **Validación de Mensajes:** Cada cliente envió un mensaje de saludo y el servidor confirmó su recepción, mostrando en consola el identificador y contenido del mensaje.  
- **Manejo de Errores:** Se comprobó que el servidor desconecta a los clientes que superan el límite de caracteres en los mensajes o envían datos de forma excesivamente rápida.  


## 5. Evidencias de Ejecución
- Iniciar Servidor:

![Imagen3](https://github.com/ALMA3112/Parcial-redes-de-computacion-/blob/main/Imagenes/Iniciar_Servidor.png)

- Conexion Cliente1:

![imagen4](https://github.com/ALMA3112/Parcial-redes-de-computacion-/blob/main/Imagenes/Conexion%20cliente1.png)

- Conexion Cliente2:

![Imagen5](https://github.com/ALMA3112/Parcial-redes-de-computacion-/blob/main/Imagenes/Conexion%20Cliente2.png)

- Conexion Cliente3:

![imagen6](https://github.com/ALMA3112/Parcial-redes-de-computacion-/blob/main/Imagenes/Conexion%20Cliente3.png)

- Conexion Cliente4:

![imagen7](https://github.com/ALMA3112/Parcial-redes-de-computacion-/blob/main/Imagenes/Conexion%20cliente4.png)

- Comunicacion entre clientes:

![imagen8](https://github.com/ALMA3112/Parcial-redes-de-computacion-/blob/main/Imagenes/Comunicacion%20entre%20clientes.png)

- Comunicacion del servidor hacia los clientes:

![imagen9](https://github.com/ALMA3112/Parcial-redes-de-computacion-/blob/main/Imagenes/Comunicacion%20del%20servidor%20hacia%20los%20clientes.png)

- Recepcion del servidor:

![imagen10](https://github.com/ALMA3112/Parcial-redes-de-computacion-/blob/main/Imagenes/Recepcion%20del%20servidor.png)

- Cerrar servidor vista servidor:

![imagen11](https://github.com/ALMA3112/Parcial-redes-de-computacion-/blob/main/Imagenes/Cerrar%20servidor%20vista%20seridor.png)

- Cerrar servidor vista cliente:

![imagen12](https://github.com/ALMA3112/Parcial-redes-de-computacion-/blob/main/Imagenes/Cerrar%20servidor%20vista%20cliente.png)
