class Compra:
    def __init__(self, bebida, cantidad, monto):
        self.bebida = bebida
        self.cantidad = cantidad
        self.monto = monto
    def MostrarCompra(self):
        self.bebida.Mostrar()
        print(f"Cantidad de bebidas: {self.cantidad}")