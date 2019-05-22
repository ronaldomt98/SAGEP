from models.Mueble import Mueble


class Mesa(Mueble):
    clave = "mesa"

    def get_clave(self):
        return self.clave

    def __init__(self, **kwargs):
        super(Mesa, self).__init__(**kwargs)
