from persistent import Persistent
from models.Persona import Persona

class Cliente(Persona, Persistent):
    clave = "cliente"

    def get_clave(self):
        return self.clave

    def __init__(self, nombre, apellido, cedula, direccion, ruc = 'ninguno', muebles = None):
        super().__init__(nombre, apellido, cedula, direccion)
        self.ruc = ruc
        self.muebles = muebles

    def obtener_ruc(self):
        return self.ruc

    def obtener_muebles(self):
        return self.muebles

    def comprar(self, bien):
        self.muebles.append(bien)

    def __str__(self):
        return super().__str__() + str(self.muebles) + '\nRUC: ' + self.ruc + '\nMuebles:\n' + str(self.muebles)
