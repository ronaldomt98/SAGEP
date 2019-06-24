from persistent import Persistent
from models.Persona import Persona
from models.Mueble import Mueble

'''CLASE QUE HEREDA DE Persona'''
class Carpintero(Persona,Persistent):
    clave = "carpintero"

    def get_clave(self):
        return self.clave

    def __init__(self, empleado):
        self.empleado = empleado

    def fabricar_mueble(self, mueble, cantidad):
        pass

    def __str__(self):
        return str(self.empleado)
