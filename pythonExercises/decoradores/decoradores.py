"""
Decoradores
Un decorador es una funcion que recibe una funcion y regresa otra
lo utilizamos para extender funcionalidad
1. funcion decorador (a)
2. funcion a decorar (b)
3. funcion decorada (c)
"""

def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c(*args, **kwargs):
        print("Antes de ejecutar la funcion")
        resultado = funcion_a_decorar_b(*args, **kwargs)
        print("Despues de ejecutar la funcion")
        return resultado

    return funcion_decorada_c

#Definimos una funcion y vamos a extender su funcionalidad con un decorador
@funcion_decorador_a
def sumar(a, b):
    print(a + b)
    return a + b

resultado = sumar(5, 6)
#print(resultado)


"""
@funcion_decorador_a
def mostrar_mensaje():
    print('Hola desde funcion mostrar_mensaje')

@funcion_decorador_a
def imprimir():
    print('Hola desde funcion imprimir')

mostrar_mensaje()
imprimir()
"""