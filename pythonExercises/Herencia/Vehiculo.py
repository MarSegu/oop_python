class Vehiculo:
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas

    def __str__(self):
        return f'[Vehiculo: Color: {self._color}, Ruedas: {self._ruedas}]'

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def ruedas(self):
        return self._ruedas

    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas

class Coche(Vehiculo):
    def __init__(self, velocidad, color, ruedas):
        self._velocidad = velocidad
        super().__init__(color, ruedas)

    def __str__(self):
        return f'{super().__str__()} [Coche: Velocidad: {self._velocidad}]'

class Bicicleta(Vehiculo):
    def __init__(self, tipo, color, ruedas):
        self._tipo = tipo
        super().__init__(color, ruedas)

    def __str__(self):
        return f'{super().__str__()} [Bicicleta: Tipo: {self._tipo}]'

bicicleta1 = Bicicleta('montania', 'rojo', 2)
print(bicicleta1)

coche1 = Coche(120, 'negro', 4)
print(coche1)