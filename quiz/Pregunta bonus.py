# Nombre del estudiante : Paula Alonso
#Número de carnet : 20221110206
#Correo unimet: paula.alonso@correo.unimet.edu.ve

num_user = input("Introduzca un número natural: ")
is_repunit = True
for digit in num_user:
    num_reference = num_user[0]
    if digit != num_reference:
        is_repunit = False
if is_repunit == True:
    print(f"El número {num_user} es repunit.")
else:
    print(f"El número {num_user} no es repunit.")

