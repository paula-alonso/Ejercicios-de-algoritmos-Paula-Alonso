class Personal:
    def __init__(self, nombre, ci, tipo, horas, monto):
        self.nombre = nombre
        self.ci = ci
        self.tipo = tipo
        self.horas = horas
        self.monto = monto
    
    def Mostrar(self):
        print("****PERSONAL****")
        print(f"Nombre: {self.nombre}\nCI: {self.ci}\nTipo: {self.tipo}\nHoras de trabajo: {self.horas}\nMonto: {self.monto}")
