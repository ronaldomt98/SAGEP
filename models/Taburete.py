from models.Mueble import Mueble


class Taburete(Mueble):
    clave = "taburete"

    def get_clave(self):
        return self.clave

    def __init__(self, **kwargs):
        super(Taburete, self).__init__(**kwargs)
