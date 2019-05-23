from persistent import Persistent


class Cliente(Persistent):
    muebles = []
    clave = "cliente"

    def get_clave(self):
        return self.clave

    def __init__(self, persona, ruc, muebles):
        self.persona = persona
        self.ruc = ruc
        self.muebles = muebles

    def obtener_ruc(self):
        return self.ruc

    def obtener_muebles(self):
        return self.muebles

    def comprar(self, bien):
        self.muebles.append(bien)

    def __str__(self):
        return '\nPersona: ' + str(self.muebles) + '\nRUC: ' + self.ruc + '\nMuebles:\n' + str(self.muebles)
