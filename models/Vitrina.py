from models.Mueble import Mueble


class Vitrina(Mueble):
    clave = "vitrina"

    def get_clave(self):
        return self.clave

    def __init__(self, **kwargs):
        super(Vitrina, self).__init__(**kwargs)
