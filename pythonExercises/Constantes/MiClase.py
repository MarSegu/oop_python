class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    #decorator that sign this method as static
    #el metodo estatico no recibe la variable self por que 'self' esta relacionada a objetos
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    #metodo de clase
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()

MiClase.metodo_clase()

miObjeto1 = MiClase('variable de instancia')
miObjeto1.metodo_clase()

miObjeto1.metodo_instancia()
