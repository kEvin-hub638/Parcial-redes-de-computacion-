# Preguntas  
## 1. ¿Cómo contribuye la Transformada de Fourier al análisis de señales en la capa física?  

La **Transformada de Fourier** es una herramienta fundamental para el análisis de señales en la **capa física**, ya que permite cambiar la perspectiva en la que se observan. En lugar de ver cómo varían en el tiempo, nos muestra las **frecuencias** que la componen. Esto es clave en redes de comunicación, pues las señales pueden verse afectadas por **ruido, interferencias o pérdidas de datos**, y mediante esta transformación es posible detectar y corregir esos problemas.  

Dos aplicaciones importantes de la **Transformada de Fourier** en el análisis de señales son:  

- **Filtrado de señales:** Facilita la separación de las **frecuencias útiles** de aquellas que generan interferencias, mejorando la calidad de la transmisión.  
- **Optimización del ancho de banda:** Permite analizar el espectro de la señal para identificar qué **frecuencias están en uso** y cuáles pueden aprovecharse mejor en la comunicación de datos.  


## 2. Señales compuestas y espectro de frecuencias

Si la señal que se esta trasmitiendo es periódica y está compuesta por la suma de tres sinusoides de diferentes frecuencias de f1, f2 y f3. La señal de este tiempo se puede expresar de la siguiente manera:

![Imagen 1](https://github.com/ALMA3112/Parcial-redes-de-computacion-/blob/main/Imagenes/Imagen1.jpg)

en  donde  A1, A2 Y A3 son las amplitudes que le correponden a cada sinusoide.
Cuando se aplica la Transformcada de Fourier a x(t), se esta transformando la señal del domino del tiempo al dominio de la frecuencia. El resultado es una representacion la cual muestra las constribuciones de cada frecuencia. Esto matematicamente se ve la transformada de faourier de una sinusoide se expresa mediante funciones delta de Dirac, para este caso en especifico, la Transformada de Fourier X(f) de x(t) es:

![Imagen 2](https://github.com/ALMA3112/Parcial-redes-de-computacion-/blob/main/Imagenes/Imagen2.jpg)

¿Que es lo que sigifica esto? Significa que en el dominio de la frecuencia se ven picos en f = +- f1, f = +-f2 y f = +-f3. En donde cada pido da el indicador de la presencia de una de las sinusoides originales y su respectiva amplitud, lo cual permite la identificacion de manera clara de los componentes que conforman la señal.

