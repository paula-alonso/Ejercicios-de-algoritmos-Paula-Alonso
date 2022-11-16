class Pedido:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def ObtenerMonto(self):
        monto = int(self.precio)
        return monto
class Comida(Pedido):
    def __init__(self, nombre, precio, tipo, platillo):
        super().__init__(nombre, precio)
        self.tipo = tipo
        self.platillo = platillo
    def GuardarComida(self):
        orden = {"Nombre": self.nombre, "Precio": self.precio, "Tipo": self.tipo, "Platillo": self.platillo}
        return orden
class Bebida(Pedido):
    def __init__(self, nombre, precio, porcentaje, temp):
        super().__init__(nombre, precio)
        self.porcentaje = porcentaje
        self.temp = temp
    def GuardarBebida(self):
        orden = {"Nombre": self.nombre, "Precio": self.precio, "% Alcohol": self.porcentaje, "Temperatura":self.temp}
        return orden