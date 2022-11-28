while True:
    try:
        n = int(input("Introduzca un número natural: "))
        if n <= 0:
            raise Exception
        break
    except:
        print("Número inválido")
i = n-1
def cuadrado(n, i):
    if i < 0:
        return False
    if i ** 2 == n:
        return True
    return cuadrado(n, i-1)
if cuadrado(n, i) == True:
    print(f"{n} es un cuadrado")
else:
    print(f"{n} no es un cuadrado")
