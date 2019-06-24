from Bdatos import Bdatos
from view.View import View

class Controller():

    def __init__(self):
        model = Bdatos()
        view = View()

    def agregar_mueble(self,mueble):
        self.model.fabricar_mueble(mueble)

    def buscar_por_cedula(self,ci):
        respuesta = self.model.obtener_clientes(ci)
        return respuesta

    def agregar_cliente(self, cliente):
        self.model.guardar_cliente(cliente)

    def listar_clientes(self):
        listaDeClientes = self.model.
        self.view.vistaListarClientes(listaDeClientes)
        return listaDeClientes

    def devolver_mueble(self,ci):
        cliente = self.buscar_por_cedula(self,ci)
        cliente.muebles = None
        self.eliminar_cliente(self,ci)
        self.agregar_cliente(self,ci,cliente)


    def vender(self,mueble, cliente):
        mueble.vender(cliente)

    def agregar_empleado(self, ci, empleado):
        self.model.guardar_empleado(ci,empleado)

    def eliminar_cliente(self,ci):
        Controller.eliminar_cliente(ci)