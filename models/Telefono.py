from .Contacto import Contacto


class Telefono(Contacto):
    clave = "contacto"

    def get_clave(self):
        return self.clave

    def __init__(self, numero):
        super(Telefono, self).__init__()
        self.numero = numero
