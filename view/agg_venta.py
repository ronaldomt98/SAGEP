from Controller import *
from Bdatos import*

from tkinter import *
from tkinter import font
from tkinter import messagebox
import tkinter.ttk as ttk

tamano='720x650'
class AgregarVenta():

    def __init__(self, root):
        self.root = root
        self.vista_agregar_mueble(self.root)



    def validar(self, valor):
         if not valor.isdigit():
            raise Exception("Debe ser un valor numerico")
