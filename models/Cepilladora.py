from .Maquina import Maquina


class Prensa(Maquina):
    clave = "cepilladora"

    def get_clave(self):
        return self.clave

    def __init__(self):
        super(Prensa, self).__init__()
        pass

    def pulir_superficie(self):
        pass
