from controller.Controller import *
from models.Empleado import Empleado

from tkinter import *
from tkinter import font
from tkinter import messagebox

tamano = '600x400+480+195'
class agregar_empleado():

	def __init__(self, ventana):
		self.ventana = ventana
		self.iniciar(self.ventana)

	def iniciar(self, ventana):
		
		self.nuev_emp = Toplevel(ventana)
		self.nuev_emp.config(bg='White')
		self.nuev_emp.resizable(0, 0)
		self.nuev_emp.geometry(tamano)
		self.nuev_emp.title("Registrar")
		self.nuev_emp.grab_set()
		
		icono= PhotoImage(file='./view/icons/addempleado.png')
		self.nuev_emp.iconphoto(self.nuev_emp, icono)  # Asigna icono app
		
		imagen = PhotoImage(file = './view/icons/empleado.png')
		lbl = Label(self.nuev_emp, image=imagen).grid(row=10, column=12)
		
		ComicSansMS = font.Font(family="Comic Sans MS",size=11,weight="bold")
		DejaVuSansMono = font.Font(family="DejaVu Sans Mono",size=15,weight="bold")
		Label(self.nuev_emp, text="REGISTRAR EMPLEADO", bg='White',font=DejaVuSansMono).grid(row=1, column=10)

		
		Label(self.nuev_emp, text="Cedula:",bg='White', fg='red',font=ComicSansMS).grid(row=5, column=9)
		self.cedula = Entry(self.nuev_emp)
		self.cedula.focus()
		self.cedula.grid(row=5, column=10)
		
		Label(self.nuev_emp, text="Nombre: ",bg='White',font=ComicSansMS).grid(row=6, column=9)
		self.nombre = Entry(self.nuev_emp)
		self.nombre.grid(row=6, column=10)
		
		Label(self.nuev_emp, text="Apellido: ",bg='White',font=ComicSansMS).grid(row=7, column=9)
		self.apellido = Entry(self.nuev_emp)
		self.apellido.grid(row=7, column=10)
		
		Label(self.nuev_emp, text="Direccion: ",bg='White',font=ComicSansMS).grid(row=8, column=9)
		self.direccion = Entry(self.nuev_emp)
		self.direccion.grid(row=8, column=10)

		Label(self.nuev_emp, text="Cargo: ",bg='White',font=ComicSansMS).grid(row=9, column=9)
		self.cargo = Entry(self.nuev_emp)
		self.cargo.grid(row=9, column=10)

		Label(self.nuev_emp, text="Telefono: ", bg='White', font=ComicSansMS).grid(row=10, column=9)
		self.telefono = Entry(self.nuev_emp)
		self.telefono.grid(row=10, column=10)

		Label(self.nuev_emp, text="Salario: ",bg='White',font=ComicSansMS).grid(row=11, column=9)
		self.salario = Entry(self.nuev_emp)
		self.salario.focus()
		self.salario.grid(row=11, column=10)

		Label(self.nuev_emp, text="Fecha Ingreso: ", bg='White', font=ComicSansMS).grid(row=12, column=9)
		self.fecha_ingreso = Entry(self.nuev_emp)
		self.fecha_ingreso.grid(row=12, column=10)

		self.btonAgregar = Button(self.nuev_emp, text="Agregar", command=self.addempleado)
		self.btonAgregar.grid(row=6, column=12)
        
		Button(self.nuev_emp, text="Cancelar", command=self.nuev_emp.destroy).grid(row=8, column=12)
		
		self.nuev_emp.mainloop()
		
	def addempleado(self):
		ci = self.cedula.get()
		nom = self.nombre.get()
		ape = self.apellido.get()
		dire = self.direccion.get()
		carg = self.cargo.get()
		telef = self.telefono.get()
		sal = self.salario.get()
		fech_ing = self.fecha_ingreso.get()

		try:
			self.validar(ci)
			self.validar(sal)
			nuevoEmpleado = Empleado(cargo=carg, salario = sal, fecha_ingreso= fech_ing,
									 muebles = None, nombre=nom, apellido=ape, cedula=int(ci),
									 direccion=dire, contactos=telef)
			self.nuev_emp.destroy()
			Controller.agregar_empleado(self,ci, nuevoEmpleado)
		except Exception as e:
			messagebox.askyesno("ERROR", e)

		
	def validar(self, valor):
		if not valor.isdigit():
			raise Exception("Debe ser un valor numerico")

