class Alimento:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Comida(Alimento):
    def __init__(self, nombre, precio, tipo_sabor, tipo_platillo):
        super().__init__(nombre, precio)
        self.tipo_sabor = tipo_sabor
        self.tipo_platillo = tipo_platillo
    def imprimir(self):
        order = [self.nombre, self.precio, self.tipo_sabor, self.tipo_platillo]
        return order

class Bebida(Alimento):
    def __init__(self, nombre, precio, por_alch, temp):
        super().__init__(nombre, precio)
        self.porcentaje_alcohol = por_alch
        self.temperatura = temp
    def imprimir(self):
        order = [self.nombre, self.precio, self.porcentaje_alcohol, self.temperatura]
        return order
