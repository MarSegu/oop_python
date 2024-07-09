class PersonaArgs:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores}  {self.terminos}')


persona1 = PersonaArgs('Juan', 'Perez', 28, '687687867',2,3,5, m='manzana', p='pera')

persona1.edad = 35
PersonaArgs.mostrar_detalle(persona1)


persona2 = PersonaArgs('Karla', 'Gomez', 30)
#print(f'Objeto persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')
#print(f'Objeto persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')

persona1.mostrar_detalle()
