import transaction
from models.Cliente import Cliente
from models.Empleado import Empleado
from models.Mueble import Mueble
from Stock import Stock
from MiZODB import MiZODB
from Venta import Venta

db = MiZODB('./Data')
dbroot = db.root
"""CLASE ENCARGADA DE PERSISTIR LOS OBJETOS Y HACER LAS MODIFICACIONES DEL NEGOCIO Y 
LAS DEVOLUCIONES QUE SE HACEN DESDE EL CONTROLADOR"""


def inicializar_stock():
    '''
    1 - armario
    2 - cama
    3 - comoda
    4 - escritorio
    5 - estanteria
    6 - mesa
    7 - silla
    8 - taburete
    9 - vitrina
    '''
    stock1 = Stock()
    stock1.cantidad=10
    stock1.nombre= 'armario'
    stock2 = Stock()
    stock2.cantidad = 11
    stock2.nombre= 'cama'
    stock3 = Stock()
    stock3.cantidad = 12
    stock3.nombre= 'comoda'
    stock4 = Stock()
    stock4.cantidad = 13
    stock4.nombre= 'escritorio'
    stock5 = Stock()
    stock5.cantidad = 14
    stock5.nombre= 'estanteria'
    stock6 = Stock()
    stock6.cantidad = 15
    stock6.nombre= 'mesa'
    stock7 = Stock()
    stock7.cantidad = 16
    stock7.nombre= 'silla'
    stock8 = Stock()
    stock8.cantidad = 17
    stock8.nombre= 'taburete'
    stock9 = Stock()
    stock9.cantidad = 18
    stock9.nombre= 'vitrina'

    dbroot[1] = stock1
    dbroot[2] = stock2
    dbroot[3] = stock3
    dbroot[4] = stock4
    dbroot[5] = stock5
    dbroot[6] = stock6
    dbroot[7] = stock7
    dbroot[8] = stock8
    dbroot[9] = stock9
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

def obtener_stock(clave):
    try:
        stock = dbroot[clave]
        return stock
    except ValueError:
        return None

def devolver(ci, clave, cantidad):
    try:
        guardar_mueble(clave,cantidad)
        venta = dbroot[ci]
        venta.revertida = True
        dbroot[ci] = venta
        transaction.commit()
        return True
    except ValueError:
        return False


def guardar_mueble(clave, cantidad):
    try:
        stock = Stock()
        stock = dbroot[clave]
        stock.cantidad = stock.cantidad +cantidad
        dbroot[clave] = stock
        transaction.commit()
        return True
    except ValueError:
        return False


def modificar_venta(ci,clave,valor):
    try:
        stock = Stock()
        stock = dbroot[clave]
        if valor > stock.cantidad:
            return False
        stock.cantidad = stock.cantidad - valor
        venta = Venta()
        venta.cantidad = valor
        venta.ci = ci
        venta.mueble = clave
        dbroot[ci] = venta
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

def obtener_ventas():
    ventas = []
    for key in dbroot.keys():
        obj = dbroot[key]
        if isinstance(obj, Venta):
            if (not obj.revertida):
                ventas.append(obj)
    return ventas

def obtener_devoluciones():
    devoluciones = []
    for key in dbroot.keys():
        obj = dbroot[key]
        if isinstance(obj, Venta):
            if (obj.revertida):
                devoluciones.append(obj)
    return devoluciones
