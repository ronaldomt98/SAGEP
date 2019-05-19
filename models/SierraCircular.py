from models.Maquina import Maquina

'''CLASE QUE HEREDA DE MAQUINA'''


class SierraCircular(Maquina):
    clave = "sierra_circular"

    def getClave(self):
        return self.clave

    def __init__(self):
        pass

    def cortar(self):
        pass