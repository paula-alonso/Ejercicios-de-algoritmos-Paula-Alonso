while True:
    try:
        points=int((input("Introduzca el puntaje obtenido: ")))
        break
    except ValueError:
        print("Por favor, ingresa una cifra válida.")
if 1<=points<=50:
    print(f"Lástima, no hay premio porque obtuviste {points} pts")
elif 51<=points<=150:
    print(f"Felicidades, haz ganado la medalla de bronce por haber obtenido {points} pts!")
elif 151<=points<=180:
    print(f"Felicidades, haz ganado la medalla de plata por haber obtenido {points} pts!")
elif 181<=points<=200:
    print(f"Felicidades, haz ganado la medalla de oro por haber obtenido {points} pts!")
else:
    print("Por favor introduzca una cifra válida.")
