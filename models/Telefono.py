from models.Contacto import Contacto

class Telefono(Contacto):
    clave = "contacto"

    def getClave(self):
        return self.clave

    def __init__(self, numero):
        self.numero = numero