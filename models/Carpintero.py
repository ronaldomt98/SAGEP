class Carpintero:
    clave = "carpintero"

    def get_clave(self):
        return self.clave

    def __init__(self, empleado):
        self.empleado = empleado

    def fabricar_mueble(self, bien, cantidad):
        pass

    def __str__(self):
        return str(self.empleado)
