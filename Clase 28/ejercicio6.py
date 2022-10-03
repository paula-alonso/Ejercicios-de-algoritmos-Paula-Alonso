data = {}
aux = 0
while True:
    key_name = input("Introduzca los datos que quiere almacenar: ")
    value = input("Introduzca el valor: ")
    data[key_name] = value
    for key, value in data.items():
        print(f"Tu {key} es {value}")
    salir = input("salir? ")
    if salir == "si":
        break
