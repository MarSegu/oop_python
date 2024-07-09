import os

from pythonExercises.catalogo_peliculas_archivos.dominio.Pelicula import Pelicula


class CatalogoPeliculas:
    ruta_archivo = './peliculas'

    def __init__(self):
        pass

    def agregar_pelicula(self, pelicula):
        with open(self.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(pelicula.nombre + '\n')

        with open(self.ruta_archivo, 'r', encoding='utf8') as archivo:
            print(archivo.read())

    def listar_peliculas(self):
        with open(self.ruta_archivo, 'r', encoding='utf8') as archivo:
            print(archivo.read())

    def eliminar(self):
        os.remove(self.ruta_archivo)
        print('El archivo ha sido eliminado')

