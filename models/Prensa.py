from .Maquina import Maquina


class Prensa(Maquina):
    clave = "prensa"

    def get_clave(self):
        return self.clave

    def __init__(self):
        super(Prensa, self).__init__()
        pass

    def presionar(self):
        pass
