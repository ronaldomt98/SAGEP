from models.Mueble import Mueble


class Taburete(Mueble):
    clave = "taburete"
    precio = 30000

    def __init__(self):
        super().__init__()

    def vender(self, cliente):
        self.cliente = cliente

    def devolver(self, cliente):
        self.cliente = None

    @classmethod
    def get_clave(self):
        return self.clave

    def costo(self):
        return self.__precio

    def __str__(self):
        return super().__str__()
