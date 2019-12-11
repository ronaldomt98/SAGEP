from models.Mueble import Mueble
from Bdatos import modificar_venta, modificar_compra

class Armario(Mueble):
    clave = 1
    precio = 100000

    def __init__(self,cantidad):
        super().__init__(cantidad)

    def vender(self, cantidad):
        try:
            if modificar_venta(self.clave, cantidad) == False:
                return False
            else:
                return True
        except ValueError:
            return False

    def comprar(self, cantidad):
        try:
            if modificar_compra(self.clave, cantidad) == False:
                return False
            return True
        except ValueError:
            return False

    def devolver(self, cantidad):
        try:
            if modificar_compra(self.clave, cantidad) == False:
                return False
            return True
        except ValueError:
            return False

    def get_clave(self):
        return self.clave

    def costo(self):
        return self.__precio

    def __str__(self):
        return (super().__str__())

    def __str__(self):
        return (super().__str__())
