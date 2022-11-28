while True:
    try:
        num = int(input("Introduzca un número natural: "))
        break
    except:
        print("Número inválido.")
i = num - 1
def deficiente(num, i):
    divisor = 0
    if i == 0:
        return 0
    if num % i == 0:
        divisor = i
    return divisor + deficiente(num, i-1)

if deficiente(num, i) < num:
    print(f"{num} es un número deficiente.")
else:
    print(f"{num} no es un número deficiente.")
