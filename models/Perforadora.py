from models.Maquina import Maquina

class perforadora(Maquina):
    clave = "perforadora"

    def getClave(self):
        return self.clave

    def __init__(self):
        pass

    def perforar(self):
        pass