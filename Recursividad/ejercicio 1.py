base = input("Introduce una base: ")
expo = input("Introduce un exponente: ")

def exponencial(base, expo):
    if expo == 0:
        return 1
    return base**exponencial(base, expo-1)
