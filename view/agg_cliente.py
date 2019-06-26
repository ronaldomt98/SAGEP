from Controller import Controller
from models.Cliente import Cliente

from tkinter import *
from tkinter import messagebox

c=Controller()
tamano='720x650'
class AgregarCliente():

    def __init__(self, root):
        self.root = root
        self.vista_agregar_cliente(self.root)

    def vista_agregar_cliente(self, root):

        self.ven_vent = Toplevel(root)
        self.ven_vent.config(bg="white")
        self.ven_vent.resizable(0, 0)
        self.ven_vent.geometry(tamano)
        self.ven_vent.title("Registrar Cliente")
        self.ven_vent.grab_set()

        label_0 = Label(root, text="Cliente", width=20, font=("bold", 20))
        label_0.place(x=160, y=20)
        miFrame = Frame(root)
        miFrame.pack()
        miFrame.place(x=100, y=100)

        nombre = StringVar(miFrame)
        cuadroNombre = Entry(miFrame, textvariable=nombre)
        cuadroNombre.grid(row=0, column=1)
        nombreLabel = Label(miFrame, text="Nombre: ")
        nombreLabel.grid(row=0, column=0, sticky="e")

        apellido = StringVar(miFrame)
        cuadroApellido = Entry(miFrame, textvariable=apellido)
        cuadroApellido.grid(row=1, column=1)
        apellidoLabel = Label(miFrame, text="Apellido: ")
        apellidoLabel.grid(row=1, column=0, sticky="e")

        cedula = StringVar(miFrame)
        cuadroCedula = Entry(miFrame, textvariable=cedula)
        cuadroCedula.grid(row=1, column=1)
        cedulaLabel = Label(miFrame, text="C.I: ")
        cedulaLabel.grid(row=1, column=0, sticky="e")

        digitoVerificador = StringVar(miFrame)
        cuadroDigitoVerificador = Entry(miFrame, textvariable=digitoVerificador)
        cuadroDigitoVerificador.grid(row=1, column=1)
        digitoVerificadorLabel = Label(miFrame, text="Digito Verificador: ")
        digitoVerificadorLabel.grid(row=1, column=0, sticky="e")

        telefono = StringVar(miFrame)
        cuadroTelefono = Entry(miFrame, textvariable=telefono)
        cuadroTelefono.grid(row=2, column=1)
        telefonoLabel = Label(miFrame, text="Telefono: ")
        telefonoLabel.grid(row=2, column=0, sticky="e")

        direccion = StringVar(miFrame)
        cuadroDireccion = Entry(miFrame, textvariable=direccion)
        cuadroDireccion.grid(row=4, column=1)
        direccionLabel = Label(miFrame, text="Direccion: ")
        direccionLabel.grid(row=4, column=0, sticky="e")

        Button(root, text='Guardar', width=20, bg='white', fg='white', command=self.add_cliente.place(x=120, y=580))
        Button(root, text='Salir', width=20, bg='white', fg='white', command=root.destroy).place(x=360, y=580)

    def add_cliente(self):
        ci = self.cedula.get()
        digito = self.digitoVerificador.get()
        nom = self.nombre.get()
        ape = self.apellido.get()
        dire = self.direccion.get()
        telef = self.telefono.get()

        try:
            if not ci.isdigit():
                raise Exception("Debe ser un valor numerico")
            nuevoCliente = Cliente(ci, digito, nom, ape, dire, telef)
            c.agregar_cliente(ci, nuevoCliente)
            messagebox.INFO("Cliente Registrado")
            self.root.destroy()
        except Exception as e:
            messagebox.askyesno("ERROR", e)

        def validar(self, valor):
            if not valor.isdigit():
                raise Exception("Debe ser un valor numerico")



