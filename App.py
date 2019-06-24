'''SISTEMA DE ADMINISTRACION Y GESTION DE PRODUCTOS'''
import os
from view.View import View
from Bdatos import inicializar_stock
from controller.Controller import Controller


class App ():
	'''METODO ESTATICO QUE DA INICIO A LA APLICACION'''
	@staticmethod
	def iniciar ():
		inicializar_stock()
		App.menu()


	'''OPCIONES QUE LA APLICACION PERMITE ELEGIR AL USUARIO'''
	def menu ():
		opmenu=0 #variable que controla el menu principal de las operaciones
		while (opmenu != 6):
			print('▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼'.center(80, '▼'))
			print()
			print("::::::::::::::::::::::::::::::::::::::".center(80, " "))
			print(": ╔══════════════════════════════════════╗ :".center(80, ' '))
			print(": ║ SISTEMA SISTEMA AUTOMATIZADO PARA LA ║ :".center(80, ' '))
			print(": ║ ADMINISTRACIÓN Y GESTIÓN DEPRODUCTOS ║ :".center(80, ' '))
			print(": ╚══════════════════════════════════════╝ :".center(80, ' '))
			print("::::::::::::::::::::::::::::::::::::::".center(80, " "))
			print("\n\t\t\t[1]  ► AGREGAR CLIENTE\n\t\t\t[2]  ► CONSULTAR CLIENTE"
				  "\n\t\t\t[3]  ► LISTAR CLIENTES\n\t\t\t[4]  ► VENDER MUEBLE\n\t\t\t[5]  ► INGRESAR NUEVO MUEBLE\n"
				  "\n\t\t\t[6]  ► SALIR\n")
			print('▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲'.center(80, '▲'))
			opmenu = input_rango("UD. PUEDE ELEGIR", 1, 6)
			print("▬▬▬▬▬▬▬▬".center(32, "▬"))
			if opmenu == 1 :
				Controller.agregar_cliente()
			if opmenu == 2 :
				View.leer_cedula()
			if opmenu == 3 :
				Controller.listar_clientes()
			if opmenu == 4 :
				Controller.vender()
			if opmenu == 5 :
				Controller.agregar_mueble()
			if opmenu == 6 :
				os.system('cls')
				print('..............------------... \n.............(   Adios!   ).. \n..............`--, ,-----´... \n.......@@@.......)/.......... ')
				print('.....@.....@.........,....... \n.....@.....@.......o00o...... \n.......@@@.........o@@....... \n........@..........@......... \n.......@@@........@.......... ')
				print('......@.@..@.....@........... \n.....@..@.....@@............. \n....@...@.................... \n...@....@.................... \n..@.....@......... made ..... ')
				print('........@.........  by  ..... \n........@...... Ronaldo ..... \n.......@.@................... \n......@....@................. \n.....@......@................ ')
				print('....@........@............... \n...@..........@.............. \n.@@@..........@@@............ ')


if __name__ == '__main__':
	App.iniciar()
