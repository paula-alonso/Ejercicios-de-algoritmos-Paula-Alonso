from electrodomestico import Electrodomestico, Lavadora, Licuadora, Nevera, Horno

def get_list_products(edd):
    list_products = []
    for key, value in edd.items():
        if key == "washer":
            for element in value:
                lavadora = Lavadora(key, element["cod_p"], element["price"],element["brand"],element["color"], element["capacity"])
                list_products.append(lavadora)   
        if key == "microwave":
            for element in value:
                horno = Horno(key, element["cod_p"], element["price"],element["brand"],element["color"], element["digital"])
                list_products.append(horno)  
        if key == "fridge":
            for element in value:
                nevera = Nevera(key, element["cod_p"], element["price"],element["brand"],element["color"], element["cooler"], element["comp"] )
                list_products.append(nevera)
        if key == "blender": 
            for element in value:
                licuadora = Licuadora(key, element["cod_p"], element["price"],element["brand"],element["color"], element["cup"], element["speeds"] )
                list_products.append(licuadora) 
    return list_products
def mostrar_productos(list_products):
    i = 1
    for producto in list_products:
        print(i,".")
        producto.mostrar()
        i += 1

def main():
    edd = {
    "washer":
    [
        {"cod_p": "AEX-200918", "price": 551.99, "brand": "Whirlpool", "color": "Blanca", "capacity": 17},
        {"cod_p": "GHT-191214", "price": 409.00, "brand": "LG", "color": "Gris", "capacity": 15}
    ],
    "microwave":
    [
        {"cod_p": "FGE-220708", "price": 109.01, "brand": "Daewoo", "color": "Blanco", "digital": False},
        {"cod_p": "PEP-210123", "price": 201.50, "brand": "Frigilux", "color": "Negro", "digital": True}
    ],
    "fridge":
    [
        {"cod_p": "HYW-180909", "price": 280.98, "brand": "Electrolux", "color": "Plateado", "cooler": False, "comp": 5},
        {"cod_p": "IUO-201020", "price": 405.99, "brand": "Samsung", "color": "Azul pastel y rosado", "cooler": True, "comp": 8}
    ],
    "blender":
    [
        {"cod_p": "OWO-191111", "price": 42.05, "brand": "Oster", "color": "Plateado", "cup": "Cristal", "speeds": 3},
        {"cod_p": "XAT-221230", "price": 17.99, "brand": "Philips", "color": "Blanco", "cup": "Plastico", "speeds": 2}
    ]
}
    list_products = get_list_products(edd)
    list_borrados = []
    while True:
        option = input("Bienvenido ¿Qué deseas hacer?\n1. Ver inventario\n2. Borrar un producto defectuoso\n3. Salir\n")
        if option != "1" and option != "2" and option != "3":
            print("Cifra inválida")
        if option == "1":
            mostrar_productos(list_products)
        if option == "2":
            mostrar_productos(list_products)
            borrar = int(input("Introduce el número que corresponda al producto que quieras borrar: "))
            list_borrados.append(list_products[borrar-1])
            list_products.pop(borrar-1)
        if option == "3":
            break   
main()