class Trabajador:
    def __init__(self, nombre, apellido, ci, tipo, num_horas, mes, especialidad, sueldo_f):
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
        self.tipo = tipo
        self.num_horas = num_horas
        self.mes = mes
        self.especialidad = especialidad
        self.sueldo_f = sueldo_f

    def Mostrar(self):
        print(f"Nombre: {self.nombre}\nApellido: {self.apellido}\nCI: {self.ci}\nTipo: {self.tipo}\nNúmero de horas trabajadas: {self.num_horas}\nMes: {self.mes}\nEspecialidad: {self.especialidad}\nSueldo: {self.sueldo_f}")
        