## 1. Introduccion
El objetivo de este punto es simular una arquitectura de cliente-servidor utilizando sockets en Python para demostrar la capacidad de manejar múltiples conexiones simultáneas. Se desarrollaron dos programas:
- Servidor: Escucha en el puerto 2010, acepta conexiones y responde a los clientes.
- Cliente: Se conecta al servidor, envía un mensaje indentificándose y espera la confirmación.

La finalidad de este ejercicio es evidenciar el manejo de conexiones TCP y la implemnetación de comunicación bidireccional, fundamental en redes de computadoras.

## 2. Objetivos
- Implementar un servidor TCP que acepte múltiples conexiones de clientes mediante el uso de threading.
- Desarrollar un cliente que conecte al servidor y envíe su identificación
- Verificar la comunicación entre cliente y servidor, asegurando que cada mensaje enviado sea reconocido y respondido.
- Realizar pruebas ejecutando simultáneamente al menos cuatro clientes, demostrando la robustez del sistema.

## 3. Descripción del Sistema
- Servidor
  - Puerto de escucha: 2010.
  - Manejo de múltiples conexiones: Se utiliza threading para atender cada cliente de forma independiente.
  - Proceso de conexión: Al conectar un cliente, se le solicita su nombre, luego, se reciben mensajes y se envía una respuesta de confirmación.
  - Gestión de mensajes: Se implemnetan controles para la longitud del mensaje y la cantidad de mensajes por segundo, protegiendo el servidor de posibles abusos.
  - LocalHost: Para conectar diferentes computadoras se tendria que cambiar los otros computadores a la siguiente IP: 192.168.0.10

- Cliente
  - Conexión: Se conecta a localHost en el puerto 2010.
  - Interacción: Solicita al usuario su nombre, envía un mensaje de saludo formateado y muetra en consola la respuesta del servidor.
  - Comunicación continua: Permite enviar múltiples mensajes, cerrándose la conexión cuando se ingresa el comando de salida.

## 4. Pruebas Realizadas
- Prueba de Conexión Simultánea: Se ejecutaron cuatro instancias del cliente de forma simultánea, verificando que el servidor acepta y responde a cada conexión sin interrupciones.
- Verificación de Mensajes: Cada cliente envió un mensaje de saludo y el servidor respondió confirmando la recepción, mostrando en consola la identificación y el mensaje de cada cliente.
- Control de Errores: Se validó que el servidr desconecta clientes que exceden el límite de longitud de mensajes o envían mensajes a una velocidad excesiva.

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
