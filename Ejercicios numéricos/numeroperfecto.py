number = int(input("Introduzca un número: "))
aux = number-1
acum = 0
while aux >=1:
    if number%aux == 0:
        acum+=aux
    aux-=1

if acum == number:
    print(f"El número {number} es perfecto")
else:
    print(f"El número {number} no es perfecto")