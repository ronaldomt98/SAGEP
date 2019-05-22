from models.Maquina import Maquina
from persistent import Persistent


class Prensa(Maquina, Persistent):
    clave = "prensa"

    def get_clave(self):
        return self.clave

    def __init__(self):
        super(Prensa, self).__init__()
        pass

    def presionar(self):
        pass
