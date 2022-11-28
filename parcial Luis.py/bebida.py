class Bebida:
    def __init__(self, tipo, nombre, precio):
        self.tipo = tipo
        self.nombre = nombre
        self.precio = precio
    def Mostrar(self):
       print(f"Nombre: {self.nombre}\nPrecio: {self.precio}") 

class Aloholica(Bebida):
    def __init__(self, tipo, nombre, precio, grado_alcoholico):
        super().__init__(tipo, nombre, precio)
        self.grado_alcoholico = grado_alcoholico
    def Mostrar(self):
        super().Mostrar()
        print(f"Grado de alcohol: {self.grado_alcoholico}")

class NoAlcoholica(Bebida):
    def __init__(self, tipo, nombre, precio, temperatura):
        super().__init__(tipo, nombre, precio)
        self.temperatura = temperatura
    
    def Mostrar(self):
        super().Mostrar()
        print(f"Temperatura: {self.temperatura}")