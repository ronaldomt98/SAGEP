from tkinter import *
from models.Mueble import *

root=Tk()
root.title("SAGEP")
varOpcion=IntVar()
barraMenu=Menu(root)
root.config(menu=barraMenu, width=800, height=650)


class ViewTk():

	def vista_mostrar_cliente(self, cliente):
		ventanaAbrir = Toplevel()
		ventanaAbrir.geometry("400x400+100+100")
		ventanaAbrir.title("Listado de Clientes")
		texto = Text(ventanaAbrir, height=720, width=480)
		texto.insert(INSERT, 'Nombre: ' + str(cliente.nombre) + '\n' + 'Apellido: ' + str(
			cliente.apellido) + '\n' + 'Direccion: ' + str(cliente.direccion) + '\n' + 'Ruc: ' + str(
			cliente.ruc) + '\n' + 'Telefono: ' + str(cliente.contacto) + '\n')
		texto.pack()


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
				empleado.cedula) + '\n') + '\n' + 'Cargo: ' + str(empleado.cargo) + '\n' + 'Salario: ' + str(
				empleado.salario)
			texto.pack()


	def vista_mostrar_muebles(self, listaDeMuebles):
		ventanaAbrir = Toplevel()
		ventanaAbrir.geometry("400x400+100+100")
		ventanaAbrir.title("Listado de Muebles")
		texto = Text(ventanaAbrir, height=720, width=480)
		for mueble in listaDeMuebles:
			texto.insert(INSERT,
						 'Nombre: ' + mueble.get_clave + '\n' + 'Cantidad: ' + str(mueble.cantidad) + '\n')
			texto.pack()
