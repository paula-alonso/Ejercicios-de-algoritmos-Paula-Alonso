#Escribir un programa que pida al usuario un número entero y muestre por pantalla 
# un triángulo rectángulo como el de más abajo, de altura el número introducido.
height = int(input("Introduzca un número entero: "))
#con while
aux = 1
while aux <= height:
    print(aux*"*")
    aux+=1

#con for
for num in range(1, height+1):
    print (num*"*")