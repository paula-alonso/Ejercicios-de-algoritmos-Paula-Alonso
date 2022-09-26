import numbers


number = int(input("Introduzca un número: "))
aux= number-1
is_prime = True
while aux>1:
    if number%aux == 0:
        is_prime = False
    aux-=1
if is_prime == False:
    print("El número no es primo.")
else:
    print("El número es primo")