class Bebida:
    def __init__(self, nombre, tipo, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
    def Mostrar(self):
        print(f"Nombre: {self.nombre}\nPrecio: {self.precio}")
    
class Alcoholica(Bebida):
    def __init__(self, nombre, tipo, precio, g_al):
        super().__init__(nombre, tipo, precio)
        self.grado_al = g_al
    def Mostrar(self):
        super().Mostrar()
        print(f"Grado de alcohol: {self.grado_al}")
class NoAlcoholica(Bebida):
    def __init__(self, nombre, tipo, precio, temp):
        super().__init__(nombre, tipo, precio)
        self.temp = temp
    def Mostrar(self):
        super().Mostrar()
        print(f"Temperatura: {self.temp}")