from personal import Personal

def main():
    sueldos = [{"Tren": "Supersónico", "Sueldo": 60}, {"Tren": "Carbón", "Sueldo": 30}]
    lista_per = []
    cont = 0
    cont_s = 0
    cont_c = 0
    cant_au = 0
    prom_s = 0
    prom_c = 0
    while True:
        print("*****BIENVENIDO A SAMÁN-TRAIN*****")
        while True:
            try:
                option = int(input("¿Qué deseas hacer?\n1. Registrar personal\n2. Ver personal\n3. Estadísticas\n4. Salir\n---->"))
                if option < 1 or option > 4:
                    raise Exception
                break
            except:
                print("Opción inválida")
        if option == 1:
            monto = 0
            name = input("Nombre: ")
            while True:
                try:
                    ci = int(input("CI: "))
                    tipo = int(input("Tipo de tren:\n1. Supersónico\n2. Carbón\n--->"))
                    horas = int(input("Horas de trabajo: "))
                    break
                except:
                    print("Objeto inválido")

            if tipo == 1:
                tipo = "Supersónico"
                for elemento in sueldos:
                    if elemento["Tren"] == "Supersónico":
                        monto = elemento["Sueldo"]
            else:
                tipo = "Carbón"
                for elemento in sueldos:
                    if elemento["Tren"] == "Carbón":
                        monto = elemento["Sueldo"]
            if horas > 8:
                    monto = monto + monto*0.30
                    cant_au += 1
            personal = Personal(name, ci, tipo, horas, monto)
            lista_per.append(personal)
            cont += 1
        if option == 2:
            if lista_per == []:
                print("No hay personal disponible.")
            for persona in lista_per:
                persona.Mostrar()
        if option == 3:
            print("******ESTADISTICAS*****")
            print(f"Cantidad de personal: {cont} pers.")
            for persona in lista_per:
                persona.Mostrar()
                if persona.tipo == "Supersónico":
                    prom_s += persona.monto
                    cont_s += 1
                if persona.tipo == "Carbón":
                    prom_c += persona.monto
                    cont_c += 1
            if cont_s == 0:
                pago_prom_s = 0
            else:
                pago_prom_s = prom_s/cont_s
            if cont_c == 0:
                pago_prom_c = 0
            else:
                pago_prom_c = prom_c/cont_c
            print(f"Personal supersónico: {cont_s}")
            print(f"Presonal carbón: {cont_c}")
            print(f"Personal con aumento: {cant_au}")
            print(f"Pago promedio supersonico: {pago_prom_s}")
            print(f"Pago promedio carbon: {pago_prom_c}")
        if option == 4:
            break


        

        

main()