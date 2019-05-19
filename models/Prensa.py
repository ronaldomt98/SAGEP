from models.Maquina import Maquina

class Prensa(Maquina):
    clave = "prensa"

    def getClave(self):
        return self.clave

    def __init__(self):
        pass

    def presionar(self):
        pass