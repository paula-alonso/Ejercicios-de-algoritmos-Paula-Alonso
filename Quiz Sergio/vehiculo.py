class Vehiculo:
    def __init__(self, placa, marca, puesto, hora_e):
        self.placa = placa
        self.marca = marca
        self.puesto = puesto
        self.hora_entrada = hora_e
        self.hora_salida = None

class Automovil(Vehiculo):
    def __init__(self, placa, marca, puesto, hora_e, minusvalido):
        super().__init__(placa, marca, puesto, hora_e)
        self.minusvalido = minusvalido
    def mostrar(self):
        if self.hora_salida==None:
            print(f"\nPlaca: {self.placa}\nMarca: {self.marca}\nPuesto: {self.puesto}\nHora de entrada: {self.hora_entrada}\nMinusvalido: {self.minusvalido}")
        else:
            print(f"\nPlaca: {self.placa}\nMarca: {self.marca}\nHora de salida: {self.hora_salida}\nMinusvalido: {self.minusvalido}")
class Motocicleta(Vehiculo):
    def __init__(self, placa, marca, puesto, hora_e):
        super().__init__(placa, marca, puesto, hora_e)
    def mostrar(self):
        if self.hora_salida==None:
            print(f"\nPlaca: {self.placa}\nMarca: {self.marca}\nPuesto: {self.puesto}\nHora de entrada: {self.hora_entrada}")
        else:
            print(f"\nPlaca: {self.placa}\nMarca: {self.marca}\nHora de salida: {self.hora_salida}")


