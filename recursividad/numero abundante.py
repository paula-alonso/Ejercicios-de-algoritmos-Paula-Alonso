while True:
    try:
        num = int(input("Introduzca un número natural: "))
        break
    except:
        print("Número inválido.")
i = num - 1
def abundante(num, i):
    divisor = 0
    if i == 0:
        return 0
    if num % i == 0:
        divisor = i
    return divisor + abundante(num, i-1)

if abundante(num, i) > num:
    print(f"{num} es un número abundante.")
else:
    print(f"{num} no es un número abundante.")
