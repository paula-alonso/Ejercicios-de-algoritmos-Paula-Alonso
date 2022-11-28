from bebida import Bebida, Alcoholica, NoAlcoholica
from compra import Compra
from cliente import Cliente

def get_fibo(edad, a, b):
    z = a + b
    if a > edad:
        return False
    if b == edad or a == edad:
        return True
    b = a
    a = z
    return get_fibo(edad, a, b)

def get_primo (edad, c):
    if c == 1:
        return True
    if edad % c == 0:
        return False
    return get_primo(edad, c-1)


def main():
    bebidas = [{"Nombre": "Coca-Cola", "Precio": 2, "Temperatura": 10}, {"Nombre": "Cerveza", "Precio": 1.5, "Grado al": 5}, {"Nombre": "Red Bull", "Precio": 3, "Temperatura": 15}]
    lista_beb = []
    for bebida in bebidas:
        if bebida["Nombre"] == "Cerveza":
            bebida = Alcoholica(bebida["Nombre"], "Alcoholica",  bebida["Precio"], bebida["Grado al"])
        else:
            bebida = NoAlcoholica(bebida["Nombre"], "No alcoholica",  bebida["Precio"], bebida["Temperatura"])
        lista_beb.append(bebida)
    cant_al = 0
    cant_nal = 0
    cont_c = 0
    suma_m = 0

    while True:
        print("*****BIENVENIDO A SAMÁN BAR*****")
        option = input("Elige la opción que corresponda:\n1. Registrar bebida\n2. Realizar compra\n3. Estadísticas\n4. Salir\n---->")
        if option == "1":
            nombre = input("Nombre: ")
            precio = int(input("Introduzca el precio: "))
            tipo = input("Tipo:\n1. Alcoholica\n2. No Alcoholica\n----->")
            if tipo == "1":
                tipo_e = "Alcoholica"
                grado_a = int(input("Grado de alcohol: "))
                bebida = Alcoholica(nombre, tipo_e, precio, grado_a)
            else:
                tipo_e = "No alcoholica"
                temp = int(input("Temperatura: "))
                bebida = NoAlcoholica(nombre, tipo_e, precio, temp)
            lista_beb.append(bebida)
        if option == "2":
            nombre_c = input("Nombre: ")
            edad = int(input("Edad: "))
            ci = int(input("CI: "))
            cliente = Cliente(nombre_c, edad, ci)
            cont_c += 1
            cant_a = 0
            cant_n = 0
            for cosa in lista_beb:
                if cosa.tipo == "Alcoholica":
                    cant_a += 1
                if cosa.tipo == "No alcoholica":
                    cant_n += 1
            lista_com = []
            while True:
                bebida_d = input("Elige la opción deseada: \n1. Alcoholica\n2. No Alcoholica\n")
                if bebida_d == "1":
                    if edad < 18:
                        print("Las bebidas alcoholicas no se encuentran disponibles para tu rango de edad.")
                    else:
                        i = 0
                        for elemento in lista_beb:
                            i += 1
                            if elemento.tipo == "Alcoholica":
                                print(i, ".")
                                elemento.Mostrar() 
                        bebida_pregun = int(input("Cual desea? "))
                        bebida_eleg = lista_beb[bebida_pregun-1]
                        cant_beb = int(input("Introduzca la cantidad de bebidas que desea: "))
                        cant_al += cant_beb
                        compra_user = Compra(bebida_eleg, cant_beb, bebida_eleg.precio*cant_beb)
                        lista_com.append(compra_user)
                if bebida_d == "2":
                    i = 0
                    for elemento in lista_beb:
                        i += 1
                        if elemento.tipo == "No alcoholica":
                            print(i, ".")
                            elemento.Mostrar() 
                    bebida_pregun = int(input("Cual desea? "))
                    bebida_eleg = lista_beb[bebida_pregun-1]
                    cant_beb = int(input("Introduzca la cantidad de bebidas que desea: "))
                    cant_nal += cant_beb
                    compra_user = Compra(bebida_eleg, cant_beb, bebida_eleg.precio*cant_beb)
                    lista_com.append(compra_user)
                salida = input("Desea otra?\n1. Sí\n2. No\n")
                if salida == "2":
                    break
            #descuentos
            b = 0
            a = 1
            c = edad-1
            desc = 0
            monto_f = 0
            fibo = get_fibo(edad, a, b)
            primo = get_primo(edad, c)
            monto_sum = 0
            for elemento in lista_com:
                monto_sum += elemento.monto
            if fibo == True:
                monto_f = monto_sum + monto_sum*0.05
                desc += monto_sum*0.05
            if primo == True:
                monto_f = monto_sum + monto_sum *0.1
                desc += monto_sum*0.1
            if fibo == False and primo == False:
                monto_f = monto_sum
            print("*****FACTURA****")
            cliente.MostrarCliente()
            for elemento in lista_com:
                elemento.MostrarCompra()
            print(f"Total: {monto_f}")
            print(f"Descuento: {desc}")
        if option == "3":
            print("*****ESTADISTICAS****")
            print(f"Vendidas alcoholicas: {cant_al}")
            print(f"Vendidas no alcoholicas: {cant_nal}")

        if option == "4":
            break
main()