class Persona:
    def __init__(self, nombre, apellido, fecha_na, ci, cuenta):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_na
        self.ci = ci
        self.cuenta = cuenta
    def GuardarPersona(self):
        cliente ={"Nombre": self.nombre,
        "Apellido": self.apellido, "Fecha de nacimiento": self.fecha_nacimiento,
        "CI": self.ci, "Cuenta": self.cuenta}
        return cliente