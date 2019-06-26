from tkinter import *
from Controller import *
from tkinter import messagebox

tamano = "400x120+520+180"


class Devolver():

    def __init__(self, root):
        self.root = root
        self.vista_devolver_mueble(self.root)

    def vista_devolver_mueble(self, root):
        self.ven_devol = Toplevel(root)
        self.ven_devol.config(bg="white")
        self.ven_devol.resizable(0, 0)
        self.ven_devol.geometry(tamano)
        self.ven_devol.grab_set()
        self.ven_devol.title("Devolver Mueble")
        self.ven_devol.grab_set()

        label_0 = Label(root, text="Cliente", width=20, font=("bold", 20))
        label_0.place(x=160, y=20)
        miFrame = Frame(root)
        miFrame.pack()
        miFrame.place(x=100, y=100)

        cedula = StringVar(miFrame)
        cuadroCedula = Entry(miFrame, textvariable=cedula)
        cuadroCedula.grid(row=1, column=1)
        cedulaLabel = Label(miFrame, text="C.I: ")
        cedulaLabel.grid(row=1, column=0, sticky="e")

        Button(root, text='Guardar', width=20, bg='white', fg='white', command=self.devoluciones.place(x=120, y=580))
        Button(root, text='Salir', width=20, bg='white', fg='white', command=self.ven_devol.destroy).place(x=360, y=580)

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