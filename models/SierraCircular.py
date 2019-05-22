from models.Maquina import Maquina
from persistent import Persistent


class SierraCircular(Maquina, Persistent):
    clave = "sierra_circular"

    def get_clave(self):
        return self.clave

    def __init__(self):
        super(SierraCircular, self).__init__()
        pass

    def cortar(self):
        pass
