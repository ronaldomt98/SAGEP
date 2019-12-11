from models.Persona import Persona
from persistent import Persistent


class Empleado(Persona, Persistent):
    clave = "empleado"

    def get_clave(self):
        return self.clave

    def __init__(self,nombre, apellido, cedula, direccion, contactos, cargo, salario):
        super().__init__(nombre, apellido, cedula, direccion, contactos)
        self.cargo = cargo
        self.salario = salario

    def obtener_cargo(self):
        return self.cargo

    def obtener_salario(self):
        return self.salario

    def vender(self, bien, cantidad):
        pass

    def __str__(self):
        return super().__str__() + '\nCargo: ' + self.cargo + self.salario
