from pythonExercises.Polimorfismo.Empleado import Empleado
from pythonExercises.Polimorfismo.Gerente import Gerente


def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado('Carlos', 5000)
imprimir_detalles(empleado)

gerente = Gerente('Karla', 6000, 'Sistemas')
imprimir_detalles(gerente)
