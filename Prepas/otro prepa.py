
contraseña = input("Introduzca su contraseña: ")
is_valid = False
mylist= []
while is_valid == False:
    while len(contraseña)<8:
        contraseña = input("Su contraseña debe tener un mínimo de ocho caracteres. Introduzcala de nuevo:")
    print (contraseña)
    while contraseña.lower() == contraseña:
        contraseña = input("Su contraseña debe tener mínimo una letra mayuscula. Introduzcala de nuevo: ") 
    print (contraseña)
    while contraseña.upper == contraseña:
        contraseña = input("Su contraseña debe tener mínimo una letra minuscula. Introduzcala de nuevo: ") 
    print (contraseña)
    while contraseña.isalpha() == contraseña: 
        contraseña = input("Su contraseña debe tener mínimo un caracter no alphanumerico . Introduzcala de nuevo: ") 
    print (contraseña)
    while contraseña.isnumeric == contraseña: 
        contraseña = input("Su contraseña debe tener mínimo un caracter no alphanumerico . Introduzcala de nuevo: ") 
    print(contraseña)
    is_valid = True
if is_valid == True:
    mylist.append(contraseña)
    print(mylist)

    


   
