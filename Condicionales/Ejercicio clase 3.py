primer_numero = input("Introduzca un número: ")
segudo_numero = input("Introduzca otro número: ")
is_valid= True
if primer_numero.isnumeric():
    primer_numero = float(primer_numero)
else:
    is_valid = False
if segudo_numero.isnumeric():
    segudo_numero = float(segudo_numero)
else:
    is_valid = False



if segudo_numero == 0:
    print("Error")
else:
    resultado = primer_numero/segudo_numero
    print(resultado)