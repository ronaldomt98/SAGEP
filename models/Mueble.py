from models.Vendible import Vendible
from abc import ABCMeta, abstractmethod

class Mueble(Vendible):

    def __init__(self, precio, cantidad):
        super().__init__(precio, cantidad)

    def vender(self, cantidad):
        self.vender(cantidad)

    def comprar(self, cantidad):
        self.comprar(cantidad)

    def devolver(self, bien, cantidad):
        self.devolver(cantidad)

    def obtener_precio(self):
        return self.precio

    def obtener_cantidad(self):
        return self.cantidad

    def __str__(self):
        return ('\nPrecio: ' + self.precio)
