from models.Mueble import Mueble


class Comoda(Mueble):
    clave = "comoda"

    def get_clave(self):
        return self.clave

    def __init__(self, **kwargs):
        super(Comoda, self).__init__(**kwargs)
