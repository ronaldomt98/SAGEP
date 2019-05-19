
class Proveedor:

	clave = "proveedor"
	def getClave(self):
		return self.clave

	def __init__(self,nombre, ruc, contactos):
		self.nombre = nombre
		self.ruc = ruc
		self.contactos = contactos

	def obtener_ruc(self):
		return self.ruc

	def obtener_contactos(self):
		return self.contactos

	def vender(self, bien, cantidad):
		pass

	def __str__(self):
		return ('\nNombre: '+self.nombre+'\nRUC: '+self.ruc+'\nContactos:\n'+str(self.contactos))