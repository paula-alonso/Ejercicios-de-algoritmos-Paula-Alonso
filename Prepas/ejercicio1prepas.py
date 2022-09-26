
temperatura = float(input("Introduzca una temperatura: "))
time = float(input("¿Qué tiempo del día es? introduzca el número:\n1-Mañana\n2-Tarde\n3-Noche\n"))
if temperatura>10 and time ==1:
    print("Hace calor en la mañana.")
elif temperatura<10:
    print("Hace frío.")
else:
    print("Se encuentra a una temperatura ambiente.")