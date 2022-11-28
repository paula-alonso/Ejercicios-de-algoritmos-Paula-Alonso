while True:
    try:
        n = int(input("Introduzca un número natural: "))
        if n <= 0:
            raise Exception
        break
    except:
        print("Número inválido")

def ambicioso(n):
    if n == 1:
        return False
    lista_div = []
    suma = 0
    for num in range(1, n-1):
        if n % num == 0:
            lista_div.append(num)
    for elemento in lista_div:
        suma += elemento
    if suma == n:
        return True
    else:
        n = suma
        return ambicioso(n)
if ambicioso(n) == True:
    print(f"{n} es un número ambicioso.")
else:
    print(f"{n} no es un número ambicioso.")