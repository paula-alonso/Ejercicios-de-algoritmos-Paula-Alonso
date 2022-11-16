from producto import Producto, Flores, Semillas
from vendedor import Vendedor
def main():
    products = [{ "id": 1, "name": "Rose", "type": "flower", "stock": 160, "colors": ["red", "white", "pink"] },
    { "id": 2, "name": "Tulip", "type": "flower", "stock": 34, "colors": ["white", "yellow"] },
    { "id": 3, "name": "Sunflower seeds", "type": "seeds", "stock": 50 },
    { "id": 4, "name": "Sunflower", "type": "flower", "stock": 77, "colors": ["yellow"] },
    { "id": 5, "name": "Lavender seeds", "type": "seeds", "stock": 100, "colors": ["purple"] },
    { "id": 6, "name": "Carnation", "type": "flower", "stock": 89, "colors": ["yellow", "burgundy", "purple", "pink", "red", "white"] },
    ]
    vendor_1 = [
    { "product_id": 5, "customer_id": 333, "amnt": 1 },
    { "product_id": 5, "customer_id": 1010, "amnt": 2 },
    { "product_id": 3, "customer_id": 1111, "amnt": 3 },
    { "product_id": 2, "customer_id": 222, "amnt": 6 },
    { "product_id": 6, "customer_id": 444, "amnt": 7 },
    { "product_id": 1, "customer_id": 1111, "amnt": 20 },
    ]
    
    vendor_2 = [
    { "product_id": 6, "customer_id": 888, "amnt": 10 },
    { "product_id": 1, "customer_id": 123, "amnt": 5 },
    { "product_id": 2, "customer_id": 321, "amnt": 4 },
    { "product_id": 4, "customer_id": 555, "amnt": 2 },
    { "product_id": 1, "customer_id": 777, "amnt": 1 },
    ]
    lista_objetos = []
    todos_vendedores = vendor_1+vendor_2
    vendedor_obj = []
    for elemento in products:
        if elemento["type"] == "flower":
            flor = Flores(elemento["id"], elemento["name"], elemento["type"], elemento["stock"], elemento["colors"])
            lista_objetos.append(flor)
        else:
            if "colors" in elemento.keys():
                semilla = Semillas(elemento["id"], elemento["name"], elemento["type"], elemento["stock"], elemento["colors"])
                lista_objetos.append(semilla)
            else:
                semilla = Semillas(elemento["id"], elemento["name"], elemento["type"], elemento["stock"], None)
                lista_objetos.append(semilla) 
    while True:
        option = input("¡Bienvenido! ¿Qué deseas hacer?\n1. Agregar productos\n2. Ver productos\n3.Salir\n")
        if option == "1":
            for elemento in products:
                if elemento["type"] == "flower":
                    flor = Flores(elemento["id"], elemento["name"], elemento["type"], elemento["stock"], elemento["colors"])
                    lista_objetos.append(flor)
                else:
                    for elemento in products:
                        if "colors" in elemento.keys():
                            semilla = Semillas(elemento["id"], elemento["name"], elemento["type"], elemento["stock"], elemento["colors"])
                            lista_objetos.append(semilla)
                        else:
                            semilla = Semillas(elemento["id"], elemento["name"], elemento["type"], elemento["stock"], None)
                            lista_objetos.append(semilla) 
        if option == "2":
            for elemento in lista_objetos:
                elemento.mostrar()
        if option == "3":
            break
    i = 0
    while i < len(todos_vendedores):
        for element in todos_vendedores: 
            if i == element["amnt"]:
                vendedor = Vendedor(element["product_id"], element["customer_id"], element["amnt"])
                vendedor_obj.append(vendedor)
        i+=1
    
    for elemento in lista_objetos:
        for element in vendedor_obj:
            if elemento.id == element.product:
                elemento.stock= elemento.stock - element.amnt

    for elemento in lista_objetos:
        elemento.mostrar()
main()