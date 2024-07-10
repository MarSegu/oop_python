"""
Funciones lambda
son funciones anonimas y son pequenias (una sola linea de codigo)

No es posible asignar una funcion a una variable
mi_funcion = def sumar(a,b): return a+b

Con una funcion lambda(anonima, sin nombre, y una sola linea de codigo)
No se necesita agregar parentesis para los parametros
No se necesita usar la palabra return, pero si se debe regresar una expresion
"""

mi_funcion_lambda = lambda a, b: a + b

resultado = mi_funcion_lambda(1, 5)
print(resultado)

"""
FUncion lambda que no recibe argumentos
"""
mi_funcion_lambda = lambda:'Funcion sin argumentos'
print(mi_funcion_lambda())

# Función lambda con parámetros por default
mi_funcion_lambda = lambda a=2, b=3: a + b
print(f'Resultado argumentos por default: {mi_funcion_lambda()}')

# Función lambda con argumentos variables *args y **kwargs
mi_funcion_lambda = lambda *args, **kwargs: len(args) + len(kwargs)
print(f'Resultado argumentos variables: {mi_funcion_lambda(1,2,3, a=5,b=6)}')

# Funciones lambda con argumentos, argumentos variables y valores por default
mi_funcion_lambda = lambda a, b, c=3, *args, **kwargs: a+b+c+len(args)+len(kwargs)
print(f'Resultado función lambda: {mi_funcion_lambda(1,2,4, 5,6,7,e=5,f=7)}')