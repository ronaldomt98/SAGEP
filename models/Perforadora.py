from .Maquina import Maquina


class Perforadora(Maquina):
    clave = "perforadora"

    def get_clave(self):
        return self.clave

    def __init__(self):
        super(Perforadora, self).__init__()
        pass

    def perforar(self):
        pass
