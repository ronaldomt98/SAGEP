from tkinter import *
from Controller import *
from Bdatos import inicializar_stock
from tkinter import messagebox
from models.Cliente import Cliente
from models.Empleado import Empleado
from models.Armario import Armario
from models.Cama import Cama
from models.Comoda import Comoda
from models.Escritorio import Escritorio
from models.Estanteria import Estanteria
from models.Mesa import Mesa
from models.Silla import Silla
from models.Taburete import Taburete
from models.Vitrina import Vitrina




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

    cedula = IntVar(miFrame)
    cuadroCedula = Entry(miFrame, textvariable=cedula)
    cuadroCedula.grid(row=2, column=1)
    cedulaLabel = Label(miFrame, text="C.I: ")
    cedulaLabel.grid(row=2, column=0, sticky="e")

    ruc = StringVar(miFrame)
    cuadroRuc= Entry(miFrame, textvariable=ruc)
    cuadroRuc.grid(row=3, column=1)
    rucLabel = Label(miFrame, text="Ruc: ")
    rucLabel.grid(row=3, column=0, sticky="e")

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
        rucCliente = ruc.get()
        nom = nombre.get()
        ape = apellido.get()
        dire = direccion.get()
        telef = telefono.get()

        try:
            '''
            validar(ci)
            '''
            nuevoCliente = Cliente(cedula=ci, ruc=rucCliente, nombre=nom, apellido=ape, direccion=dire, contactos=telef)
            agregar_cliente(ci, nuevoCliente)
            messagebox.INFO("Cliente Registrado")
            root.destroy()
        except Exception as e:
            messagebox.askyesno("ERROR", e)

    Button(root, text='Guardar', width=20, bg='white', fg='black', command=add_cliente).place(x=120, y=580)
    Button(root, text='Salir', width=20, bg='white', fg='black', command=root.destroy).place(x=360, y=580)


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
    apellidoLabel = Label(miFrame, text="Apellido: ")
    apellidoLabel.grid(row=1, column=0, sticky="e")

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
    cuadroCargo.grid(row=6, column=1)
    cargoLabel = Label(miFrame, text="Cargo: ")
    cargoLabel.grid(row=6, column=0, sticky="e")

    salario = StringVar(miFrame)
    cuadroSalario = Entry(miFrame, textvariable=salario)
    cuadroSalario.grid(row=7, column=1)
    salarioLabel = Label(miFrame, text="Salario: ")
    salarioLabel.grid(row=7, column=0, sticky="e")

    def add_empleado():
        nomb = nombre.get()
        ci = cedula.get()
        telef = telefono.get()
        dir = direccion.get()
        apell = apellido.get()
        carg = cargo.get()
        sal = salario.get()

        try:
            '''
            validar(ci)
            validar(sal)
            '''
            nuevoEmpleado = Empleado(nombre=nomb, apellido=apell, cedula=ci, direccion=dir,
                                     contactos=telef, cargo=carg, salario=sal)
            agregar_empleado(ci,nuevoEmpleado)
            messagebox.INFO("Empleado Registrado")
            root.destroy()
        except Exception as e:
            messagebox.askyesno("ERROR", e)


    Button(root, text='Registrar', width=20, bg='white', fg='black', command= add_empleado).place(x=120, y=580)
    Button(root, text='Salir', width=20, bg='white', fg='black', command=root.destroy).place(x=360, y=580)

def vista_agregar_mueble():
    root = Toplevel()
    root.title("Agregar Mueble")
    root.geometry('720x650')
    label_0 = Label(root, text="Mueble", width=20, font=("bold", 20))
    label_0.place(x=160, y=20)
    miFrame = Frame(root)
    miFrame.pack()
    miFrame.place(x=100, y=100)

    armario = IntVar(miFrame)
    cuadroArmario= Entry(miFrame, textvariable=armario)
    cuadroArmario.grid(row=0, column=1)
    ArmarioLabel = Label(miFrame, text="Armario: ")
    ArmarioLabel.grid(row=0, column=0, sticky="e")

    cama = IntVar(miFrame)
    cuadroCama= Entry(miFrame, textvariable= cama)
    cuadroCama.grid(row=1, column=1)
    camaLabel = Label(miFrame, text="Cama: ")
    camaLabel.grid(row=1, column=0, sticky="e")

    comoda = IntVar(miFrame)
    cuadroComoda= Entry(miFrame, textvariable= comoda)
    cuadroComoda.grid(row=2, column=1)
    comodaLabel = Label(miFrame, text="Comoda: ")
    comodaLabel.grid(row=2, column=0, sticky="e")

    escritorio = IntVar(miFrame)
    cuadroEscritorio= Entry(miFrame, textvariable= escritorio)
    cuadroEscritorio.grid(row=3, column=1)
    escritorioLabel = Label(miFrame, text="Escritorio: ")
    escritorioLabel.grid(row=3, column=0, sticky="e")

    estanteria = IntVar(miFrame)
    cuadroEstanteria= Entry(miFrame, textvariable= estanteria)
    cuadroEstanteria.grid(row=4, column=1)
    estanteriaLabel = Label(miFrame, text="Estanteria: ")
    estanteriaLabel.grid(row=4, column=0, sticky="e")

    mesa = IntVar(miFrame)
    cuadroMesa= Entry(miFrame, textvariable= mesa)
    cuadroMesa.grid(row=5, column=1)
    mesaLabel = Label(miFrame, text="Mesa: ")
    mesaLabel.grid(row=5, column=0, sticky="e")

    silla = IntVar(miFrame)
    cuadroSilla= Entry(miFrame, textvariable= silla)
    cuadroSilla.grid(row=6, column=1)
    sillaLabel = Label(miFrame, text="Silla: ")
    sillaLabel.grid(row=6, column=0, sticky="e")

    taburete = IntVar(miFrame)
    cuadroTaburete= Entry(miFrame, textvariable= taburete)
    cuadroTaburete.grid(row=7, column=1)
    tabureteLabel = Label(miFrame, text="Mesa: ")
    tabureteLabel.grid(row=7, column=0, sticky="e")

    vitrina = IntVar(miFrame)
    cuadroVitrina = Entry(miFrame, textvariable=vitrina)
    cuadroVitrina.grid(row=8, column=1)
    vitrinaLabel = Label(miFrame, text="Silla: ")
    vitrinaLabel.grid(row=8, column=0, sticky="e")


    def add_mueble():
        armar = int(armario.get())
        cam = int(cama.get())
        comod = int(comoda.get())
        escrit = int(escritorio.get())
        estant = int(estanteria.get())
        mes = int(mesa.get())
        sill = int(silla.get())
        taburet = int(taburete.get())
        vitrin = int(vitrina.get())

        try:
            '''
            validar(armar)
            validar(cam)
            validar(comod)
            validar(escrit)
            validar(estant)
            validar(mes)
            validar(sill)
            validar(taburet)
            validar(vitrin)
            '''
            agregar_mueble(1, armar)
            agregar_mueble(2, cam)
            agregar_mueble(3, comod)
            agregar_mueble(4, escrit)
            agregar_mueble(5, estant)
            agregar_mueble(6, mes)
            agregar_mueble(7, sill)
            agregar_mueble(8, taburet)
            agregar_mueble(9, vitrin)

            messagebox.INFO("Cliente Registrado")
            root.destroy()
        except Exception as e:
            messagebox.askyesno("ERROR", e)

    Button(root, text='Guardar', width=20, bg='white', fg='black', command=add_mueble).place(x=120, y=580)
    Button(root, text='Salir', width=20, bg='white', fg='black', command=root.destroy).place(x=360, y=580)

def vista_agregar_venta():
    root = Toplevel()
    root.title("Agregar venta")
    root.geometry('720x650')
    label_0 = Label(root, text="Venta", width=20, font=("bold", 20))
    label_0.place(x=160, y=20)
    miFrame = Frame(root)
    miFrame.pack()
    miFrame.place(x=100, y=100)

    ci = IntVar(miFrame)
    cuadroCi= Entry(miFrame, textvariable=ci)
    cuadroCi.grid(row=0, column=1)
    ciLabel = Label(miFrame, text="C.I del cliente: ")
    ciLabel.grid(row=0, column=0, sticky="e")

    armario = IntVar(miFrame)
    cuadroArmario = Entry(miFrame, textvariable=armario)
    cuadroArmario.grid(row=1, column=1)
    ArmarioLabel = Label(miFrame, text="Armario: ")
    ArmarioLabel.grid(row=1, column=0, sticky="e")

    cama = IntVar(miFrame)
    cuadroCama = Entry(miFrame, textvariable=cama)
    cuadroCama.grid(row=2, column=1)
    camaLabel = Label(miFrame, text="Cama: ")
    camaLabel.grid(row=2, column=0, sticky="e")

    comoda = IntVar(miFrame)
    cuadroComoda = Entry(miFrame, textvariable=comoda)
    cuadroComoda.grid(row=3, column=1)
    comodaLabel = Label(miFrame, text="Comoda: ")
    comodaLabel.grid(row=3, column=0, sticky="e")

    escritorio = IntVar(miFrame)
    cuadroEscritorio = Entry(miFrame, textvariable=escritorio)
    cuadroEscritorio.grid(row=4, column=1)
    escritorioLabel = Label(miFrame, text="Escritorio: ")
    escritorioLabel.grid(row=4, column=0, sticky="e")

    estanteria = IntVar(miFrame)
    cuadroEstanteria = Entry(miFrame, textvariable=estanteria)
    cuadroEstanteria.grid(row=5, column=1)
    estanteriaLabel = Label(miFrame, text="Estanteria: ")
    estanteriaLabel.grid(row=5, column=0, sticky="e")

    mesa = IntVar(miFrame)
    cuadroMesa = Entry(miFrame, textvariable=mesa)
    cuadroMesa.grid(row=6, column=1)
    mesaLabel = Label(miFrame, text="Mesa: ")
    mesaLabel.grid(row=6, column=0, sticky="e")

    silla = IntVar(miFrame)
    cuadroSilla = Entry(miFrame, textvariable=silla)
    cuadroSilla.grid(row=7, column=1)
    sillaLabel = Label(miFrame, text="Silla: ")
    sillaLabel.grid(row=7, column=0, sticky="e")

    taburete = IntVar(miFrame)
    cuadroTaburete = Entry(miFrame, textvariable=taburete)
    cuadroTaburete.grid(row=8, column=1)
    tabureteLabel = Label(miFrame, text="Mesa: ")
    tabureteLabel.grid(row=8, column=0, sticky="e")

    vitrina = IntVar(miFrame)
    cuadroVitrina = Entry(miFrame, textvariable=vitrina)
    cuadroVitrina.grid(row=9, column=1)
    vitrinaLabel = Label(miFrame, text="Silla: ")
    vitrinaLabel.grid(row=9, column=0, sticky="e")



    def add_venta():
        ced = int(ci.get())
        armar = int(armario.get())
        cam = int(cama.get())
        comod = int(comoda.get())
        escrit = int(escritorio.get())
        estant = int(estanteria.get())
        mes = int(mesa.get())
        sill = int(silla.get())
        taburet = int(taburete.get())
        vitrin = int(vitrina.get())

        try:
            '''
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
            ArmarioObj = Armario(obtener_stock(1).cantidad)
            CamaObj = Cama()
            ComodaObj = Comoda()
            EscritorioObj = Escritorio()
            EstanteriaObj = Estanteria()
            MesaObj = Mesa()
            SillaObj = Silla()
            TabureteObj = Taburete()
            VitrinaObj = Vitrina()
            '''
            agregar_venta(ced,1, armar)
            agregar_venta(ced,2, cam)
            agregar_venta(ced,3, comod)
            agregar_venta(ced,4, escrit)
            agregar_venta(ced,5, estant)
            agregar_venta(ced,6, mes)
            agregar_venta(ced,7, sill)
            agregar_venta(ced,8, taburet)
            agregar_venta(ced,9, vitrin)

            root.destroy()
        except Exception as e:
            messagebox.askyesno("ERROR", e)

    Button(root, text='Guardar', width=20, bg='white', fg='black', command=add_venta).place(x=120, y=580)
    Button(root, text='Salir', width=20, bg='white', fg='black', command=root.destroy).place(x=360, y=580)

def vista_devolver_mueble():
    root = Toplevel()
    root.title("Devolver Mueble")
    root.geometry('720x650')
    label_0 = Label(root, text="Mueble", width=20, font=("bold", 20))
    label_0.place(x=160, y=20)

    miFrame = Frame(root)
    miFrame.pack()
    miFrame.place(x=100, y=100)


    ci = IntVar(miFrame)
    cuadroCi= Entry(miFrame, textvariable=ci)
    cuadroCi.grid(row=0, column=1)
    ciLabel = Label(miFrame, text="C.I del cliente: ")
    ciLabel.grid(row=0, column=0, sticky="e")

    armario = IntVar(miFrame)
    cuadroArmario = Entry(miFrame, textvariable=armario)
    cuadroArmario.grid(row=1, column=1)
    ArmarioLabel = Label(miFrame, text="Armario: ")
    ArmarioLabel.grid(row=1, column=0, sticky="e")

    cama = IntVar(miFrame)
    cuadroCama = Entry(miFrame, textvariable=cama)
    cuadroCama.grid(row=2, column=1)
    camaLabel = Label(miFrame, text="Cama: ")
    camaLabel.grid(row=2, column=0, sticky="e")

    comoda = IntVar(miFrame)
    cuadroComoda = Entry(miFrame, textvariable=comoda)
    cuadroComoda.grid(row=3, column=1)
    comodaLabel = Label(miFrame, text="Comoda: ")
    comodaLabel.grid(row=3, column=0, sticky="e")

    escritorio = IntVar(miFrame)
    cuadroEscritorio = Entry(miFrame, textvariable=escritorio)
    cuadroEscritorio.grid(row=4, column=1)
    escritorioLabel = Label(miFrame, text="Escritorio: ")
    escritorioLabel.grid(row=4, column=0, sticky="e")

    estanteria = IntVar(miFrame)
    cuadroEstanteria = Entry(miFrame, textvariable=estanteria)
    cuadroEstanteria.grid(row=5, column=1)
    estanteriaLabel = Label(miFrame, text="Estanteria: ")
    estanteriaLabel.grid(row=5, column=0, sticky="e")

    mesa = IntVar(miFrame)
    cuadroMesa = Entry(miFrame, textvariable=mesa)
    cuadroMesa.grid(row=6, column=1)
    mesaLabel = Label(miFrame, text="Mesa: ")
    mesaLabel.grid(row=6, column=0, sticky="e")

    silla = IntVar(miFrame)
    cuadroSilla = Entry(miFrame, textvariable=silla)
    cuadroSilla.grid(row=7, column=1)
    sillaLabel = Label(miFrame, text="Silla: ")
    sillaLabel.grid(row=7, column=0, sticky="e")

    taburete = IntVar(miFrame)
    cuadroTaburete = Entry(miFrame, textvariable=taburete)
    cuadroTaburete.grid(row=8, column=1)
    tabureteLabel = Label(miFrame, text="Mesa: ")
    tabureteLabel.grid(row=8, column=0, sticky="e")

    vitrina = IntVar(miFrame)
    cuadroVitrina = Entry(miFrame, textvariable=vitrina)
    cuadroVitrina.grid(row=9, column=1)
    vitrinaLabel = Label(miFrame, text="Silla: ")
    vitrinaLabel.grid(row=9, column=0, sticky="e")



    def devoluciones():
        ced = int(ci.get())
        armar = int(armario.get())
        cam = int(cama.get())
        comod = int(comoda.get())
        escrit = int(escritorio.get())
        estant = int(estanteria.get())
        mes = int(mesa.get())
        sill = int(silla.get())
        taburet = int(taburete.get())
        vitrin = int(vitrina.get())

        try:
            '''
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
            '''
            root.destroy()
            devolver_mueble(ced,1,armar)
            devolver_mueble(ced,2,cam)
            devolver_mueble(ced,3,comod)
            devolver_mueble(ced,4,escrit)
            devolver_mueble(ced,5,estant)
            devolver_mueble(ced,6,mes)
            devolver_mueble(ced,7,sill)
            devolver_mueble(ced,8,taburet)
            devolver_mueble(ced,9,vitrin)

            messagebox.showinfo('Aviso', 'EXITO AL DEVOLVER')
        except Exception as e:
            messagebox.askyesno("ERROR", e)

    Button(root, text='Guardar', width=20, bg='white', fg='black', command=devoluciones).place(x=120, y=580)
    Button(root, text='Salir', width=20, bg='white', fg='black', command=root.destroy).place(x=360, y=580)


def vista_mostrar_cliente(cliente):
    ventanaAbrir = Toplevel()
    ventanaAbrir.geometry("400x400+100+100")
    ventanaAbrir.title("Listado de Clientes")
    texto = Text(ventanaAbrir, height=720, width=480)
    texto.insert(INSERT, 'Nombre: ' + str(cliente.nombre) + '\n' + 'Apellido: ' + str(
        cliente.apellido) + '\n' + 'Direccion: ' + str(cliente.direccion) + '\n' + 'Ruc: ' + str(
        cliente.ruc) + '\n' + 'Telefono: ' + str(cliente.contacto) + '\n')
    texto.pack()


def vista_listar_clientes():
    ventanaAbrir = Toplevel()
    ventanaAbrir.geometry("400x400+100+100")
    ventanaAbrir.title("Listado de Clientes")
    texto = Text(ventanaAbrir, height=720, width=480)
    listaDeClientes = listar_clientes()
    for cliente in listaDeClientes:
        texto.insert(INSERT, 'Nombre: ' + str(cliente.nombre) + '\n' + 'Apellido: ' + str(
            cliente.apellido) + '\n' + 'Direccion: ' + str(cliente.direccion) + '\n' + 'Ruc: ' + str(
            cliente.ruc) + '\n' + 'Telefono: ' + str(cliente.contactos) + '\n\n')
        texto.pack()


def vista_listar_empleados():
    ventanaAbrir = Toplevel()
    ventanaAbrir.geometry("400x400+100+100")
    ventanaAbrir.title("Listado de Empleados")
    texto = Text(ventanaAbrir, height=720, width=480)
    listaDeEmpleados = listar_empleados()
    for empleado in listaDeEmpleados:
        texto.insert(INSERT, 'Nombre: ' + empleado.nombre + '\n' +'Apellido: ' + empleado.apellido + '\n' + 'Telefono: ' +
            empleado.contactos + '\n' + 'Direccion: ' + empleado.direccion + '\n' + 'CI: ' +
            empleado.cedula + '\n') + '\n' + 'Cargo: '+ empleado.cargo + '\n'\
            + 'Salario: ' + empleado.salario
        texto.pack()


def vista_mostrar_muebles():
    ventanaAbrir = Toplevel()
    ventanaAbrir.geometry("400x450+100+100")
    ventanaAbrir.title("Listado de Muebles")
    texto = Text(ventanaAbrir, height=720, width=480)
    '''
    listaMuebles = []
    listaMuebles.append(listar_stock(1))
    listaMuebles.append(listar_stock(2))
    '''
    for i in range(1,10):
        mueble = listar_stock(i)
        texto.insert(INSERT,
                     'Nombre: ' + mueble.nombre + '\n' + 'Cantidad: ' + str(mueble.cantidad) + '\n\n')
        texto.pack()
'''
def validar(valor):
    if not valor.isdigit():
        raise Exception("Debe ser un valor numerico")
'''