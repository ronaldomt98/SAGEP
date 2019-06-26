from persistent import Persistent
class Stock(Persistent):

	def __init__(self):
		self.cantidad=0
