import transaction
from models.Cliente import Cliente
from models.Empleado import Empleado
from models.Mueble import Mueble
from Stock import Stock
from MiZODB import MiZODB

db = MiZODB('./Data')
dbroot = db.root
"""CLASE ENCARGADA DE PERSISTIR LOS OBJETOS Y HACER LAS MODIFICACIONES DEL NEGOCIO Y 
LAS DEVOLUCIONES QUE SE HACEN DESDE EL CONTROLADOR"""


def inicializar_stock():
    dbroot['armario'] = 10
    dbroot['cama'] = 10
    dbroot['comoda'] = 10
    dbroot['escritorio'] = 10
    dbroot['estanteria'] = 10
    dbroot['mesa'] = 10
    dbroot['silla'] = 10
    dbroot['taburete'] = 10
    dbroot['vitrina'] = 10
    transaction.commit()

def guardar_cliente(clave, valor):
    dbroot[clave] = valor
    transaction.commit()

def actualizar_cliente(clave,valor):
    dbroot[clave] = valor
    transaction.commit()


def guardar_empleado(clave, valor):
    dbroot[clave] = valor
    transaction.commit()


def obtener_cliente(clave):
    """para retornar un cliente segun la clave(CI) que se le pasa"""
    try:
        if (dbroot[clave] != None):
            return dbroot[clave]
        else:
            raise (KeyError)
    except KeyError:
        print('CLIERNTE NO ENCONTRADO \nVERIFICAR LA C.I.: ', clave)


def obtener_empleado(clave):
    """para retornar un empleado segun la clave(CI) que se le pasa"""
    try:
        if (dbroot[clave] != None):
            return dbroot[clave]
        else:
            raise (KeyError)
    except KeyError:
        print('EMPLEADO NO ENCONTRADO \nVERIFICAR LA C.I.: ', clave)


def cobrar(clave, monto):
    try:
        dbroot[clave] += monto
        transaction.commit()
        return True
    except ValueError:
        return False


def obtener_ventas():
    muebles = []
    for key in dbroot.keys():
        obj = dbroot[key]
        if isinstance(obj, Mueble):
            mueble = obj
            if mueble.cliente is not None:
                muebles.append(mueble)
    return muebles


def obtener_clientes():
    clientes = []
    for key in dbroot.keys():
        obj = dbroot[key]
        if isinstance(obj, Cliente):
            clientes.append(obj)
    return clientes


def obtener_empleados():
    empleados = []
    for key in dbroot.keys():
        obj = dbroot[key]
        if isinstance(obj, Empleado):
            empleados.append(obj)
    return empleados

def obtener_stock():
    stock = []
#    stock.append(dbroot['armario'])
#    stock.append(dbroot['cama'])
#    stock.append(dbroot['comoda'])
#    stock.append(dbroot['escritorio'])
#    stock.append(dbroot['estanteria'])
#    stock.append(dbroot['mesa'])
#    stock.append(dbroot['silla'])
#    stock.append(dbroot['taburete'])
#    stock.append(dbroot['vitrina'])
    for key in dbroot.keys():
        obj = dbroot[key]
        if isinstance(obj, Mueble):
            stock.append(obj)
    return stock

def devolver(clave, cantidad):
    try:
        stock = Stock()
        stock = dbroot[clave]
        stock.cantidad = stock.cantidad +cantidad
        transaction.commit()
        return True
    except ValueError:
        return False


def agregar_mueble(clave, cantidad):
    try:
        stock = Stock()
        stock = dbroot[clave]
        stock.cantidad = stock.cantidad +cantidad
        dbroot[clave] += cantidad
        transaction.commit()
        return True
    except ValueError:
        return False


def modificar_venta(clave,valor):
    try:
        stock = Stock()
        stock = dbroot[clave]
        if valor > stock.cantidad:
            return False
        stock.cantidad = stock.cantidad - valor
        transaction.commit()
        return True
    except ValueError:
        return False

def modificar_compra(clave,valor):
    try:
        stock=Stock()
        stock = dbroot[clave]
        stock.cantidad = stock.cantidad + valor
        transaction.commit()
        return True
    except ValueError:
        return False