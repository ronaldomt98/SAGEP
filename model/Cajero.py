from model.empleado import Empleado

#...................................CLASE CAJERO..........................................
'''CLASE QUE HEREDA DE Empleado'''
class Cajero(Empleado):
	clave = "cajero"
	def getClave(self):
		return self.clave

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def cobrar(self, bien, cantidad):
		pass

   
	def __str__(self):
		return (super().__str__()+'\nRUC: '+self.ruc+'\nMuebles:\n'+str(self.muebles))