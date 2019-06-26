from models.Persona import Persona
from persistent import Persistent


class Empleado(Persona, Persistent):
    muebles = []
    clave = "empleado"

    def get_clave(self):
        return self.clave

    def __init__(self, cargo, salario, muebles = None, **kwargs):
        super().__init__(**kwargs)
        self.cargo = cargo
        self.salario = salario
        self.muebles = muebles

    def obtener_cargo(self):
        return self.cargo

    def obtener_salario(self):
        return self.salario

    def obtener_muebles(self):
        return self.muebles

    def vender(self, bien, cantidad):
        pass

    def __str__(self):
        return Persona().__str__() + '\nCargo: ' + self.cargo + '\nMuebles:\n' + str(self.muebles)
