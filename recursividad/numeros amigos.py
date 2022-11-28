#Números amigos: parejas de números que cumplen que la suma de los divisores propios de 
#cada uno de ellos da como resultado el otro número. Por ejemplo, 220 y 284 son números amigos.
while True:
    try:
        num1 = int(input("Introduzca un número natural: "))
        num2 = int(input("Introduzca un número natural: "))
        break
    except:
        print("Número inválido.")
i = num1 - 1
a = num2 - 1
divisor1 = 0
divisor2 = 0
def amigos (num1, num2, i, a, divisor1, divisor2):
    if divisor2 == num1 and divisor1 == num2:
        return True
    if a <= 0 and i <= 0:
        return False
    if a <= 0:
        divisor2 += 0
    else:
        if num2 % a == 0:
            divisor2 += a
    if i <= 0:
        divisor1 += 0
    else:
        if num1 % i == 0:
            divisor1 += i
    return amigos(num1, num2, i-1, a-1, divisor1, divisor2)

if amigos (num1, num2, i, a, divisor1, divisor2) == True:
    print(f"{num1} y {num2} son números amigos.")
else:
    print(f"{num1} y {num2} no son números amigos.")

