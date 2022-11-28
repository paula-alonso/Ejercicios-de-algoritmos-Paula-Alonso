class Persona:
    def __init__(self, nombre, apellido, fecha_na, ci, cuenta):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_na
        self.ci = ci
        self.cuenta = cuenta
    def imprimir (self):
        cliente = [self.nombre, self.apellido, self.fecha_nacimiento, self.ci, self.cuenta]
        return cliente
