from tkinter import *
from Apptk import vista_devolver_mueble
from Apptk import vista_agregar_cliente
from Apptk import vista_agregar_empleado
from Apptk import vista_agregar_venta
from Apptk import vista_agregar_mueble
from Apptk import vista_listar_clientes
from Apptk import vista_listar_empleados
from Apptk import vista_mostrar_muebles
from Bdatos import inicializar_stock

ventana = Tk()
inicializar_stock()

ventana.geometry("800x650")
ventana.title("SAGEP")
# creamos los menus

barraMenu = Menu(ventana)
barraMenu.add_command(label="Devolución", command=vista_devolver_mueble)

menuAgregar = Menu(barraMenu, tearoff=0)
menuAgregar.add_command(label="Agregar Clientes", command=vista_agregar_cliente)
menuAgregar.add_command(label="Agregar Empleado", command=vista_agregar_empleado)
menuAgregar.add_command(label="Aregar Venta", command=vista_agregar_venta)
menuAgregar.add_command(label="Aregar Mueble", command=vista_agregar_mueble)

menuListar = Menu(barraMenu, tearoff=0)
menuListar.add_command(label="Lista de Clientes", command=vista_listar_clientes)
menuListar.add_command(label="Lista de Empleados", command=vista_listar_empleados)
menuListar.add_command(label="Lista de Muebles", command=vista_mostrar_muebles)

barraMenu.add_cascade(label="Agregar", menu=menuAgregar)
barraMenu.add_cascade(label="Listar", menu=menuListar)

ventana.config(menu=barraMenu)
ventana.mainloop()
