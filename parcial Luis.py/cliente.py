class Cliente:
    def __init__(self, nombre, edad, ci):
        self.nombre = nombre
        self.edad = edad
        self.ci = ci

class Factura(Cliente):
    def __init__(self, nombre, edad, ci, lista_compras, descuento, total):
        super().__init__(nombre, edad, ci)
        self.lista_compras = lista_compras
        self.descuento = descuento
        self.total = total