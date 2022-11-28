from article import Article
import random
class Redactores:
    def __init__(self, nombre, ci):
        self.nombre = nombre
        self.ci = ci
    def escribir_articulo(self):
        print("Estoy escribiendo un artículo")
        articulo = Article(input("Titulo "), input("Resumen "), input("Cuerpo "))
        print("Terminé de escribir el artículo")
        return articulo
class Jefes(Redactores):
    def __init__(self, nombre, ci, lista_redactores):
        super().__init__(nombre, ci)
        self.lista_redactores = lista_redactores
    def supervisar(self):
        print("Todo está bien")
    def decidir(self, articulo):
        if random.ran
        print("El artículo fue aprobado", articulo)


        