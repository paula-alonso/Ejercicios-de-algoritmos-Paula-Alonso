from vehiculo import Vehiculo, Automovil, Motocicleta
def main():
    vehiculos = [ 
    { "tipo": "AUTOMOVIL", "placa": "ABC12D", "marca": "Chevrolet", "puesto": "A12", "entrada": "10:00:36", "minusvalido": False},
    { "tipo": "AUTOMOVIL", "placa": "IJK56M", "marca": "Mazda", "puesto": "A33", "entrada": "11:48:22", "minusvalido": False},
    { "tipo": "MOTOCICLETA", "placa": "EFG34H", "marca": "Suzuki", "puesto": "B10", "entrada": "10:20:15"},
]
    vehiculo2 = []
    while True:
        user = input("Bienvenido! Qué deseas hacer?\n1. Registrar vehículo\n2. Salida de vehículo\n3. Ver vehículo\n4. Salir\n")
        if user == "1":
            for elemento in vehiculos:
                if elemento["tipo"] == "AUTOMOVIL":
                    automovil = Automovil(elemento["placa"], elemento["marca"], elemento["puesto"], elemento["entrada"], elemento["minusvalido"])
                    vehiculo2.append(automovil)
                if elemento["tipo"] == "MOTOCICLETA":
                    moto = Motocicleta(elemento["placa"], elemento["marca"], elemento["puesto"], elemento["entrada"])
                    vehiculo2.append(moto)
        if user == "2":
            i = 0
            for elemento in vehiculo2:
                print(i, ".")
                elemento.mostrar()
                i+= 1
            option = int(input("Introduzca el número del que desea eliminar: "))
            del vehiculo2[option].puesto
            vehiculo2[option].hora_salida = input("Introduzca la hora de salida: ")
            a = 0
            for elemento in vehiculo2:
                print(a, ".")
                elemento.mostrar()
                a+= 1
        if user == "3":
            e = 0
            for elemento in vehiculo2:
                if elemento.hora_salida == None:
                    print(e, ".")
                    elemento.mostrar()
                    e += 1
        if user == "4":
            break
main()