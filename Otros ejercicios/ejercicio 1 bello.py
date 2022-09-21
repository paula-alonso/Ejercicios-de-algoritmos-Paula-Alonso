number = float(input("Introduzca un número: "))
if number>=0:
    if number%2==0:
        print(f"El número {number} es positivo y par")
    else:
        print(f"El número {number} es positivo e impar")
if number<0:
    if number%2==0:
        print(f"El número {number} es negativo y par")
    else:
        print(f"El número {number} es negativo e impar")