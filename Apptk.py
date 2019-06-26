from tkinter import *
from Controller import Controller
from Bdatos import inicializar_stock
from tkinter import messagebox
from models.Cliente import Cliente
from models.Empleado import Empleado
root=Tk()
root.title("SAGEP")

varOpcion=IntVar()
barraMenu=Menu(root)
root.config(menu=barraMenu, width=800, height=650)
c=Controller()

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
    apellidoLabel = Label(miFrame, text="Apellido: ")
    apellidoLabel.grid(row=1, column=0, sticky="e")

    cedula = StringVar(miFrame)
    cuadroCedula = Entry(miFrame, textvariable=cedula)
    cuadroCedula.grid(row=2, column=1)
    cedulaLabel = Label(miFrame, text="C.I: ")
    cedulaLabel.grid(row=2, column=0, sticky="e")

    digitoVerificador = StringVar(miFrame)
    cuadroDigitoVerificador = Entry(miFrame, textvariable=digitoVerificador)
    cuadroDigitoVerificador.grid(row=3, column=1)
    digitoVerificadorLabel = Label(miFrame, text="Digito Verificador: ")
    digitoVerificadorLabel.grid(row=3, column=0, sticky="e")

    telefono = StringVar(miFrame)
    cuadroTelefono = Entry(miFrame, textvariable=telefono)
    cuadroTelefono.grid(row=4,  column=1)
    telefonoLabel = Label(miFrame, text="Telefono: ")
    telefonoLabel.grid(row=4, column=0, sticky="e")

    direccion = StringVar(miFrame)
    cuadroDireccion = Entry(miFrame, textvariable=direccion)
    cuadroDireccion.grid(row=5, column=1)
    direccionLabel = Label(miFrame, text="Direccion: ")
    direccionLabel.grid(row=5, column=0, sticky="e")


    def add_cliente():
        ci = cedula.get()
        digito = digitoVerificador.get()
        nom = nombre.get()
        ape = apellido.get()
        dire = direccion.get()
        telef = telefono.get()

        try:
            validar(ci)
            nuevoCliente = Cliente(ci, digito, nom, ape, dire)
            c.agregar_cliente(ci, nuevoCliente)
            messagebox.INFO("Cliente Registrado")
            root.destroy()
        except Exception as e:
            messagebox.askyesno("ERROR", e)

    Button(root, text='Guardar', width=20, bg='white', fg='white', command=add_cliente).place(x=120, y=580)
    Button(root, text='Salir', width=20, bg='white', fg='white', command=root.destroy).place(x=360, y=580)


def vista_agregar_empleado():
    root = Toplevel()
    root.title("Agregar Empleado")
    root.geometry('720x650')
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

    def add_empleado():
        nomb = nombre.get()
        ci = cedula.get()
        telef = telefono.get()
        dir = direccion.get()
        apell = apellido.get()
        carg = cargo.get()
        sal = salario.get()

        try:
            validar(ci)
            validar(sal)
            nuevoEmpleado = Empleado(nomb, apell, ci, dir, telef, carg, sal)
            c.guardar_empleado(nuevoEmpleado)
            messagebox.INFO("Empleado Registrado")
            root.destroy()
        except Exception as e:
            messagebox.askyesno("ERROR", e)


    Button(root, text='Registrar', width=20, bg='purple', fg='white', command= add_empleado).place(x=120, y=580)
    Button(root, text='Salir', width=20, bg='purple', fg='white', command=root.destroy).place(x=360, y=580)

def vista_agregar_mueble():
    root = Toplevel()
    root.title("Agregar Mueble")
    root.geometry('720x650')
    label_0 = Label(root, text="Mueble", width=20, font=("bold", 20))
    label_0.place(x=160, y=20)
    miFrame = Frame(root)
    miFrame.pack()
    miFrame.place(x=100, y=100)

    armario = StringVar(miFrame)
    cuadroArmario= Entry(miFrame, textvariable=armario)
    cuadroArmario.grid(row=0, column=1)
    ArmarioLabel = Label(miFrame, text="Armario: ")
    ArmarioLabel.grid(row=0, column=0, sticky="e")

    cama = StringVar(miFrame)
    cuadroCama= Entry(miFrame, textvariable= cama)
    cuadroCama.grid(row=1, column=1)
    camaLabel = Label(miFrame, text="Cama: ")
    camaLabel.grid(row=1, column=0, sticky="e")

    comoda = StringVar(miFrame)
    cuadroComoda= Entry(miFrame, textvariable= comoda)
    cuadroComoda.grid(row=1, column=1)
    comodaLabel = Label(miFrame, text="Comoda: ")
    comodaLabel.grid(row=1, column=0, sticky="e")

    escritorio = StringVar(miFrame)
    cuadroEscritorio= Entry(miFrame, textvariable= escritorio)
    cuadroEscritorio.grid(row=1, column=1)
    escritorioLabel = Label(miFrame, text="Escritorio: ")
    escritorioLabel.grid(row=1, column=0, sticky="e")

    estanteria = StringVar(miFrame)
    cuadroEstanteria= Entry(miFrame, textvariable= estanteria)
    cuadroEstanteria.grid(row=1, column=1)
    estanteriaLabel = Label(miFrame, text="Estanteria: ")
    estanteriaLabel.grid(row=1, column=0, sticky="e")

    mesa = StringVar(miFrame)
    cuadroMesa= Entry(miFrame, textvariable= mesa)
    cuadroMesa.grid(row=1, column=1)
    mesaLabel = Label(miFrame, text="Mesa: ")
    mesaLabel.grid(row=1, column=0, sticky="e")

    silla = StringVar(miFrame)
    cuadroSilla= Entry(miFrame, textvariable= silla)
    cuadroSilla.grid(row=1, column=1)
    sillaLabel = Label(miFrame, text="Silla: ")
    sillaLabel.grid(row=1, column=0, sticky="e")

    taburete = StringVar(miFrame)
    cuadroTaburete= Entry(miFrame, textvariable= taburete)
    cuadroTaburete.grid(row=1, column=1)
    tabureteLabel = Label(miFrame, text="Mesa: ")
    tabureteLabel.grid(row=1, column=0, sticky="e")

    vitrina = StringVar(miFrame)
    cuadroVitrina = Entry(miFrame, textvariable=vitrina)
    cuadroVitrina.grid(row=1, column=1)
    vitrinaLabel = Label(miFrame, text="Silla: ")
    vitrinaLabel.grid(row=1, column=0, sticky="e")


    def add_mueble():
        armar = armario.get()
        cam = cama.get()
        comod = comoda.get()
        escrit = escritorio.get()
        estant = estanteria.get()
        mes = mesa.get()
        sill = silla.get()
        taburet = taburete.get()
        vitrin = vitrina.get()

        try:
            validar(armar)
            validar(cam)
            validar(comod)
            validar(escrit)
            validar(estant)
            validar(mes)
            validar(sill)
            validar(taburet)
            validar(vitrin)

            Controller.agregar_mueble(armar, cam, comod, escrit, estant, mes, sill, taburet, vitrin)
            messagebox.INFO("Cliente Registrado")
            root.destroy()
        except Exception as e:
            messagebox.askyesno("ERROR", e)

    Button(root, text='Guardar', width=20, bg='white', fg='white', command=add_mueble).place(x=120, y=580)
    Button(root, text='Salir', width=20, bg='white', fg='white', command=root.destroy).place(x=360, y=580)

def vista_agregar_venta(self, root):
    root = Toplevel()
    root.title("Agregar venta")
    root.geometry('720x650')
    label_0 = Label(root, text="Venta", width=20, font=("bold", 20))
    label_0.place(x=160, y=20)
    miFrame = Frame(root)
    miFrame.pack()
    miFrame.place(x=100, y=100)

    ci = StringVar(miFrame)
    cuadroCi= Entry(miFrame, textvariable=ci)
    cuadroCi.grid(row=0, column=1)
    ciLabel = Label(miFrame, text="C.I del cliente: ")
    ciLabel.grid(row=0, column=0, sticky="e")

    armario = StringVar(miFrame)
    cuadroArmario = Entry(miFrame, textvariable=armario)
    cuadroArmario.grid(row=0, column=1)
    ArmarioLabel = Label(miFrame, text="Armario: ")
    ArmarioLabel.grid(row=0, column=0, sticky="e")

    cama = StringVar(miFrame)
    cuadroCama = Entry(miFrame, textvariable=cama)
    cuadroCama.grid(row=1, column=1)
    camaLabel = Label(miFrame, text="Cama: ")
    camaLabel.grid(row=1, column=0, sticky="e")

    comoda = StringVar(miFrame)
    cuadroComoda = Entry(miFrame, textvariable=comoda)
    cuadroComoda.grid(row=1, column=1)
    comodaLabel = Label(miFrame, text="Comoda: ")
    comodaLabel.grid(row=1, column=0, sticky="e")

    escritorio = StringVar(miFrame)
    cuadroEscritorio = Entry(miFrame, textvariable=escritorio)
    cuadroEscritorio.grid(row=1, column=1)
    escritorioLabel = Label(miFrame, text="Escritorio: ")
    escritorioLabel.grid(row=1, column=0, sticky="e")

    estanteria = StringVar(miFrame)
    cuadroEstanteria = Entry(miFrame, textvariable=estanteria)
    cuadroEstanteria.grid(row=1, column=1)
    estanteriaLabel = Label(miFrame, text="Estanteria: ")
    estanteriaLabel.grid(row=1, column=0, sticky="e")

    mesa = StringVar(miFrame)
    cuadroMesa = Entry(miFrame, textvariable=mesa)
    cuadroMesa.grid(row=1, column=1)
    mesaLabel = Label(miFrame, text="Mesa: ")
    mesaLabel.grid(row=1, column=0, sticky="e")

    silla = StringVar(miFrame)
    cuadroSilla = Entry(miFrame, textvariable=silla)
    cuadroSilla.grid(row=1, column=1)
    sillaLabel = Label(miFrame, text="Silla: ")
    sillaLabel.grid(row=1, column=0, sticky="e")

    taburete = StringVar(miFrame)
    cuadroTaburete = Entry(miFrame, textvariable=taburete)
    cuadroTaburete.grid(row=1, column=1)
    tabureteLabel = Label(miFrame, text="Mesa: ")
    tabureteLabel.grid(row=1, column=0, sticky="e")

    vitrina = StringVar(miFrame)
    cuadroVitrina = Entry(miFrame, textvariable=vitrina)
    cuadroVitrina.grid(row=1, column=1)
    vitrinaLabel = Label(miFrame, text="Silla: ")
    vitrinaLabel.grid(row=1, column=0, sticky="e")



    def add_venta():
        ced = ci.get()
        armar = armario.get()
        cam = cama.get()
        comod = comoda.get()
        escrit = escritorio.get()
        estant = estanteria.get()
        mes = mesa.get()
        sill = silla.get()
        taburet = taburete.get()
        vitrin = vitrina.get()

        try:
            validar(ci)
            validar(armar)
            validar(cam)
            validar(comod)
            validar(escrit)
            validar(estant)
            validar(mes)
            validar(sill)
            validar(taburet)
            validar(vitrin)

            root.destroy()
        except Exception as e:
            messagebox.askyesno("ERROR", e)

    Button(root, text='Guardar', width=20, bg='white', fg='white', command=add_venta).place(x=120, y=580)
    Button(root, text='Salir', width=20, bg='white', fg='white', command=root.destroy).place(x=360, y=580)

def vista_devolver_mueble():
    root = Toplevel()
    root.title("Devolver Mueble")
    root.geometry('720x650')
    label_0 = Label(root, text="Mueble", width=20, font=("bold", 20))
    label_0.place(x=160, y=20)

    miFrame = Frame(root)
    miFrame.pack()
    miFrame.place(x=100, y=100)


    ci = StringVar(miFrame)
    cuadroCi= Entry(miFrame, textvariable=ci)
    cuadroCi.grid(row=0, column=1)
    ciLabel = Label(miFrame, text="C.I del cliente: ")
    ciLabel.grid(row=0, column=0, sticky="e")

    armario = StringVar(miFrame)
    cuadroArmario = Entry(miFrame, textvariable=armario)
    cuadroArmario.grid(row=0, column=1)
    ArmarioLabel = Label(miFrame, text="Armario: ")
    ArmarioLabel.grid(row=0, column=0, sticky="e")

    cama = StringVar(miFrame)
    cuadroCama = Entry(miFrame, textvariable=cama)
    cuadroCama.grid(row=1, column=1)
    camaLabel = Label(miFrame, text="Cama: ")
    camaLabel.grid(row=1, column=0, sticky="e")

    comoda = StringVar(miFrame)
    cuadroComoda = Entry(miFrame, textvariable=comoda)
    cuadroComoda.grid(row=1, column=1)
    comodaLabel = Label(miFrame, text="Comoda: ")
    comodaLabel.grid(row=1, column=0, sticky="e")

    escritorio = StringVar(miFrame)
    cuadroEscritorio = Entry(miFrame, textvariable=escritorio)
    cuadroEscritorio.grid(row=1, column=1)
    escritorioLabel = Label(miFrame, text="Escritorio: ")
    escritorioLabel.grid(row=1, column=0, sticky="e")

    estanteria = StringVar(miFrame)
    cuadroEstanteria = Entry(miFrame, textvariable=estanteria)
    cuadroEstanteria.grid(row=1, column=1)
    estanteriaLabel = Label(miFrame, text="Estanteria: ")
    estanteriaLabel.grid(row=1, column=0, sticky="e")

    mesa = StringVar(miFrame)
    cuadroMesa = Entry(miFrame, textvariable=mesa)
    cuadroMesa.grid(row=1, column=1)
    mesaLabel = Label(miFrame, text="Mesa: ")
    mesaLabel.grid(row=1, column=0, sticky="e")

    silla = StringVar(miFrame)
    cuadroSilla = Entry(miFrame, textvariable=silla)
    cuadroSilla.grid(row=1, column=1)
    sillaLabel = Label(miFrame, text="Silla: ")
    sillaLabel.grid(row=1, column=0, sticky="e")

    taburete = StringVar(miFrame)
    cuadroTaburete = Entry(miFrame, textvariable=taburete)
    cuadroTaburete.grid(row=1, column=1)
    tabureteLabel = Label(miFrame, text="Mesa: ")
    tabureteLabel.grid(row=1, column=0, sticky="e")

    vitrina = StringVar(miFrame)
    cuadroVitrina = Entry(miFrame, textvariable=vitrina)
    cuadroVitrina.grid(row=1, column=1)
    vitrinaLabel = Label(miFrame, text="Silla: ")
    vitrinaLabel.grid(row=1, column=0, sticky="e")



    def devoluciones():
        armar = armario.get()
        cam = cama.get()
        comod = comoda.get()
        escrit = escritorio.get()
        estant = estanteria.get()
        mes = mesa.get()
        sill = silla.get()
        taburet = taburete.get()
        vitrin = vitrina.get()

        try:
            validar(ci)
            validar(armar)
            validar(cam)
            validar(comod)
            validar(escrit)
            validar(estant)
            validar(mes)
            validar(sill)
            validar(taburet)
            validar(vitrin)

            root.destroy()
            Controller.devolver_mueble(ci,clave,cantidad)
            Controller.devolver_mueble(ci,clave,cantidad)
            Controller.devolver_mueble(ci,clave,cantidad)
            Controller.devolver_mueble(ci,clave,cantidad)
            Controller.devolver_mueble(ci,clave,cantidad)
            Controller.devolver_mueble(ci,clave,cantidad)
            Controller.devolver_mueble(ci,clave,cantidad)
            Controller.devolver_mueble(ci,clave,cantidad)
            Controller.devolver_mueble(ci,clave,cantidad)
            Controller.devolver_mueble(ci,clave,cantidad)
            messagebox.showinfo('Aviso', 'EXITO AL DEVOLVER')
        except Exception as e:
            messagebox.askyesno("ERROR", e)

    Button(root, text='Guardar', width=20, bg='white', fg='white', command=devoluciones).place(x=120, y=580)
    Button(root, text='Salir', width=20, bg='white', fg='white', command=root.destroy).place(x=360, y=580)


def validar(valor):
    if not valor.isdigit():
        raise Exception("Debe ser un valor numerico")

barraMenu = Menu(root)
barraMenu.add_command(label="Devolución", command=vista_devolver_mueble)

menuAgregar = Menu(barraMenu, tearoff=0)
menuAgregar.add_command(label="Agregar Clientes", command=vista_agregar_cliente)
menuAgregar.add_command(label="Agregar Empleado", command=vista_agregar_empleado)
menuAgregar.add_command(label="Aregar Venta", command=vista_agregar_venta)
menuAgregar.add_command(label="Aregar Mueble", command=vista_agregar_mueble)

menuListar = Menu(barraMenu, tearoff=0)
menuListar.add_command(label="Lista de Clientes", command=c.listar_clientes)
menuListar.add_command(label="Lista de Empleados", command=c.listar_empleados)
menuListar.add_command(label="Lista de Muebles", command=c.listar_stock)

barraMenu.add_cascade(label="Agregar", menu=menuAgregar)
barraMenu.add_cascade(label="Listar", menu=menuListar)

root.config(menu=barraMenu)
root.mainloop()

