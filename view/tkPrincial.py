from view.agg_cliente import AgregarCliente
from view.agg_empleado import AgregarEmpleado
from view.agg_mueble import AgregarMueble
from view.agg_venta import AgregarVenta
from view.devolver import Devolver
from Controller import Controller
from tkinter import messagebox
from tkinter import *


class TkPrincipal():

    def __init__(self, root):
        self.root = root
        self.principal(self.root)

    def principal(self, root):
        root.title("SAGEP")
        root.geometry("978x633")
        barraMenu = Menu(root)
        root.config(menu=barraMenu, width=978, height=633)
        root.resizable(10, 10)

        barraMenu = Menu(root)
        barraMenu.add_command(label="Devolución", command=self.devolver_mueble)

        menuAgregar = Menu(barraMenu, tearoff=0)
        menuAgregar.add_command(label="Agregar Clientes", command=self.agregar_cliente)
        menuAgregar.add_command(label="Agregar Empleado", command=self.agregar_empleado)
        menuAgregar.add_command(label="Aregar Venta", command=self.agregar_venta)
        menuAgregar.add_command(label="Aregar Mueble", command=self.agregar_mueble)

        menuListar = Menu(barraMenu, tearoff=0)
        menuListar.add_command(label="Lista de Clientes", command=Controller.listar_clientes(self))
        menuListar.add_command(label="Lista de Empleados", command=Controller.listar_empleados(self))
        menuListar.add_command(label="Lista de Muebles", command=Controller.listar_stock(self))

        barraMenu.add_cascade(label="Agregar", menu=menuAgregar)
        barraMenu.add_cascade(label="Listar", menu=menuListar)

        btnComprar = Button(root, text="SALIR", command=root.destroy).place(x=50, y=500)

        root.config(menu=barraMenu)
        root.mainloop()


    def agregar_cliente(self):
        AgregarCliente.vista_agregar_cliente(self.root)


    def agregar_empleado(self):
        AgregarEmpleado.vista_agregar_empleado(self.root)


    def agregar_venta(self):
        AgregarVenta.vista_agregar_venta(self.root)


    def agregar_mueble(self):
        AgregarMueble.vista_agregar_mueble(self.root)

    def devolver_mueble(self):
        Devolver.vista_devolver_mueble(self.root)


    def salir(self):
        if (messagebox.askyesno("Salir", "¿Terminar la ejecución?")):
            exit()