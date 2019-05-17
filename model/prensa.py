from model.maquina import Maquina

# ...................................CLASE PRENSA..........................................
'''CLASE QUE HEREDA DE MAQUINA'''


class Prensa(Maquina):
    clave = "prensa"

    def getClave(self):
        return self.clave

    def __init__(self):
        pass

    def presionar(self):
        pass