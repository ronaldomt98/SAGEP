from persistent import *
from .Persona import Persona

#...................................CLASE EMPLEADO..........................................
'''CLASE QUE HEREDA DE Persona'''
class Empleado(Persona, Persistent):
   
	def __init__(self,ruc='Ninguno', muebles=None, **kwargs):
		super().__init__(**kwargs)
		self.ruc=ruc
		self.muebles=muebles

	def obtener_cargo(self):
		return self.cargo
		
	def comprar(self, bien, cantidad):
		pass
		
	def vender(self, bien, cantidad):
		pass

   
	def __str__(self):
		return (super().__str__()+'\nRUC: '+self.ruc+'\nMuebles:\n'+str(self.muebles))
		
		
		