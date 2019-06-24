from abc import ABC


class Contacto(ABC):

    def __init__(self,tipo_contacto,descripcion):
        self.tipo_contacto = tipo_contacto
        self.descripcion = descripcion

    def obtener_tipo_contacto(self):
        return self.tipo_contacto

    def obtener_descripcion(self):
        return self.descripcion