from persistent import Persistent
class Venta(Persistent):

	def __init__(self):
		self.cantidad=0
		self.ci = 0
		self.mueble=0
		self.revertida = False