from controller.Controller import *
from models.Cliente import Cliente

from tkinter import *
from tkinter import font
from tkinter import messagebox
import tkinter.ttk as ttk

tamano = '600x400+480+195'


class agregar_cliente():

    def __init__(self, ventana):
        self.ventana = ventana
        self.iniciar(self.ventana)

    def iniciar(self, ventana):

        'Tipo de fuente de la letra'
        self.ComicSansMS = font.Font(family="Comic Sans MS", size=13, weight="bold")

        self.nuev_clien = Toplevel(ventana)
        self.nuev_clien.config(bg="white")
        self.nuev_clien.resizable(0, 0)
        self.nuev_clien.geometry(tamano)
        self.nuev_clien.title("AGREGAR CLIENTE")
        self.nuev_clien.grab_set()

        '''intancia las notebook(pestañas)'''
        self.pestana = ttk.Notebook(self.ven_pedi)
        self.pestana.pack(fill='both', expand='yes')

        '''se istancias los frames que va contener los labeles, etc'''
        self.frmcli = Frame(self.pestana, bg='White', highlightthickness=2, highlightbackground='black')
        self.frmbien = Frame(self.pestana, bg='White', highlightthickness=2, highlightbackground='black')

        '''se agrega los frames a las pestañas'''
        self.pestana.add(self.frmcli, text='Cliente')

        Label(self.frmcli, text="Cedula:", bg='White', fg='red', font=self.ComicSansMS).place(x=60, y=25)
        self.cedula = Entry(self.frmcli)
        self.cedula.focus()
        self.cedula.place(x=160, y=30)

        Label(self.frmcli, text="Nombre: ", bg='White', font=self.ComicSansMS).place(x=60, y=117)
        self.nombre = Entry(self.frmcli)
        self.nombre.place(x=160, y=120)

        Label(self.frmcli, text="Apellido: ", bg='White', font=self.ComicSansMS).place(x=60, y=162)
        self.apellido = Entry(self.frmcli)
        self.apellido.place(x=160, y=165)

        Label(self.frmcli, text="Direccion: ", bg='White', font=self.ComicSansMS).place(x=60, y=207)
        self.direccion = Entry(self.frmcli)
        self.direccion.place(x=160, y=210)

        Label(self.frmcli, text="Telefono: ", bg='White', font=self.ComicSansMS).place(x=60, y=252)
        self.telefono = Entry(self.frmcli)
        self.telefono.place(x=160, y=255)

        self.btonAgregar = Button(self.nuev_clien, text="Guardar", command=self.add_cliente)
        self.btonAgregar.place(x=430, y=365)

        Button(self.ven_pedi, text="Cancelar", command=self.ven_clien.destroy).place(x=510, y=365)

    def add_cliente(self):
        ci = self.cedula.get()
        ruc = self.ruc.get()
        nom = self.nombre.get()
        ape = self.apellido.get()
        dire = self.direccion.get()
        telef = self.telefono.get()

        try:
            self.validar(ci)
            nuevoCliente = Cliente(nombre=nom, apellido=ape, cedula=int(ci),
                           direccion=dire, telefono=telef, ruc=ruc, muebles=None)
            self.nuev_clien.destroy()

            Controller.agregar_cliente(ci, nuevoCliente)
        except Exception as e:
            messagebox.askyesno("ERROR", e)