#Con while
age = input("Por favor, introduce tu edad: ")
aux = 1
age = int(age)
while aux<=age:
    print(aux)
    aux+=1
#Con for 
if age.isnumeric():
    age = int(age)
    for ages in range(1,age+1):
        print (ages)
else:
    print("Introduzca una cifra válida")
