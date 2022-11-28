while True:
    try:
        num = int(input("Introduzca un número natural mayor que 1: "))
        if num <= 1:
            raise Exception
        break
    except:
        print("Número inválido.")
i = num-1
def compuesto(num, i):
    if i == 1:
        return False
    if num % i == 0:
        return True
    return compuesto(num, i-1)

if compuesto(num, i) == True:
    print(f"{num} es un número compuesto.")
else:
    print(f"{num} no es un número compuesto.")