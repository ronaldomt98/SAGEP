import transaction
from models.Cliente import Cliente
from models.Empleado import Empleado
from models.Mueble import Mueble

from MiZODB import MiZODB

db = MiZODB('./Data')
dbroot = db.root
"""CLASE ENCARGADA DE PERSISTIR LOS OBJETOS Y HACER LAS MODIFICACIONES DEL NEGOCIO Y 
LAS DEVOLUCIONES QUE SE HACEN DESDE EL CONTROLADOR"""


def inicializar_stock():
    dbroot['armario'] = 2
    dbroot['escritorio'] = 3
    dbroot['taburete'] = 2
    dbroot['estanteria'] = 3
    dbroot['silla'] = 2
    dbroot['vitrina'] = 3
    dbroot['cama'] = 2
    dbroot['mesa'] = 3
    dbroot['comoda'] = 1


def guardar_cliente(clave, valor):
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


def vender(clave, cantidad):
    try:
        dbroot[clave] -= cantidad
        transaction.commit()
        return True
    except ValueError:
        return False


def fabricar_mueble(clave, cantidad):
    try:
        dbroot[clave] += cantidad
        transaction.commit()
        return True
    except ValueError:
        return False


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


def devolver(clave,cantidad):
    try:
        dbroot[clave]+=cantidad
        transaction.commit()
        return True
    except ValueError:
        return False

