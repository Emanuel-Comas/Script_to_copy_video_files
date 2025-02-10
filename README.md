### Importacion de librerias necesarias.

-- os : Para interactuar con el sistema.
-- shutil : Para copiar archivos y directorios.

![importaciones](image.png)


### Definición de función para copiar los archivos de video.

-- La funcion copia todos los 'archivos de video' que encuentre en el directorio origen, 
al directorio destino.

![funcion](image-1.png)


### Comprobación de existencia de directorios.

-- Se comprueba si existe la ruta del directorio origen ingresada.
![verifica](image-1.png)



-- Se comprueba si existe la ruta del directorio destino ingresada, si no existe se crea.
![verifica2](image-3.png)



### Obtención de los archivos dentro del directorio origen.

Obtención de todos los archivos dentro del directorio origen:

![archivos](image-4.png)

Definicion de una tupla de extensiónes de archivos de video comunes.

![extensiones](image-5.png)



### Iteración

-- Se itera sobre cada archivo.
-- Obteniendo la ruta completa del archivo en el directorio origen.
![for](image-6.png)


ej: 'video1.mp4' es la parte que va a variar todo el tiempo.
![alt text](image-7.png)



-- Se comprueba si es un archivo y no un subdirectorio.
![alt text](image-8.png)


-- Se comprueba si el archivo tiene una extensión de video válida.
![alt text](image-9.png)



-- Si es un archivo de video valido, se copia al directorio destino

![alt text](image-10.png)



### Manejo de excepciones.

![alt text](image-11.png)

-- Copia el 'archivo' del directorio origen al directorio destino.
![alt text](image-12.png)


-- En caso de haber un error, se vizualiza la excepcion.


### Finalmente.

-- Se ejecuta la funcion del script.
![ejecucion](image-13.png)
![alt text](image-14.png)
![alt text](image-15.png)