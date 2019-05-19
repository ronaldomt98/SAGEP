from .Maquina import Maquina


class SierraCircular(Maquina):
    clave = "sierra_circular"

    def get_clave(self):
        return self.clave

    def __init__(self):
        super(SierraCircular, self).__init__()
        pass

    def cortar(self):
        pass
