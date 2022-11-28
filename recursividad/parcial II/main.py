from trabajador import Trabajador
def get_prime(num_h, a):
    if num_h == 1:
        return False
    if a == 1:
        return True
    if num_h % a == 0:
        return False
    return get_prime(num_h, a-1)
def get_def(monto_tentativo, a, suma_div):
    if a < 1:
        if suma_div < monto_tentativo:
            return True
        else:
            return False
    if monto_tentativo % a == 0:
        suma_div += a
    return get_def(monto_tentativo, a-1, suma_div)

def get_fact(num_h):
    if num_h == 1:
        return 1
    return num_h * get_fact(num_h-1)

def main():
    tar_horas = [{"Tipo": "Ingeniero", "Honorarios": 25}, {"Tipo": "Arquitecto", "Honorarios": 10}, {"Tipo": "Obrero", "Honorarios": 5}]
    lista_trab = []
    monto_total = 0
    cant_i = 0
    cant_a = 0
    cant_o = 0
    pago_i = 0
    pago_a = 0
    pago_o = 0
    max_i = 0
    name_i = "No hay ninguno"
    max_a = 0
    name_a = "No hay ninguno"
    max_o = 0
    name_o = "No hay ninguno"
    while True:
        print("Bienvenido a Saman Constructions!")
        option = input("Selecciona la opción que corresponda: \n1. Registrar Trabajador\n2. Ver trabajadores\n3. Estadisticas\n4. Salir\n")
        if option == "1":
            name = input("Nombre: ")
            apellido = input("Apellido: ")
            ci = input("CI: ")
            i = 1
            for elemento in tar_horas:
                print(i, ".")
                for key, value in elemento.items():
                    print(key, ": ", value)
                i += 1
            eleccion = input("Introduzca el número de la opción deseada: ")
            if eleccion == "1":
                tipo = "Ingeniero"
                sueldo = 25
                cant_i += 1
                especialidad = input("Especialidad\n1. Civil\n2. Electricista\n")
                if especialidad == "1":
                    especialidad ="Civil" 
                else:
                    especialidad ="Electricista"
            elif eleccion == "2":
                tipo = "Arquitecto"
                sueldo = 10
                cant_a += 1
                especialidad = input("Especialidad\n1. Exterior\n2. Interior\n")
                if especialidad == "1":
                    especialidad ="Exterior" 
                else:
                    especialidad ="Interior"
            else:
                tipo = "Obrero"
                sueldo = 5
                cant_o += 1
                especialidad = input("Especialidad\n1. Capataz\n2. Novato\n")
                if especialidad == "1":
                    especialidad ="Capataz" 
                else:
                    especialidad ="Novato"
            num_h = int(input("Número de horas trabajadas este mes: "))
            mes = input("Mes:\n1. Enero\n2.Febrero\n3. Marzo\n4. Abril\n5. Mayo\n6. Junio\n7. Julio\n8. Agosto\n9. Septiembre\n10. Octubre\n11. Noviembre\n12. Diciembre\n")
            monto_tentativo = sueldo*num_h
            #Descuentos
            desc = 0 
            rec = 0
            a = num_h-1
            suma_div = 0
            num_prim = get_prime(num_h, a)
            num_def = get_def(monto_tentativo, a, suma_div)
            fact = get_fact(num_h)
            if num_prim == True:
                desc += monto_tentativo * 0.05
            if num_def == True:
                rec += monto_tentativo * 0.1
            if fact == num_h:
                rec += monto_tentativo * 0.15
            monto_f = monto_tentativo + rec - desc
            monto_total += monto_f
            trabajador = Trabajador(name, apellido, ci, tipo, num_h, mes, especialidad, monto_f)
            lista_trab.append(trabajador)
            if tipo == "Ingeniero":
                pago_i += monto_total
            if tipo == "Arquitecto":
                pago_a += monto_total
            if tipo == "Obrero":
                pago_o += monto_total

        if option == "2":
            for empleado in lista_trab:
                empleado.Mostrar()
    
        if option =="3":
            if cant_i == 0:
                prom_i = 0
            else:
                prom_i = pago_i/cant_i
            if cant_a == 0:
                prom_a = 0
            else:
                prom_a = pago_a/cant_a
            if cant_o == 0:
                prom_o = 0
            else:
                prom_o = pago_o/cant_o
            for elemento in lista_trab:
                if elemento.tipo == "Ingeniero":
                    if elemento.sueldo_f > max_i:
                        max_i = elemento.sueldo_f
                        name_i = elemento.nombre
                if elemento.tipo == "Arquitecto":
                    if elemento.sueldo_f > max_a:
                        max_a = elemento.sueldo_f
                        name_a = elemento.nombre
                if elemento.tipo == "Obrero":
                    if elemento.sueldo_f > max_o:
                        max_o = elemento.sueldo_f
                        name_o = elemento.nombre
                
            print("*****ESTADÍSTICAS****")
            print(f"Monto total pagado a los empleados: {monto_total}")
            print(f"Cantidad de ingenieros: {cant_i}")
            print(f"Cantidad de arquitectos: {cant_a}")
            print(f"Cantidad de obreros: {cant_o}")
            print(f"Promedio de pago de ingenieros: {prom_i}")
            print(f"Promedio de pago de arquitectos: {prom_a}")
            print(f"Promedio de pago de obreros: {prom_o}")
            print(f"Ingeniero con mayor pago: {name_i}")
            print(f"Arquitecto con mayor pago: {name_a}")
            print(f"Obrero con mayor pago: {name_o}")

        if option == "4":
            break
main()