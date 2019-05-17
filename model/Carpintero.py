

#...................................CLASE CARPINTERO..........................................
'''CLASE QUE se compone DE Empleado'''
class Carpintero:

    clave = "carpintero"
    def getClave(self):
        return self.clave

	def __init__(self, empleado):
		self.empleado = empleado

	def fabricar_mueble(self, bien, cantidad):
		pass

   
	def __str__(self):
		return (super().__str__()+'\nRUC: '+self.ruc+'\nMuebles:\n'+str(self.muebles))
		
		
