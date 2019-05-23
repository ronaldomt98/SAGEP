import Bdatos
from view import View

class Controller():

    def __init__(self):
        self.model = Bdatos()
        self.view = View()

    def agregar_mueble(self):
        mueble = self.view.vista_agregar_mueble()
        self.model.fabricar_mueble(mueble)

    def buscar_por_cedula(self):
        cedula = self.view.leer_cedula()
        respuesta = self.model.buscar_por_cedula(cedula)
        self.view.imprimir_en_pantalla(respuesta)

    def agregar_cliente(self):
        cliente = self.view.vista_agregar_cliente()
        self.model.registrar(cliente.get_clave(),cliente)

    def listar_clientes(self):
        lista_clientes = self.model.obtener_clientes()
        self.view.vista_listar_clientes(lista_clientes)
        return lista_clientes

    def devolver_mueble(self,mueble):
        pass

    def vender_mueble(self,mueble,cliente):
        mueble = self.view.vender_mueble()
        mueble.vender(cliente)

