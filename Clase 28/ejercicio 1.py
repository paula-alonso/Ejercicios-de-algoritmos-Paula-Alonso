divisa =  {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa_user = input("introduzca la divisa. ej: Euro, Dollar, Yen: ")
print(divisa.get(divisa_user.title(), "Divisa no encontrada."))