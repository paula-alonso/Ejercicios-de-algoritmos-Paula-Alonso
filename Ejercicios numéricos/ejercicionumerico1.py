number = int(input("Introduzca un número: "))
aux = number-1
cont = 0
if number <=1:
    print(f"El número {number} no es primo.")
else:
    while aux > 1:
        print("aux",aux)
        if number%aux == 0:
            cont +=1
            break
        aux-=1

    if cont == 0:
        print(f"El número {number} es primo.")
    else:
        print(f"El número {number} no es primo.")

