import os
import shutil


def copiarVideos(origen, destino):


    if not os.path.exists(origen):
        print(f'La ruta origen: {origen} no existe.')
        


    if not os.path.exists(destino):
        print(f'La ruta destino: {destino} no existe.')
        os.makedirs(destino)


    archivos = os.listdir(origen)

    extensiones_video = ('.mp4', '.mkv','.avi','.mov','.flv','.wmv',)

    for archivo in archivos:
        archivo_origen = os.path.join(origen, archivo)

        if os.path.isfile(archivo_origen):
            
            if archivo.lower().endswith(extensiones_video):
                archivo_destino = os.path.join(destino, archivo)


                try:
                    shutil.copy(archivo_origen, archivo_destino)
                    print(f'Archivo {archivo} copiado a {destino}.')

                except Exception as e:
                    print(f'Error al copiar el archivo {archivo}: {e}')



if __name__ == '__main__':

    directorio_origen = input('Ingrese el directorio origen donde estan los archivos a copiar: ')
    directorio_destino = input('Ingrese el directorio destino, donde se copiaran los archivos: ')

    copiarVideos(directorio_origen, directorio_destino)



