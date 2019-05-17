from model.maquina import Maquina

# ...................................CLASE CEPILLADORA..........................................
'''CLASE QUE HEREDA DE MAQUINA'''


class Prensa(Maquina):
    clave = "cepilladora"

    def getClave(self):
        return self.clave

    def __init__(self):
        pass

    def pulir_superficie(self):
        pass