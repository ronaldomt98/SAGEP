from models.Mueble import Mueble


class Silla(Mueble):
    clave = "silla"

    def get_clave(self):
        return self.clave

    def __init__(self, **kwargs):
        super(Silla, self).__init__(**kwargs)
