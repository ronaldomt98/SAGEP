from models import Bdatos
from view import View

class MuebleControler:

    def __init__(self):
        self.model = Bdatos()
        self.view = View()

    def agregar_mueble(self):
        mueble = self.view.vista_agregar_mueble()
        self.model.fabricar_mueble(mueble)