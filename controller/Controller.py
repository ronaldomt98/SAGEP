from Bdatos import obtener_clientes

class Controller():

    def __init__(self):
        pass

    def agregar_mueble(self,mueble):
        self.model.fabricar_mueble(mueble)

    def buscar_por_cedula(self,ci):
        respuesta = self.model.obtener_clientes(ci)
        return respuesta

    def agregar_cliente(self, ci, cliente):
        self.model.guardar_cliente(ci,cliente)

    def listar_clientes(self):
        return obtener_clientes()

    def devolver_mueble(self,ci):
        pass

    def vender(self,mueble,cliente):
        mueble = self.view.vender
        mueble.vender(cliente)

    def agregar_empleado(self, ci, empleado):
        self.model.guardar_empleado(ci,empleado)