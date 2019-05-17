from model.contacto import Contacto

#...................................CLASE EMAIL..........................................
'''CLASE QUE HEREDA DE CONTACTO'''
class Email(Contacto):

	clave = "email"
	def getClave(self):
		return self.clave

	def __init__(self,correo):
		self.correo = correo