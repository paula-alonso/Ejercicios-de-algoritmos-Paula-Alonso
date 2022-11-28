class Bebida:
    def __init__(self, nombre, tipo, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio

    def MostrarBebida(self):
        print(f"Nombre: {self.nombre}\nPrecio: {self.precio}$")
    
class Alcoholica(Bebida):
    def __init__(self, nombre, tipo, precio, grado_alcohol):
        super().__init__(nombre, tipo, precio)
        self.grado_alcohol = grado_alcohol
    
    def MostrarBebida(self):
        super().MostrarBebida()
        print(f"Grado de alcohol: {self.grado_alcohol}")

class NoAlcoholica(Bebida):
    def __init__(self, nombre, tipo, precio, temperatura):
        super().__init__(nombre, tipo, precio)
        self.temperatura = temperatura

    def MostrarBebida(self):
        super().MostrarBebida()
        print(f"Temperatura: {self.temperatura}")


