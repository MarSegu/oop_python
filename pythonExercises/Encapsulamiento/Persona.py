class Persona:
    """
    guion bajo antes de una variable indica que no se debe editar fuera de la variable pero aun se puede
    dos guion bajo, no permite editar el valor de la variable
    @property annotation for get
    @variable_name.setter for set
    """
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad} ')

    #metodo destructor
    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido}')


if __name__ == '__main__':
    persona1 = Persona('Juan', 'Perez', 28)
    print(persona1.nombre)
    persona1.nombre = "Mario"
    print(f'{persona1.nombre} {persona1.apellido }')

    print(__name__)