import numbers


number = int(input("Introduzca un número: "))
aux = number-1
is_prime = True
while aux>1:
    if number%aux == 0:
        is_prime = False
        break
    aux-=1
if is_prime==False:
    print(f"El número {number} es compuesto")
else:
    print(f"El número {number} no es compuesto")