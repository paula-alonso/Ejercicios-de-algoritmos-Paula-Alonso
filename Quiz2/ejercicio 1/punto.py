class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def ObtenerPunto(self):
        x = self.x
        y = self.y
        return x, y
    def Cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "El punto pertenece al primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "El punto pertenece al segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "El punto pertenece al tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "El punto pertenece al cuarto cuadrante"
        else:
            return "El punto es el origen"