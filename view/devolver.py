from tkinter import *
from Controller import *
from tkinter import messagebox

tamano = "400x120+520+180"


class Devolver():

    def __init__(self, root):
        self.root = root
        self.vista_devolver_mueble(self.root)


    def validar(self, valor):
        if not valor.isdigit():
            raise Exception("Debe ser un valor numerico")