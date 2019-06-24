from models.Vendible import Vendible
from abc import ABCMeta, abstractmethod

class Mueble(Vendible):

    __metaclass__ = ABCMeta

    def __init__(self, precio, imagen , fecha_venta, cliente):
        super().__init__()
        self.precio = precio
        self.imagen = imagen
        self.fecha_venta = fecha_venta
        self.cliente = cliente

    def obtener_precio(self):
        return self.precio

    def obtener_imagen(self):
        return self.imagen

    def obtener_fecha_venta(self):
        return self.fecha_venta

    def obtener_cliente(self):
        return self.cliente

    def __str__(self):
        return ('\nPrecio: ' + self.precio + '\nFecha_venta: ' + self.fecha_venta
                + '\nCliente: ' + str(self.cliente))
