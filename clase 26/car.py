from main1 import Vehicle
class Car(Vehicle):
    def __init__(self, color, wheels, speed, cilindrada):
        super().__init__(self, color, wheels)
        self.speed = speed
        self.cilindrada = cilindrada
class Camioneta (Car):
    def __init__(self, color, wheels, speed, cilindrada, carga):
        super().__init__(color, wheels, speed, cilindrada)
        self.carga = carga