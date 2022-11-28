from books import Books
from clients import Client
def main():
    available_books = []
    db = []
    while True:
        print("Bienvenido")
        user = input("¿Qué deseas hacer? Elige la opción correspondiente:\n1. Préstamo\n2. Comprar libro\n3. Incorporar nuevo libro\n4. Eliminar libro")
        if user == "1":
            libro = Books(input("Introduce el nombre del libro: "), input("Introduce el género del libro que desea: "))
            libro = Books.UsarLibro(libro)
            if libro in available_books:
                print("Libro encontrado")
                clients = Client(input("Introduzca su nombre: "), input("Introduzca su cédula: ")) 
                clients = Client.GuardarCliente(clients)
                db.append(clients)
            print(db)
        if user == "3":
            libro = Books(input("Introduce el nombre del libro: "), input("Introduce el género del libro que desea: "))
            available_books.append(Books.UsarLibro(libro))
            print(available_books)
main()