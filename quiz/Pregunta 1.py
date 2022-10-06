# Nombre del estudiante : Paula Alonso
#Número de carnet : 20221110206
#Correo unimet: paula.alonso@correo.unimet.edu.ve

penta = [[45,78,65],[12,35,70],[51,3,105],[22,12,85]]
is_penta = False
for listanum in penta:
    for num in listanum:
        for n in range (0, num+1):
            op = ((3*(n**2))-n)/2
            if op == int(num):
                is_penta = True
        if is_penta == True:
            print(f"{num} es pentagonal")
        else:
            print(f"{num} no es pentagonal")

