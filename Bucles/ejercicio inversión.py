cant_inver = float(input("Introduzca la cantidad a invertir: "))
interes = float(input("Introduzca el interés anual: "))
years = int(input("Introduzca el número de años que dura la inversión: "))
#con while
aux = 1
cont = 0
while aux<=years:
    cap_obtenido = cant_inver*(interes/100)*1
    cont +=cap_obtenido
    print(cont)
    aux+=1
#con for
cont_for = 0
for year in range (0, years):
    cap_obtenido_for = cant_inver*(interes/100)*1
    cont_for += cap_obtenido_for
    print(cont_for)