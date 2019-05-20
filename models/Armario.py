from .Model import Mueble

class Armario(Mueble):

    clave = "armario"

    def get_clave(self):
        return self.clave

    def __init__(self):
        super(Armario, self).__init__()
