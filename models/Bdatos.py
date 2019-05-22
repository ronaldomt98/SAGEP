from mizodb import MiZODB, transaction

db = MiZODB('./Data')
dbroot = db.raiz
"""CLASE ENCARGADA DE PERSISTIR LOS OBJETOS Y HACER LAS MODIFICACIONES DEL NEGOCIO Y 
LAS DEVOLUCIONES QUE SE HACEN DESDE EL CONTROLADOR"""
def inicializarStock():
	dbroot['Silla Grande']=1000
	dbroot['Silla Pequena']=400
	dbroot['Mesa Rectangulo']=200
	dbroot['Mesa Redonda']=100
	dbroot['Cubre']=100
	dbroot['Vaso']=200
	dbroot['Plato']=200
	dbroot['Aparejo']=200


def guardarCliente(clave,valor):
	dbroot[clave]=valor

def guardarEmpleado(clave, valor):
	dbroot[clave]=valor

def obtenerCliente(clave):
	"""para retornar un cliente segun la clave que se le pasa"""
	try :
		if( dbroot[clave] != None):
			return dbroot[clave]
		else:
			raise(KeyError)
	except KeyError:
		print( 'CLIERNTE NO ENCONTRADO \nVERIFICAR LA C.I.: ',clave)

def obtenerEmpleado(clave):
	"""para retornar un empleado segun la clave que se le pasa"""
	try :
		if( dbroot[clave] != None):
			return dbroot[clave]
		else:
			raise(KeyError)
	except KeyError:
		print( 'EMPLEADO NO ENCONTRADO \nVERIFICAR LA C.I.: ',clave)

def obtenerDeposito(clave):
	"""para retornar la cantidad en stock que existe de ese objeto(ejemplo un ropero)"""
	try :
		return dbroot[clave]
	except ValueError:
		return None

def venderMueble(clave, cantidad):
	try:
		dbroot[clave] -= cantidad
		transaction.commit()
		return True
	except ValueError:
			return False

def fabricarMueble(clave,cantidad):
	try:
		dbroot[clave]+=cantidad
		transaction.commit()
		return True
	except ValueError:
			return False
			

def sustraerbienes(clave):
	dbroot[clave].bienes_alquilados={'Silla Grande':0, 'Silla Pequena':0,
	'Mesa Rectangulo':0, 'Mesa Redonda':0, 'Cubre':0, 'Vaso':0, 'Plato':0, 'Aparejo':0}
	transaction.commit()
