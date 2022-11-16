from main1 import Vehicle
class Bicicleta (Vehicle):
    def __init__(self, color, wheels, tipo):
        super().__init__(color, wheels)
        self.tipo = tipo  
class Motoclicleta(Bicicleta):
    def __init__(self, color, wheels, tipo, speed, cilindrada):
        super().__init__(color, wheels, tipo)
        self.speed = speed
        self.cilindrada = cilindrada