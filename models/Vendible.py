from abc import ABCMeta, abstractmethod

class Vendible(object):

    def __init__(self):
        self.precio = 0
        self.codigo = 0
        self.cantidad = 0

    def vender(self, bien, cantidad):
        if bien.vender(bien, cantidad) == False:
            return False
        else:
            return True

    def comprar(self, bien, cantidad):
        if bien.comprar(bien, cantidad) == False:
            return False
        else:
            return True

    def devolver(self, bien, cantidad):
        if bien.devolver(bien, cantidad) == False:
            return False
        else:
            return True
