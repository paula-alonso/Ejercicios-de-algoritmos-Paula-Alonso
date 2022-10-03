from re import I


phrase = input("Introduzca una frase: ")
letter = input("Introduzca una letra: ")
cont = 0
for i in phrase:
    if letter == i:
        cont += 1

if cont==1:
    print(f"La letra {letter} aparece {cont} vez en la frase")
elif cont>1:
    print(f"La letra {letter} aparece {cont} veces en la frase") 
else:
    print(f"La letra {letter} no está en la frase")