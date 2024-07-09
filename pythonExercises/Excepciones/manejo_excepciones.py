from NumerosIdenticosException import NumerosIdenticosException

resultado = None



try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))

    if a==b:
        raise NumerosIdenticosException('Numeros identicos')

    resultado = a/b

except ZeroDivisionError as e:
    print(f'TypeError - Ocurrio un error: {e}, {type(e)}')
except TypeError as e:
    print(f'TypeError - Ocurrio un error: {e}, {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrio un error: {e}, {type(e)}')
else:
    print('No ocurrio ningun error')
finally:
    print('Ejecucion del bloque finally')

print(f'Resultado: {resultado}')
print('Continuamos...')