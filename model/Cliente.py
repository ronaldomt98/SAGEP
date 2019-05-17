
from model.persona import Persona

#...................................CLASE CLIENTE..........................................
'''CASE QUE HEREDA DE Persona '''
class Cliente(Persona):

	clave = "cliente"
	def getClave(self):
		return self.clave

	def __init__(self,ruc, *muebles, **kwargs):
		super().__init__(**kwargs)
		self.ruc=ruc
		self.muebles=muebles

	def obtener_ruc(self):
		return self.ruc

	def obtener_muebles(self):
		return self.muebles
		
	def comprar(self, bien, cantidad):
		pass
   
	def __str__(self):
		return (super().__str__()+'\nRUC: '+self.ruc+'\nMuebles:\n'+str(self.muebles))
      

