from Bdatos import obtener_cliente, guardar_cliente, obtener_clientes, actualizar_cliente\
    , devolver, guardar_empleado, obtener_empleados, obtener_stock
from view.ViewTk import ViewTk

view = ViewTk()

class Controller:

    def agregar_mueble(self,mueble):
        self.fabricar_mueble(mueble)

    def buscar_por_cedula(self,ci):
        respuesta = obtener_cliente(ci)
        view.vista_mostrar_cliente(respuesta)

    def agregar_cliente(self, cliente):
        guardar_cliente(cliente)

    def listar_clientes(self):
        listaClientes = obtener_clientes()
        view.vista_listar_clientes(listaClientes)

    def listar_empleados(self):
        listaEmpleados = obtener_empleados()
        view.vista_listar_empleados(listaEmpleados)

    def listar_stock(self):
        listaStock = obtener_stock()
        view.vista_mostrar_muebles(listaStock)

    def devolver_mueble(self,ci,clave,cantidad):
        cliente = obtener_cliente(ci)
        cliente.muebles.cantidad -= cantidad
        actualizar_cliente(ci,cliente)
        devolver(clave, cantidad)


    def vender(self,mueble, cliente):
        mueble.vender(cliente)

    def agregar_empleado(self, ci, empleado):
        guardar_empleado(ci,empleado)
