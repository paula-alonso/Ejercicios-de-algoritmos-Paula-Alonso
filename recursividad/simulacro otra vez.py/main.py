from bebida import Bebida, Alcoholica, NoAlcoholica
from cliente import Cliente
from compra import Compra

def get_fibo(edad, a, b):
    z = a + b
    if a > edad:
        return False
    if a == edad:
        return True
    b = a
    a = z
    return get_fibo(edad, a, b)

def get_primo (monto1, c):
    if c == 1:
        return True
    if monto1 % c == 0:
        return False
    return get_primo(monto1, c-1)

def main():
    bebidas = [{"Nombre": "Coca-Cola", "Precio": 2, "Temperatura": 10}, {"Nombre": "Cerveza", "Precio": 1.5, "Grado al": 5}, {"Nombre": "Red Bull", "Precio": 3, "Temperatura": 15}]
    lista_bebidas = []
    for elemento in bebidas:
        if elemento["Nombre"] == "Cerveza":
            bebida = Alcoholica(elemento["Nombre"], "Alcoholica", elemento["Precio"], elemento["Grado al"])
        else:
            bebida = NoAlcoholica(elemento["Nombre"], "No Alcoholica",  elemento["Precio"], elemento["Temperatura"])
        lista_bebidas.append(bebida)
    cant_a = 0
    cant_b = 0
    cant_c = 0
    monto_dia = 0
    max_a = 0
    max_n = 0
    n_a = "No se ha vendido ninguna"
    n_n = "No se ha vendido ninguna"
    while True:
        print("Bienvenido a Saman Bar")
        option = input("¿Qué deseas hacer?\n1. Registrar bebida\n2.Realizar Compra\n3. Estadísticas\n4. Salir\n")
        if option == "1":
            nombre_b = input("Nombre: ")
            precio_b = int(input("Precio: "))
            bebida_t = input("Tipo de bebida:\n1. Alcoholica\n2. No alcoholica\n")
            if bebida_t == "1":
                bebida_user = "Alcoholica"
                g_al = int(input("Grado de alcohol: "))
                bebida_regis = Alcoholica(nombre_b, bebida_user, precio_b, g_al) 
            else:
                bebida_user = "No Alcoholica"
                temp = int(input("Temperatura: ")) 
                bebida_regis = NoAlcoholica(nombre_b, bebida_user, precio_b, temp)
            lista_bebidas.append(bebida_regis)
        if option == "2":
            monto_1 = 0
            lista_compras = []
            nombre_c = input("Nombre del cliente: ")
            edad = int(input("Edad: "))
            ci = input("CI: ")
            cliente = Cliente(nombre_c, edad, ci)
            cant_c += 1
            while True:
                print("Bebidas disponibles")
                i = 0
                for elemento in lista_bebidas:
                    if edad > 18: 
                        print(f"ID: {i}")
                        elemento.MostrarBebida()
                    else:
                        if elemento.tipo != "Alcoholica":
                            print(f"ID: {i}")
                            elemento.MostrarBebida()
                    i += 1
                index_b = int(input("Introduzca el ID de la bebida que desea: "))
                bebida_eleg = lista_bebidas[index_b]
                cantidad = int(input("Introduzca la cantidad que desea: "))
                compra = Compra(bebida_eleg, cantidad)
                lista_compras.append(compra)
                monto_1 += compra.CalcularMonto()
                if bebida_eleg.tipo == "Alcoholica":
                    cant_a += 1
                    if cantidad > max_a:
                        n_a = bebida_eleg.nombre
                        max_a = cantidad
                else:
                    cant_b += 1
                    if cantidad > max_n:
                        n_n = bebida_eleg.nombre
                        max_n = cantidad
                salida = input("Deseas otra bebida:\n1. Sí\n2. No\n")
                if salida == "2":
                    break
            #Descuentos
            a = 1
            b = 0
            c = monto_1-1
            desc= 0
            fibo = get_fibo(edad, a, b)
            primo = get_primo(monto_1, c)
            if fibo == True:
                desc += monto_1 * 0.05
            if primo == True:
                desc += monto_1 * 0.1
            if desc > 0:
                monto_t = monto_1 + desc
            else:
                monto_t = monto_1
            monto_dia += monto_t
            print("******FACTURA*****")
            cliente.MostrarCliente()
            print("BEBIDAS")
            for elemento in lista_compras:
                elemento.MostrarCompra()
                print("")
            print(f"Total de la compra: {monto_t}")
            print(f"Descuentos: {desc}")
        
        if option == "3":
            #Promedio de compra
            if monto_dia == 0:
                prom_c = 0
            else:
                prom_c = monto_dia/cant_c
            print("*****ESTADISTICAS*****")
            print(f"Bebidas alcoholicas vendidas: {cant_a}")
            print(f"Bebidas no alcoholicas vendidas: {cant_b}")
            print(f"Bebida alcoholica más vendida: {n_a}")
            print(f"Bebida alcoholica más vendida: {n_n}")  
            print(f"Promedio de compra: {prom_c}")                      
                    
                    
        if option == "4":
            break

main()