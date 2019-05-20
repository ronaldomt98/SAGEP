from abc import ABC
from .Vendible import Vendible
from .Model import Model


class Mueble(ABC, Vendible, Model):

    def __init__(self, precio, imagen, fecha_venta, cliente):
        self.precio = precio
        self.imagen = imagen
        self.fecha_venta = fecha_venta
        self.cliente = cliente

    def aplicar_descuento(self):
        pass

    def vender(self, cliente):
        pass

    def __str__(self):
        return '\nPrecio: ' + self.precio + '\nFecha_venta: ' + self.fecha_venta
        + '\nCliente: ' + str(self.cliente)
