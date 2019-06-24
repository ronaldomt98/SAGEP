from models.Contacto import Contacto
from persistent import Persistent


class Telefono(Contacto, Persistent):
    clave = "telefono"

    def get_clave(self):
        return self.clave

    def __init__(self, numero):
        super().__init__()
        self.numero = numero
