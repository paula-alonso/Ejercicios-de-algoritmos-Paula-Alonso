name=input("Por favor introduzca su nombre: ")
age=float(input("Por favor introduzca su edad: "))
if age<=4:
    print(f"El cliente: {name.capitalize()} tiene: {round(age,None)} años y su entrada de cine es gratis.")
elif age<=18:
    print(f"El cliente: {name.capitalize()} tiene: {round(age,None)} años y su entrada de cine cuesta: 1.50 dólares.")
elif age>=60:
    print(f"El cliente: {name.capitalize()} tiene: {round(age,None)} años y su entrada de cine cuesta: 1 dólar.")
else:
    print(f"El cliente: {name.capitalize()} tiene: {round(age,None)} años y su entrada de cine cuesta: 2.00 dólares")




