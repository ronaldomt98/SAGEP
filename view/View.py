from models.Cliente import Cliente
from models.Persona import Persona

'''Valida que un valor ingresado este entre cierto rango de valores'''
def input_rango(text, men, may):
    while True:
        valor = input("{} [{}] al [{}] >>> ".format(text, men, may))
        try:
            valor = int(valor)
            if (valor <= may and valor >= men):
                return valor
            else:
                raise (ValueError)
        except ValueError:
            print("\n[" + str(valor) + "] NO ES UNA DE LAS OPCIONES OFRECIDAS :(\n\t VUELVA A INTENTARLO ;)\n")




class View():


    def leer_cedula(self):
        cedula = input("Ingrese el numero de documento de la persona a buscar: ")
        return cedula


    def imprimir_en_pantalla(self, resultado):
        print('La persona encontrada es: {}'.format(resultado))


    def vista_agregar_cliente(self):
        print("Crear nuevo cliente")
        cedula = input("Ingrese documento del nuevo cliente: ")
        nombre = input("Ingrese nombre del nuevo cliente: ")
        apellido = input("Ingrese apellido del nuevo cliente: ")
        nueva_persona = Persona(nombre, apellido, cedula, 'No especificada', None)
        opcion = input("Agregar ruc (s/n):").lower
        if (opcion == 's'):
            ruc = input("Ingrese ruc del nuevo cliente: ")
            nuevo_cliente = Cliente(ruc, nueva_persona)
        else:
            nuevo_cliente = Cliente(None, nueva_persona)
        return nuevo_cliente


    def vista_listar_clientes(self, lista_clientes):
        print ("Listado de personas en la base de datos: \n")
        if lista_clientes:
            for cliente in lista_clientes:
                print(
                    'Nombre: {}; Apellido: {}; Documento: {}.'.format(cliente.nombre, cliente.apellido,
                                                                    cliente.cedula))


    def vista_agregar_mueble(self):
        print ("Agregar nuevo mueble")


    def vista_devolver_mueble(self):
        pass


    def vista_vender(self):
        pass

