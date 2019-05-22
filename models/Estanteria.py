from models.Mueble import Mueble


class Estanteria(Mueble):
    clave = "estanteria"

    def get_clave(self):
        return self.clave

    def __init__(self, **kwargs):
        super(Estanteria, self).__init__(**kwargs)
