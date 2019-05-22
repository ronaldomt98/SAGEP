from models.Mueble import Mueble


class Armario(Mueble):
    clave = "armario"

    def get_clave(self):
        return self.clave

    def __init__(self, **kwargs):
        super(Armario, self).__init__(**kwargs)
