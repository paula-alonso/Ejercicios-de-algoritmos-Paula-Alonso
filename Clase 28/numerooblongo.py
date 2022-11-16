from unittest import result


num_user = int(input("Introduzca un número natural: "))
aux = 1
cont = 0
while aux <= num_user:
    resultado = (aux+1)*aux
    if resultado == num_user:
        cont +=1
        print(f"El número {num_user} es un número oblongo")
    aux +=1
if cont == 0:
    print(f"El número {num_user} no es un número oblongo")

