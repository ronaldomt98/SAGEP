from mizodb import MiZODB, transaction
from models.Mueble import Mueble
from models.Cliente import Cliente
from models.Empleado import Empleado

db = MiZODB('./Data')
dbroot = db.raiz
"""CLASE ENCARGADA DE PERSISTIR LOS OBJETOS Y HACER LAS MODIFICACIONES DEL NEGOCIO Y 
LAS DEVOLUCIONES QUE SE HACEN DESDE EL CONTROLADOR"""


def inicializar_stock():
    dbroot['armario'] = 0
    dbroot['escritorio'] = 0
    dbroot['taburete'] = 0
    dbroot['estanteria'] = 0
    dbroot['silla'] = 0
    dbroot['vitrina'] = 0
    dbroot['cama'] = 0
    dbroot['mesa'] = 0
    dbroot['comoda'] = 0


def registrar(clave, valor):
    dbroot[clave] = valor


def obtener(clave):
    """para retornar un objeto segun la clave que se le pasa"""
    try:
        if dbroot[clave] is not None:
            return dbroot[clave]
        else:
            raise KeyError
    except KeyError:
        print('CLIERNTE NO ENCONTRADO \nVERIFICAR LA C.I.: ', clave)


def vender_mueble(clave, cantidad):
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