
#Le agregué un atributo a la clase electrodoméstico
class Electrodomestico:
    def __init__(self, type, codigo_producto, precio, marca, color):
        self.type = type
        self.codigo_producto = codigo_producto
        self.precio = precio
        self.marca = marca
        self.color = color
    def mostrar(self):
        print(f"Nombre del producto: {self.type}\nCódigo del producto: {self.codigo_producto}\nPrecio: {self.precio}\nMarca: {self.marca}\nColor: {self.color}")

class Lavadora(Electrodomestico):
    def __init__(self, type, codigo_producto, precio, marca, color, capacidad):
        super().__init__(type, codigo_producto, precio, marca, color)
        self.capacidad = capacidad
    def mostrar(self):
        super().mostrar()
        print(f"Capacidad: {self.capacidad}")

class Horno(Electrodomestico):
    def __init__(self, type, codigo_producto, precio, marca, color, control):
        super().__init__(type, codigo_producto, precio, marca, color)
        self.control = control
    def mostrar(self):
        super().mostrar()
        print(f"Control: {self.control}")

class Nevera(Electrodomestico):
    def __init__(self, type, codigo_producto, precio, marca, color, inc_congelador, compartimentos):
        super().__init__(type, codigo_producto, precio, marca, color)
        self.inc_congelador = inc_congelador
        self.compartimentos = compartimentos
    def mostrar(self):
        super().mostrar()
        print(f"Incluye congelador: {self.inc_congelador}\nCompartimentos: {self.compartimentos}")

class Licuadora(Electrodomestico):
    def __init__(self, type, codigo_producto, precio, marca, color, material_vaso, velocidades):
        super().__init__(type, codigo_producto, precio, marca, color)
        self.material_vaso = material_vaso
        self.velocidades = velocidades
    def mostrar(self):
        super().mostrar()
        print(f"Material del vaso: {self.material_vaso}\nVelocidades: {self.velocidades}")