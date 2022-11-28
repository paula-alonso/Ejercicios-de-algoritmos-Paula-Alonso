while True:
    try:
        num = int(input("Introduzca un número natural: "))
        break
    except:
        print("Número inválido.")
i = num-1 
 
def perfecto (num, i):
    divisor = 0  
    if i == 0:
        return 0
    if num % i == 0:
        divisor = i
    return divisor + perfecto(num, i-1)

if perfecto (num, i) == num:
    print(f"{num} es un número perfecto.")
else: 
    print(f"{num} no es un número perfecto.")