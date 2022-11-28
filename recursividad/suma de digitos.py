num = int(input("Introduzca un número: "))

def suma_digitos(num):    
    if num < 10:
        return num
    else:
        suma = 0
        for digito in str(num):
            suma += int(digito)
        num = suma
        return suma_digitos(num)

print(suma_digitos(num))
