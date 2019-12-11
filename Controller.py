from Bdatos import obtener_cliente, guardar_cliente, obtener_clientes, actualizar_cliente\
    , devolver, guardar_empleado, obtener_empleados, obtener_stock, guardar_mueble\
    , modificar_venta

def agregar_mueble(mueble, cantidad):
    guardar_mueble(mueble, cantidad)

def buscar_por_cedula(ci):
    respuesta = obtener_cliente(ci)
    return respuesta

def agregar_cliente(ci,cliente):
    guardar_cliente(ci,cliente)

def agregar_empleado(ci, empleado):
    guardar_empleado(ci,empleado)

def listar_clientes():
    listaClientes = obtener_clientes()
    return listaClientes

def listar_empleados():
    listaEmpleados = obtener_empleados()
    return listaEmpleados

def listar_stock(clave):
    listaStock = obtener_stock(clave)
    return listaStock

def devolver_mueble(ci, clave, cantidad):
    '''
    cliente = obtener_cliente(ci)
    cliente.muebles.cantidad -= cantidad
    actualizar_cliente(ci,cliente)
    '''
    devolver(ci, clave, cantidad)

'''
def agregar_venta(mueble, cliente, cantidad):
    mueble.vender(cliente, cantidad)
'''
def agregar_venta(ci,mueble, cantidad):
    modificar_venta(ci,mueble, cantidad)

def agregar_empleado(ci, empleado):
    guardar_empleado(ci, empleado)

