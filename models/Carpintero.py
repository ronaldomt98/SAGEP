from persistent import Persistent
from models.Persona import Persona
from Bdatos import agregar_mueble

'''CLASE QUE HEREDA DE Persona'''
class Carpintero(Persona,Persistent):
    clave = "carpintero"

    def get_clave(self):
        return self.clave

    def __init__(self, empleado):
        self.empleado = empleado

    def fabricar_mueble(self, clave, cantidad):
        try:
            if agregar_mueble(self.clave, cantidad) == False:
                return False
            else:
                return True
        except ValueError:
            return False

    def __str__(self):
        return str(self.empleado)
