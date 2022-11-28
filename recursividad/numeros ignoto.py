while True:
    try:
        n = int(input("Introduzca un número natural: "))
        if n <= 0:
            raise Exception
        break
    except:
        print("Número inválido")
cont = 0
def ignoto(n, cont):
    if n < 1:
        return cont
    if n % 2 == 1:
        cont += 1
    n = n // 2
    return ignoto(n, cont)

if ignoto(n, cont) % 2 != 0:
    print(f"{n} es un número ignoto")
else:
    print(f"{n} no es un número ignoto")