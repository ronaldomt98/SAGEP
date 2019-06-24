from controller.Controller import Controller
from models.Cliente import Cliente

from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("SAGEP")
tamano = '600x400+480+195'

varOpcion=IntVar()
barraMenu=Menu(root)
root.config(menu=barraMenu, width=800, height=650)
c=Controller()


#def __init__(self, ventana):
#   self.ventana = ventana
#    self.iniciar(self.ventana)

#def iniciar(self, ventana):
#    pass

def vista_agregar_cliente():

    root = Toplevel()
    root.title("Agregar Cliente")
    root.geometry('720x650')
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
    apellido = Label(miFrame, text="Apellido: ")
    apellido.grid(row=1, column=0, sticky="e")

    ci = StringVar(miFrame)
    cuadroCi = Entry(miFrame, textvariable=ci)
    cuadroCi.grid(row=1, column=1)
    ciLabel = Label(miFrame, text="C.I: ")
    ciLabel.grid(row=1, column=0, sticky="e")

    ruc = StringVar(miFrame)
    cuadroRuc = Entry(miFrame, textvariable=ruc)
    cuadroRuc.grid(row=1, column=1)
    rucLabel = Label(miFrame, text="Ruc: ")
    rucLabel.grid(row=1, column=0, sticky="e")

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

    Button(root, text='Guardar', width=20, bg='white', fg='white', command=add_cliente().place(x=120, y=580))
    Button(root, text='Salir', width=20, bg='white', fg='white', command=root.destroy).place(x=360, y=580)

    def add_cliente(self):
        ci = self.cedula.get()
        ruc = self.ruc.get()
        nom = self.nombre.get()
        ape = self.apellido.get()
        dire = self.direccion.get()
        telef = self.telefono.get()

        try:
            self.validar(ci)
            Label(root, text="Empleado Registrado").place(x=255, y=60)
            nuevoCliente = Cliente(ci, ruc, nom, ape, dire, telef)
            self.root.destroy()

            Controller.agregar_cliente(self,ci, nuevoCliente)
        except Exception as e:
            messagebox.askyesno("ERROR", e)


    def validar(self, valor):
        if not valor.isdigit():
            raise Exception("Debe ser un valor numerico")