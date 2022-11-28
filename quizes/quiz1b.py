infraction={
    1:{"name":"Choque", "cost":50},
    2:{"name":"Semáforo", "cost":30},
    3:{"name":"Falta de documentos", "cost":100},
}

officers={
    1:{"name":"Luis", "lastName":"Bello","ci":13452224},
    2:{"name":"Jose", "lastName":"Quevedo","ci":44235611},
    3:{"name":"Antonio", "lastName":"Guerra","ci":12345678},
}

db={}
key_list = ["name", "Last name", "CI"]
print("Bienvenido a la estación de transito")
opción = int(input("Introduzca el numero que corresponda a la opción deseada:\n1-Ingresar un infractor a la base de datos del sistema\n2-Eliminar un infractor de la base de datos del sistema\n3-Mostrar por pantalla las multas registradas hasta el momento del sistema\n"))
while opción != 4:
    if opción == 1:
        for key in key_list:
            db[key] = input(f"Introduzca su {key}")
        print(db)

        for id, inf in infraction.items():
            print(id, inf)
        infractions = input("Introduzca la opción que prefiera: ")
        while not int(infractions) in infraction.keys():
            infraction = input("Cifra inválida. Introduzca la opción que prefiera: ")
        if infractions == 1:
            db["Infraction"] = infraction.get(1)
        elif infractions == 2:
            db["Infraction"] = infraction.get(2)
        else:
            db["Infraction"] = infraction.get(3) 
        name_officer = input("Introduzca el oficial que le puso la multa:\n1-Luis\n2-Jose\n3-Antonio")
        if name_officer == 1:
            db["Officer"] = officers.get(1)
        elif name_officer == 2:
            db["Officer"] = officers.get(2)
        else:
            db["Officer"] = officers.get(3)

        print(db)

