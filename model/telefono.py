from model.contacto import Contacto

# ...................................CLASE TELEFONO..........................................
'''CLASE QUE HEREDA DE CONTACTO'''


class Telefono(Contacto):
    clave = "contacto"

    def getClave(self):
        return self.clave

    def __init__(self, numero):
        self.numero = numero