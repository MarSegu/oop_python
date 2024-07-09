from pythonExercises.catalogo_peliculas_archivos.dominio.Pelicula import Pelicula
from pythonExercises.catalogo_peliculas_archivos.servicio.CatalogoPeliculas import CatalogoPeliculas

print('Bienvenido al menu'.center(50, '-'))

print('1. Agregar Pelicula')
print('2. Listar peliculas')
print('3. Eliminar archivo de peliculas')
print('4. Salir')

menu_opcion = int(input('Opcion a Escoger: '))

catalogo = CatalogoPeliculas()

if menu_opcion == 1:
    pelicula = input('Nueva pelicula: ')
    objeto_pelicula = Pelicula(pelicula)
    catalogo.agregar_pelicula(objeto_pelicula)
elif menu_opcion == 2:
    catalogo.listar_peliculas()
elif menu_opcion == 3:
    catalogo.eliminar()
elif menu_opcion == 4:
    pass
else:
    print(f'Opcion no valida: {menu_opcion}')

print('Fin de la aplicacion'.center(50, '-'))