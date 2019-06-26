from tkinter import *

from Bdatos import inicializar_stock
from view.tkPrincial import TkPrincipal



inicializar_stock()
root = Tk()
TkPrincipal(root)
