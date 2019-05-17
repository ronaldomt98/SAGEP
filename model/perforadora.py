from model.maquina import Maquina

# ...................................CLASE PERFORADORA..........................................
'''CLASE QUE HEREDA DE MAQUINA'''


class Perforadora(Maquina):
    clave = "perforadora"

    def getClave(self):
        return self.clave

    def __init__(self):
        pass

    def perforar(self):
        pass