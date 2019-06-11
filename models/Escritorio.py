from models.Mueble import Mueble


class Escritorio(Mueble):
    clave = "escritorio"

    def get_clave(self):
        return self.clave

    def __init__(self, **kwargs):
        super(Escritorio, self).__init__(**kwargs)