#Imprimir si el número pertenece o no a la sucesión de fibonacci

num = int(input("Introduzca un número: "))
a = 1
b = 1
def fibo(num, a, b):
    z = a + b
    if b >= num:
        return False
    if num == 0 or num == 1:
        return True
    if z == num:
        return True
    b = a
    a = z
    return fibo(num, a, b)
if fibo(num, a, b) == True:
    print(f"{num} está en la sucesión de fibonacci")
else:
    print(f"{num} no está en la sucesión de fibonacci")

#Determinar el término n-esimo de la sucesión
def fibo2(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibo2(num-1) + fibo2(num-2)

print(fibo2(num))