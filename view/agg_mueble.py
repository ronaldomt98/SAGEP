from Controller import Controller
from models.Mueble import *

from tkinter import *
from tkinter import messagebox


c=Controller()
tamano='720x650'
class AgregarMueble():


    def __init__(self, root):
        self.root = root
        self.vista_agregar_mueble(self.root)



    def validar(self, valor):
        if not valor.isdigit():
            raise Exception("Debe ser un valor numerico")

