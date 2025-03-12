## 1. Introduccion
El objetivo de este punto es simular una arquitectura de cliente-servidor utilizando sockets en Python para demostarr la capacidad de manejar múltiples conexiones simultáneas. Se desarrollaron deos programas:
- Servidor: Escucha en el puerto 2010, apecta conexiones y responde a los clientes.
- Cliente: Se conecta al servidor, envía un mensaje indentificándose y espera la confirmación.

La finalidad de este ejercicio es evidenciar el manejo de conexiones TCP y la implemnetación decomunicación bidireccional, fundamental en redes de computadoras.

## 2. Objetivos
- Implementar un seridor TCP que acepte múltiples conexiones de clientes mediante el uso de threading.
- Desarrollar un cliente que conecte al servidor y envíe su identificación
- Verificar la comunicación entre cliente y servidor, asegurando que cada mensaje enviado sea reconocido y respondido.
- Realizar pruebas ejecutando simultáneamente al menos cuatro clientes, demostrando la robustez del sistema.

## 3. Descripción del Sistema
- Servidor
  - Puerto de escucha: 2010.
  - Manejo de múltiples conexiones: Se utiliza threading para atender cada cliente de forma independiente.
  - Proceso de conexión: Al conectar un cliente, se le solicita su nombre, luego, se reciben mensajes y se envía una respuesta de confirmación.
  - Gestión de mensajes: Se implemnetan controles para la longitud del mensaje y la cantidad de mensjaes por segundo, protegiendo el servidor de posibles abusos.

- Cliente
  - Conexión: Se conecta a localhost en el puerto 2010.
  - Interacción: Solicita al usuario su nombre, envía un mensaje de saludo formateado y muetra en consola la respuesta del servidor.
  - Comunicación continua: Permite enviar múltiples mensajes, cerrándose la conexión cuando se ingresa el comando de salida.

## Pruebas Realizadas
- Prueba de Conexión Simultánea: Se ejecutaron cuatro instancias del cliente de forma simultánea, verificando que el servidor acepta y responde a cada conexión sin interrupciones.
- Verificación de Mensajes: Cada cliente envió un mensaje de saludo y el servidor respondió confirmando la recepción, mostrando en consolala identificación y el mensaje de cada cliente.
- Control de Errores: Se validó que el servidr desconecta clientes que exceden el límite de longitud de mensajes o envían mensajes a una velocidad excesiva.

## Evidencias de Ejecución



