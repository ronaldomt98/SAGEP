from tkinter import *
from controller.Controller import *
from tkinter import font
from tkinter import messagebox

tamano = "400x120+520+180"


class devolver():

    def __init__(self, ventana):
        self.ventana = ventana
        self.iniciar(self.ventana)

    def iniciar(self, ventana):
        self.ven_devo = Toplevel(ventana)
        self.ven_devo.config(bg='White')
        self.ven_devo.resizable(0, 0)
        self.ven_devo.geometry(tamano)
        self.ven_devo.title("Registrar")
        self.ven_devo.grab_set()

        self.id = IntVar()
        self.id.set('')
        self.ComicSansMS = font.Font(family="Comic Sans MS", size=11, weight="bold")
        self.MVBoli = font.Font(family="MV Boli", size=15, weight="bold")

        Label(self.ven_devo, text="DEVOLUCIONES", bg='White', font=self.MVBoli).place(x=100, y=0)
        Label(self.ven_devo, text="N° CEDULA: ", bg='White', font=self.ComicSansMS).place(x=50, y=50)

        self.cedula = Entry(self.ven_devo, textvariable=self.id)
        self.cedula.focus()
        self.cedula.place(x=155, y=55)

        Button(self.ven_devo, text="Devolver", command=self.devoluciones).place(x=241, y=90)
        Button(self.ven_devo, text="Cancelar", command=self.ven_devo.destroy).place(x=320, y=90)

    def devoluciones(self):
        ci = self.cedula.get()
        print(ci)
        try:
            self.validar(ci)
            self.ven_devo.destroy()
            Controller.devolver_mueble(self,ci)
            messagebox.showinfo('Aviso', 'EXITO AL DEVOLVER')
        except Exception as e:
            messagebox.askyesno("ERROR", e)

    def validar(self, valor):
        if not valor.isdigit():
            raise Exception("Debe ser un valor numerico")