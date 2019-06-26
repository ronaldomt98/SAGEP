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

    def vista_agregar_mueble(self, root):

        self.ven_mueb = Toplevel(root)
        self.ven_mueb.config(bg="white")
        self.ven_mueb.resizable(0, 0)
        self.ven_mueb.geometry(tamano)
        self.ven_mueb.title("Registrar Mueble")
        self.ven_mueb.grab_set()

        label_0 = Label(root, text="Mueble", width=20, font=("bold", 20))
        label_0.place(x=160, y=20)
        miFrame = Frame(root)
        miFrame.pack()
        miFrame.place(x=100, y=100)

        armario = StringVar(miFrame)
        cuadroArmario= Entry(miFrame, textvariable=armario)
        cuadroArmario.grid(row=0, column=1)
        ArmarioLabel = Label(miFrame, text="Armario: ")
        ArmarioLabel.grid(row=0, column=0, sticky="e")

        cama = StringVar(miFrame)
        cuadroCama= Entry(miFrame, textvariable= cama)
        cuadroCama.grid(row=1, column=1)
        camaLabel = Label(miFrame, text="Cama: ")
        camaLabel.grid(row=1, column=0, sticky="e")

        comoda = StringVar(miFrame)
        cuadroComoda= Entry(miFrame, textvariable= comoda)
        cuadroComoda.grid(row=1, column=1)
        comodaLabel = Label(miFrame, text="Comoda: ")
        comodaLabel.grid(row=1, column=0, sticky="e")

        escritorio = StringVar(miFrame)
        cuadroEscritorio= Entry(miFrame, textvariable= escritorio)
        cuadroEscritorio.grid(row=1, column=1)
        escritorioLabel = Label(miFrame, text="Escritorio: ")
        escritorioLabel.grid(row=1, column=0, sticky="e")

        estanteria = StringVar(miFrame)
        cuadroEstanteria= Entry(miFrame, textvariable= estanteria)
        cuadroEstanteria.grid(row=1, column=1)
        estanteriaLabel = Label(miFrame, text="Estanteria: ")
        estanteriaLabel.grid(row=1, column=0, sticky="e")

        mesa = StringVar(miFrame)
        cuadroMesa= Entry(miFrame, textvariable= mesa)
        cuadroMesa.grid(row=1, column=1)
        mesaLabel = Label(miFrame, text="Mesa: ")
        mesaLabel.grid(row=1, column=0, sticky="e")

        silla = StringVar(miFrame)
        cuadroSilla= Entry(miFrame, textvariable= silla)
        cuadroSilla.grid(row=1, column=1)
        sillaLabel = Label(miFrame, text="Silla: ")
        sillaLabel.grid(row=1, column=0, sticky="e")

        taburete = StringVar(miFrame)
        cuadroTaburete= Entry(miFrame, textvariable= taburete)
        cuadroTaburete.grid(row=1, column=1)
        tabureteLabel = Label(miFrame, text="Mesa: ")
        tabureteLabel.grid(row=1, column=0, sticky="e")

        vitrina = StringVar(miFrame)
        cuadroVitrina = Entry(miFrame, textvariable=vitrina)
        cuadroVitrina.grid(row=1, column=1)
        vitrinaLabel = Label(miFrame, text="Silla: ")
        vitrinaLabel.grid(row=1, column=0, sticky="e")

        Button(root, text='Guardar', width=20, bg='white', fg='white', command=self.add_mueble.place(x=120, y=580))
        Button(root, text='Salir', width=20, bg='white', fg='white', command=self.ven_mueb.destroy).place(x=360, y=580)

    def add_mueble(self):
        armar = self.armario.get()
        cam = self.cama.get()
        comod = self.comoda.get()
        escrit = self.escritorio.get()
        estant = self.estanteria.get()
        mes = self.mesa.get()
        sill = self.silla.get()
        taburet = self.taburete.get()
        vitrin = self.vitrina.get()

        try:
            self.validar(armar)
            self.validar(cam)
            self.validar(comod)
            self.validar(escrit)
            self.validar(estant)
            self.validar(mes)
            self.validar(sill)
            self.validar(taburet)
            self.validar(vitrin)

            Controller.agregar_mueble(armar, cam, comod, escrit, estant, mes, sill, taburet, vitrin)
            messagebox.INFO("Cliente Registrado")
            self.root.destroy()
        except Exception as e:
            messagebox.askyesno("ERROR", e)

    def validar(self, valor):
        if not valor.isdigit():
            raise Exception("Debe ser un valor numerico")

