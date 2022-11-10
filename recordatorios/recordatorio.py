from tarea import Tarea
class Recordatorio(Tarea):
    def __init__(self, nombre, hora, dia, mes, descripcion):
        super().__init__(descripcion)
        self.nombre = nombre
        self.hora = hora
        self.dia = dia
        self.mes = mes

    def mostrar(self):
        print(f"Nombre: {self.nombre}\nHora:{self.hora}\nFecha:{self.dia}/{self.mes}")
        for elemento in self.descripcion:
            elemento.mostrarTarea()
