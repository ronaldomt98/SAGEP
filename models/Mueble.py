from models.Vendible import Vendible


class Mueble(Vendible):

    def __init__(self, precio, cantidad, imagen , fecha_venta, cliente):
        super(Mueble, self).__init__()
        self.cantidad = cantidad
        self.precio = precio
        self.imagen = imagen
        self.fecha_venta = fecha_venta
        self.cliente = cliente

    def aplicar_descuento(self):
        pass

    def vender(self, cliente):
        pass

    def __str__(self):
        return ('\nPrecio: ' + self.precio + '\nFecha_venta: ' + self.fecha_venta
                + '\nCliente: ' + str(self.cliente))
