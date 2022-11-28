class Cliente:
    def __init__(self, nombre, edad, ci):
        self.nombre = nombre
        self.edad = edad
        self.ci = ci

    def MostrarCliente(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nCI: {self.ci}\n")

    