from models.Maquina import Maquina
from persistent import Persistent

class Perforadora(Maquina, Persistent):
    clave = "perforadora"

    def get_clave(self):
        return self.clave

    def __init__(self):
        super(Perforadora, self).__init__()
        pass

    def perforar(self):
        pass
