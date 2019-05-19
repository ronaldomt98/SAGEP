from model.Contacto import Contacto

class Email(Contacto):

	clave = "email"
	def getClave(self):
		return self.clave

	def __init__(self,correo):
		self.correo = correo

	def __str__(self):
		return ('\nEmail: '+self.correo)