from .Contacto import Contacto


class Email(Contacto):
    clave = "email"

    def get_clave(self):
        return self.clave

    def __init__(self, correo):
        super(Email, self).__init__()
        self.correo = correo

    def __str__(self):
        return '\nEmail: ' + self.correo
