from models.Empleado import Empleado
from tkinter import *
from Controller import Controller
from tkinter import messagebox

tamano='720x650'
c=Controller()
class AgregarEmpleado():

	def __init__(self, root):
		self.root = root
		self.vista_agregar_empleado(self.root)

	def vista_agregar_empleado(self, root):
		self.ven_emp = Toplevel(root)
		self.ven_emp.config(bg="white")
		self.ven_emp.resizable(0, 0)
		self.ven_emp.geometry(tamano)
		self.ven_emp.title("Registrar Empleado")
		self.ven_emp.grab_set()

		label_0 = Label(root, text="Empleado", width=20, font=("bold", 20))
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

		cedula = StringVar(miFrame)
		cuadroCedula = Entry(miFrame, textvariable=cedula)
		cuadroCedula.grid(row=2, column=1)
		CedulaLabel = Label(miFrame, text="CI: ")
		CedulaLabel.grid(row=2, column=0, sticky="e")

		telefono = StringVar(miFrame)
		cuadroTelefono = Entry(miFrame, textvariable=telefono)
		cuadroTelefono.grid(row=4, column=1)
		telefonoLabel = Label(miFrame, text="Telefono: ")
		telefonoLabel.grid(row=4, column=0, sticky="e")

		direccion = StringVar(miFrame)
		cuadroDireccion = Entry(miFrame, textvariable=direccion)
		cuadroDireccion.grid(row=5, column=1)
		direccionLabel = Label(miFrame, text="Direccion: ")
		direccionLabel.grid(row=5, column=0, sticky="e")

		cargo = StringVar(miFrame)
		cuadroCargo = Entry(miFrame, textvariable=cargo)
		cuadroCargo.grid(row=5, column=1)
		cargoLabel = Label(miFrame, text="Cargo: ")
		cargoLabel.grid(row=5, column=0, sticky="e")

		salario = StringVar(miFrame)
		cuadroSalario = Entry(miFrame, textvariable=salario)
		cuadroSalario.grid(row=5, column=1)
		salarioLabel = Label(miFrame, text="Salario: ")
		salarioLabel.grid(row=5, column=0, sticky="e")

		Button(root, text='Registrar', width=20, bg='purple', fg='white', command=self.add_empleado).place(x=120, y=580)
		Button(root, text='Salir', width=20, bg='purple', fg='white', command=self.ven_emp.destroy).place(x=360, y=580)

	def add_empleado(self):
		nomb = self.nombre.get()
		ci = self.cedula.get()
		telef = self.telefono.get()
		dir = self.direccion.get()
		apell = self.apellido.get()
		carg = self.cargo.get()
		sal = self.salario.get()

		try:
			self.validar(ci)
			self.validar(sal)
			nuevoEmpleado = Empleado(nomb, apell,ci, dir, telef,carg,sal)
			c.guardar_empleado(nuevoEmpleado)
			messagebox.INFO("Empleado Registrado")
			self.root.destroy()
		except Exception as e:
			messagebox.askyesno("ERROR", e)

	def validar(self, valor):
		if not valor.isdigit():
			raise Exception("Debe ser un valor numerico")



