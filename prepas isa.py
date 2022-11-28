from unicodedata import name


products = {
    "mobiles": {
        "Apple": [
            {
                "id": 1,
                "name": "iPhone 7",
                "price": 300
            },
            {
                "id": 2,
                "name": "iPhone 8",
                "price": 350
            },
            {
                "id": 3,
                "name": "iPhone Xr",
                "price": 450
            },
            {
                "id": 4,
                "name": "iPhone Xs",
                "price": 460
            },
            {
                "id": 5,
                "name": "iPhone 11",
                "price": 900
            },
            {
                "id": 6,
                "name": "iPhone 12",
                "price": 1100
            },
            {
                "id": 7,
                "name": "iPhone 13",
                "price": 1300
            },
        ],
        "Samsung": [
            {
                "id": 8,
                "name": "Samsung Galaxy Beam",
                "price": 150
            },
            {
                "id": 9,
                "name": "Samsung Galaxy S6",
                "price": 200
            },
            {
                "id": 10,
                "name": "Samsung Galaxy S7",
                "price": 300
            },
        ],
        "Xiaomi": [
            {
                "id": 11,
                "name": "Xiaomi Redmi Note 8",
                "price": 250
            },
            {
                "id": 12,
                "name": "Xiaomi Redmi Note 8 Pro",
                "price": 300
            },
        ]
    },
    "laptops": {
        "DELL": [
            {
                "id": 13,
                "name": "Dell Inspiron 15",
                "price": 600
            },
            {
                "id": 14,
                "name": "Dell Latitude 14",
                "price": 650
            },
        ],
        "MAC": [
            {
                "id": 15,
                "name": "MacBook Pro 13",
                "price": 900
            },
            {
                "id": 16,
                "name": "MacBook M1",
                "price": 1500
            },
        ]
    },
}

    



option = ""
while option != "3":
    print("Bienvenido!")
    option = input("¿Qué deseas hacer? Selecciona el número que corresponda?\n1. Ver inventario.\n2. Registrar compra.\n3. Salir.\n")
    if option == "1":
        categories = {1 : "mobiles", 2: "laptos"}
        category = int(input("Introduce una categoría: \n1. Moviles\n2. Computadoras"))
        for type, brands in products.items():
            if type == categories.get(category):
                for brand, list_of_products in brands.items():
                    print(brand)
                    for product in list_of_products:
                        id = product.get("id")
                        names = product.get("name")
                        price = product.get("price")
                        print(f"{id},{names},{price}")
    if option == "2":
        product_id = int(input("Introduce el id del prodicto que quieres: "))
        product_selected = None
        for type, brands in products.items():
                for brand, list_of_products in brands.items():
                    for product in list_of_products:
                        if product.get("id") == product_id:
                            product_selected = product
                            break
        if product_selected:
            client = {"name" : input("Introduce tu nombre: "), "CI": input("Introduce tu cédula: "), "Product_id":product_id}
            print("<<<<<<Factura>>>>>>")
            for key , value in client.items():
                if key != "Product_id":
                    print(key, value)
            for key, value in product_selected.items():
                print(key, value)
        else:
            print("Producto no encontrado")



print("Gracias por preferirnos!")

