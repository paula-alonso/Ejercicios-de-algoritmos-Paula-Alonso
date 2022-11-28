while True:
    try:
        num = int(input("Introduzca un número natural mayor que 1: "))
        if num <= 1:
            raise Exception
        break
    except:
        print("Número inválido.")
i = num - 1
def primo(num, i):
    if i <= 1:
        return True
    if num % i == 0:
        return False
    return primo(num, i-1)

if primo(num, i) == True:
    print(f"{num} es un número primo.")
else:
    print(f"{num} no es un número primo.")