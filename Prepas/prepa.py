names_list = []
age_list = []
data = {"name" :names_list, "age" : age_list}
user = ""

for key in data:
    while user != "si":
        names_list.append(input(f"Introduzca su {key}: "))
        user = input("Desea salir?: ")

print(data)