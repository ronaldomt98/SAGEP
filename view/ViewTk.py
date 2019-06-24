from tkinter import *
from tkinter import messagebox
import random
from view.agg_empleado import agregar_empleado
from view.agg_cliente import agregar_cliente
from view.agg_venta import agregar_venta
from view.listAll import ListAll
from view.devolver import devolver

resolucion_prin = "430x430+450+100"
colores = ["Navy blue","gray", "black", "White", "green", "pink" ]

class ViewTk():

    def __init__(self, ventana):
        self.ventana = ventana
        self.main(self.ventana)

    def vista_listar_clientes(self, listaDeClientes):
        ventanaAbrir = Toplevel()
        ventanaAbrir.geometry("400x400+100+100")
        ventanaAbrir.title("Listado de Clientes")
        texto = Text(ventanaAbrir, height=720, width=480)
        for cliente in listaDeClientes:
            texto.insert(INSERT, 'Nombre: ' + str(cliente.nombre) + '\n' + 'Apellido: ' + str(
                cliente.apellido) + '\n' + 'Direccion: ' + str(cliente.direccion) + '\n' + 'Ruc: ' + str(
                cliente.ruc) + '\n' + 'Telefono: ' + str(cliente.contacto) + '\n')
            texto.pack()

    def vista_listar_empleados(self, listaDeEmpleados):
        ventanaAbrir = Toplevel()
        ventanaAbrir.geometry("400x400+100+100")
        ventanaAbrir.title("Listado de Empleados")
        texto = Text(ventanaAbrir, height=720, width=480)
        for empleado in listaDeEmpleados:
            texto.insert(INSERT, 'Nombre: ' + str(empleado.nombre) + '\n' + 'Telefono: ' + str(
                empleado.telefono) + '\n' + 'Direccion: ' + str(empleado.direccion) + '\n' + 'CI: ' + str(
                empleado.ci) + '\n')  + '\n' + 'Cargo: ' + str(empleado.cargo) + '\n' + 'Salario: ' + str(
                empleado.salario)
            texto.pack()

    def vista_listar_muebles(self, listaDeMuebles):
        ventanaAbrir = Toplevel()
        ventanaAbrir.geometry("400x400+100+100")
        ventanaAbrir.title("Listado de Muebles")
        texto = Text(ventanaAbrir, height=720, width=480)
        for productomedi in listaDeMuebles:
            texto.insert(INSERT,
                         'Nombre: ' + str(productomedi.nombre) + '\n' + 'Precio: ' + str(productomedi.precio) + '\n')
            texto.pack()

    def main(self, ventana):
        ventana.resizable(10, 10)
        ventana.geometry(resolucion_prin)
        ventana.title("SISTEMA DE ADMINISTRACION Y GESTION DE PRODUCTOS")
        ventana.protocol("WM_DELETE_WINDOW", self.salir)
        ventana.config(bg=random.choice(colores))
        icono = PhotoImage(file='./view/icons/icono.png')
        ventana.iconphoto(ventana, icono)  # Asigna icono app

        barraMenu = Menu(ventana)

        imagen = PhotoImage(file="fondo.png")
        lbl = Label(ventana, image=imagen).place(x=5, y=5)

        menuVenta = Menu(barraMenu, tearoff=0)
        menuVenta.add_command(label="Aregar Venta", command=self.agregar_venta)
        barraMenu.add_cascade(label="Aregar Venta", menu=menuVenta)

        barraMenu.add_command(label="Devolución", command=self.devuelve)

        menuEmpleado = Menu(barraMenu, tearoff=0)
        menuEmpleado.add_command(label="Aregar Empleado", command=self.add_empl)
        barraMenu.add_cascade(label="Empleado", menu=menuEmpleado)

        menuCliente = Menu(barraMenu, tearoff=0)
        menuCliente.add_command(label="Aregar Clientes", command=self.add_clie)
        barraMenu.add_cascade(label="Cliente", menu=menuCliente)

        menuList = Menu(barraMenu, tearoff=0)
        menuList.add_command(label="Listar", command=self.list)
        barraMenu.add_cascade(label="Lista de Clientes", command=self.list)

        ventana.config(menu=barraMenu)
        ventana.mainloop()


    def list(self):
        ListAll(self.ventana)


    def add_empl(self):
        agregar_empleado(self.ventana)

    def add_clie(self):
        agregar_cliente(self.ventana)


    def agregar_venta(self):
        agregar_venta(self.ventana)


    def devuelve(self):
        devolver(self.ventana)


    def salir(self):
        if (messagebox.askyesno("Salir", "¿Terminar la ejecución?")):
            exit()
