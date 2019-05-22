from models.Mueble import Mueble


class Cama(Mueble):
    clave = "cama"

    def get_clave(self):
        return self.clave

    def __init__(self, **kwargs):
        super(Cama, self).__init__(**kwargs)
