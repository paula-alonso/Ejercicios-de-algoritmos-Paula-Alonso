from msilib.schema import ComboBox
from alimento import Alimento, Comida, Bebida
from cliente import Persona


def main():
    bd = {"Comida": [],
        "persona": ""}
    order = ""
    cliente = ""
    option = input("Introduzca la opción que prefiera:\n1.Comida\n2.Bebida\n3. Salir\n------>")
    if option == "1":
        order = Comida(input("Introduzca el nombre: "), input("Introduzca el precio: "), input("Salado o Dulce: "), input("Introduce el tipo de platillo: "))
        bd["Comida"].append(Comida.imprimir(order))
    if option == "2":
        order = Bebida(input("Introduzca el nombre: "), input("Introduzca el precio: "), input("Porcentaje de alcohol: "), input("Temperatura:  "))
        bd["Comida"].append(Bebida.imprimir(order))
    cliente = Persona(input("Introduzca su nombre: "), input("Introduzca su apellido: "), input("Fecha de nacimiento: "), input("CI: "), "Cuenta: ")
    bd["persona"] = (Persona.imprimir(cliente))
    print(bd)
main()