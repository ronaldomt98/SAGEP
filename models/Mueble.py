from abc import ABC
from models.Vendible import Vendible


class Mueble(ABC, Vendible):

    def __init__(self, precio, imagen, fecha_venta, cliente):
        super.__init__()
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
