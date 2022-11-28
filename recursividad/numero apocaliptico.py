while True:
    try:
        n = int(input("Introduzca un número natural: "))
        if n <= 0:
            raise Exception
        break
    except:
        print("Número inválido")

base2 = str(2 ** n)
i = 0
cont = 0
def num_ap(base2, i, cont):
    if i == len(base2) or i+1 == len(base2) or i+2 == len(base2):
        return False
    if cont >= 1:
        return True
    if base2[i] == "6" and base2[i+1] == "6" and base2[i+2] == "6":
        cont += 1
    return num_ap(base2, i+1, cont)

if num_ap(base2, i, cont) == True:
    print("Sí")
else:
    print("No")