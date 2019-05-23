#.....................CLASE_NEGOCIO...........................................
class Negocio ():
   
	''' clase que contiene la lista de cliente, articulos, maqunarias, proveedores, empleados'''

	""" estas listas estaran en uso mientras el programa se este ejecutando"""
	Muebles = {}
	Clientes = {}
	Empleados = {}
	Maquinas = {}
	Proveedores = {}

#.....................CLASE_ACERCA_DE_(info_del_negocio).............................
class AcercaDe():
   
	def __init__(self, nombre, rubro):
		self.nombre=nombre
		self.rubro = rubro

      
	def __str__(self):
		return '\nNOMBRE DEL NEGOCIO: '+self.nombre+'\nRUBRO: '+self.rubro
