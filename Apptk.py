from tkinter import *
from Bdatos import inicializar_stock
from view.ViewTk import ViewTk

inicializar_stock()

ventana = Tk()
ViewTk(ventana)
