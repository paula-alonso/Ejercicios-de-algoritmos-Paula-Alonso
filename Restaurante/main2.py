from pedido import Pedido, Comida, Bebida
from persona import Persona
def main():
    facturacion = {"Comida": [], "Persona": ""}
    monto = 0
    facturacion["Persona"] = []
    while True:
        opcion = input("Bienvenido, deseas una comida o una bebida: \n1. Comida\n2. Bebida\n3.Salir\n")
        if opcion == "1":
            orden = Comida(input("Introduzca el nombre de la comida que desea: "), input("Introduzca su precio: "), input("Salado o dulce: "), input("Platillo: "))
            monto += Pedido.ObtenerMonto(orden)
            orden = Comida.GuardarComida(orden)
            facturacion["Comida"].append(orden)
        if opcion == "2":
            orden = Bebida(input("Introduzca el nombre de la bebida que desea: "), input("Introduzca su precio: "), input("Porcentaje de alcohol: "), input("Temperatura: "))
            monto += Pedido.ObtenerMonto(orden)
            orden = Bebida.GuardarBebida(orden)
            facturacion["Comida"].append(orden)
        if opcion == "3":
            break
    if len(facturacion["Comida"]) >= 1:
        cliente = Persona(input("Introdzuca su nombre: "),input("Introduzca su apellido: "), input("Fecha de nacimiento: "),input("CI: "), monto)
        cliente = Persona.GuardarPersona(cliente)
        facturacion["Persona"].append(cliente)
        print(facturacion)
        print("********FACTURA*******")
        print("COMIDA------")
        for elemento in facturacion.get("Comida"):
            for k, v in elemento.items():
                print(k, ":", v)
        print("CLIENTE-----")
        for elemento in facturacion.get("Persona"):
            for k, v in elemento.items():
                print(k, ":", v)


main()