
class Cajero:

	clave = "cajero"
	def getClave(self):
		return self.clave

	def __init__(self, empleado):
		self.empleado = empleado

	def cobrar(self, bien, cantidad):
		pass

	def __str__(self):
		return (str(self.empleado))