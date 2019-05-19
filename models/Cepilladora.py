from models.Maquina import Maquina

class Prensa(Maquina):

    clave = "cepilladora"
    def getClave(self):
        return self.clave

    def __init__(self):
        pass

    def pulir_superficie(self):
        pass