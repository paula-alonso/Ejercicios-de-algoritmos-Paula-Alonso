from bebida import Bebida, Aloholica, NoAlcoholica
from compra import Compra
from cliente import Cliente
def main():
    bebidas = [{"Descripción": "Coca-Cola", "Precio": 2, "Temperatura": 15}, {"Descripción": "Cerveza", "Precio": 1.5, "Grado de Alcohol": 9}, {"Descripción": "Red Bull", "Precio": 3, "Temperatura": 10}]
    lista_bebidas = []
    for elemento in bebidas:
        if "Grado de Alcohol" in elemento.keys():
            bebida = Aloholica("Alcoholica", elemento["Descripción"], elemento["Precio"], elemento["Grado de Alcohol"] )
            lista_bebidas.append(bebida)
        else:
            bebida = NoAlcoholica("No Alcoholica", elemento["Descripción"], elemento["Precio"], elemento["Temperatura"] )
            lista_bebidas.append(bebida)
    while True:
        print("*****BIENVENIDO A SAMAN BAR*****")
        option = input("¿Qué deseas hacer? Selecciona la opción que corresponda:\n1. Registrar nueva bebida\n2. Realizar compra\n3. Salir\n---->")
        if option == "1":
            tipo = input("¿Qué tipo de bebida desea agregar?\n1. Alcoholica\n2. No alcoholica\n--->")
            if tipo == "1":
                bebida_user = Aloholica( "Alcoholica", input("Introduzca el nombre: "), int(input("Introduzca el precio: ")), int(input("Introduzca el grado de alcohol: ")))
            if tipo == "2":
                bebida_user = NoAlcoholica("No Alcohoica", input("Introduzca el nombre: "), int(input("Introduzca el precio: ")), int(input("Introduzca la temperatura: ")))
            print("*******BEBIDAS DISPONIBLES******")
            for bebida in lista_bebidas:
                print("")
                bebida.Mostrar()
        if option == "2":
            lista_compras = []
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            ci = input("CI: ")
            cliente = Cliente(nombre, edad, ci)
            while True:
                i = 1
                print("*******BEBIDAS DISPONIBLES******")
                for bebida in lista_bebidas:
                    if edad < 18:
                        if bebida.tipo == "No Alcohoica":
                            print(i, ".")
                            bebida.Mostrar()
                    i += 1
                bebida_index = int(input("¿Qué bebida desea? Introduzca la opción que corresponda: "))
                cant = int(input("Introduzca la cantidad que desea: "))
                for bebida in lista_bebidas:
                    if bebida == lista_bebidas[bebida_index-1]:
                        compra = Compra(bebida, cant)
                        lista_compras.append(compra)
                salida = input("¿Desea otra bebida?\n1. Sí\n2. No\n---->")
                if salida == "2":
                    break
            
            
        if option == "3":
            break
main()