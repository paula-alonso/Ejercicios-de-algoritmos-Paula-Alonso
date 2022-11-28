class AnuncioComercial:
    def __init__(self, imagen, seccion):
        self.imagen = imagen
        self.seccion = seccion

class AnuncioClasificado:
    def __init__(self, precio, fecha_pub, dias, tipo):
        self.precio = precio
        self.fecha_publicacion = fecha_pub
        self.dias = dias
        self.tipo = tipo

class AnuncioClasificadoVehiculo(AnuncioClasificado):
    def __init__(self, precio, fecha_pub, dias, marca, modelo, año, color, kilo):
        super().__init__(precio, fecha_pub, dias, "Vehículo")
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.kilometraje = kilo

class AnuncioClasificadoVivienda(AnuncioClasificado):
    def __init__(self, precio, fecha_pub, dias, metros, cuartos, baños, puestos, politica):
        super().__init__(precio, fecha_pub, dias, "Vivienda")
        self.metros_cuadrados = metros
        self.cantidad_cuartos = cuartos
        self.cantidad_baños = baños
        self.cantidad_puestos = puestos
        self.politica_adicional = politica