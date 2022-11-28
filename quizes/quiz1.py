num_user = input("Introduzca un número entero positivo: ")
while not num_user.isnumeric():
    num_user = input("Cifra inválida. Introduzca un número entero positivo: ")

#Algoritmo para saber si es repunit
is_repunit = True
for digit in num_user:
    if digit != num_user[0]:
        is_repunit = False
        break

if is_repunit != False:
    print(f"El número {num_user} es repunit")
    suma_numeros = 0
    for numeros in num_user:
        suma_numeros += int(numeros)
    cont = 0
    for nums in range (0, suma_numeros):
        if nums*nums == int(suma_numeros):
            cont += 1
    if cont >0:
        print(f"La suma de los digitos de {num_user} es un numero cuadrado")
    else:
        print(f"la suma de los digitos de {num_user} no es numero cuadrado")

else:
    print(f"El número {num_user} no es repunit")

#Para saber si es cuadrado





