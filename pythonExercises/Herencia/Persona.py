class Persona:

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return f'Persona: [Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}]'

class Empleado(Persona):
    def __init__(self, sueldo, nombre, apellido, edad):
        super().__init__(nombre, apellido, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()} [Empleado: Sueldo: {self.sueldo}]'

if __name__ == '__main__':
    Empleado1 = Empleado(5000, 'mario', 'Segura', 26)
    print(Empleado1.nombre)


