# Preguntas
## 1. ¿Cómo contribuye la Transformada de Fourier al análisis de señales en la capa física?

La Transformada de Fourier es una herramienta súper útil para analizar señales en la capa física porque permite verlas desde otra perspectiva: en lugar de observar cómo cambian en el tiempo, nos muestra qué frecuencias la componen. Esto es importante porque en las redes de comunicación, las señales pueden sufrir interferencias, distorsiones o pérdidas de información, y con esta transformación podemos identificar problemas y mejorarlos.

Dos aplicaciones concretas de la Transformada de Fourier en el análisis de señales son:

Filtrado de señales: Permite separar las frecuencias útiles de aquellas que generan ruido, ayudando a mejorar la calidad de la transmisión.
Optimización del ancho de banda: Analizando el espectro de la señal, se puede ver qué frecuencias están ocupadas y cuáles se pueden aprovechar mejor en la transmisión de datos.

## 2. Señales compuestas y espectro de frecuencias

Si la señal que se esta trasmitiendo es periódica y está compuesta por la suma de tres sinusoides de diferentes frecuencias de f1, fa2 y f3. La señal de este tiempo se puede expresar de la sigueinte manera:

![Imagen 1](https://github.com/ALMA3112/Parcial-redes-de-computacion-/blob/main/Imagenes/Imagen1.jpg)

en  donde  A1, A2 Y A3 son las amplitudes que le correponden a cada sinusoide.
Cuando se aplica la Transformcada de Fourier a x(t), se esta transformando la señal del domino del tiempo al dominio de la frecuencia. El resultado es una representacion la cual muestra las constribuciones de cada frecuencia.Esto matematicamente se ve la transformada de afaourier de una sinusoide se expresa mediante funciones delta de Dirac, para este caso en especifico, la Transformada de Fourier X(f) de x(t) es:

![Imagen 2](https://github.com/ALMA3112/Parcial-redes-de-computacion-/blob/main/Imagen2.jpg)

¿Que es lo que sigifica esto? Significa que en el dominio de la frecuencia se ven picos en f = +- f1, f = +-f2 y f = +-f3. En donde cada pido da el indicador de la presencia de una de las sinusoides originales y su respectiva amplitud, lo cual permite la identificacion de manera clara de los componentes que conforman la señal.

