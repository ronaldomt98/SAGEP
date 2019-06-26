from models.Empleado import Empleado
from tkinter import *
from Controller import Controller
from tkinter import messagebox

tamano='720x650'
c=Controller()
class AgregarEmpleado():

	def __init__(self, root):
		self.root = root
		self.vista_agregar_empleado(self.root)

