from bebida import Bebida, Alcoholica, NoAlcoholica
class Compra:
    def __init__(self, bebida, cantidad):
        self.bebida = bebida
        self.cantidad = cantidad

    def MostrarCompra(self):
        self.bebida.MostrarBebida()
        print(f"Cantidad: {self.cantidad}")
    
    def CalcularMonto(self):
        return self.bebida.precio * self.cantidad


