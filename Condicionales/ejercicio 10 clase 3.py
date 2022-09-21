opcion = float(input("Introduzca la opción de su preferencia: \n1-Vegetariana\n2-No vegetariana\n"))
if opcion == 1:
    opcion = "vegetariana"
    ingrediente= float(input("Introduzca que opción prefiere: \n1-Pimiento \n2-Tofu\n"))
    if ingrediente == 1:
        ingrediente = "Pimiento"
    else:
        ingrediente = "Tofu"
    print(f"Ha elegido una pizza {opcion} con {ingrediente}")
if opcion == 2:
    opcion = "no vegetariana"
    ingrediente2 = float(input("introduzca la opción que prefiere \n1-Peperoni\n2-Jamón\n3-Salmón\n"))
    if ingrediente2 == 1:
        ingrediente2 = "Peperoni"
    elif ingrediente2 == 2:
        ingrediente2 = "Jamón"
    else:
        ingrediente2 = "Salmón"
    print(f"Ha elegido una pizza {opcion} con {ingrediente2}")

        