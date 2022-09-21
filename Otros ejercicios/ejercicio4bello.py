import os


while True:
    try:
        player1=int(input("Hola, juguemos a piedra, papel o tijeras! Elige una opción:\n1-Piedra\n2-Papel\n3-Tijeras\n"))
        break
    except ValueError:
        print("Introduce una opción válida.")
os.system('cls')
while True:
    try:
        player2=int(input("Hola, juguemos a piedra, papel o tijeras! Elige una opción:\n1-Piedra\n2-Papel\n3-Tijeras\n"))
        break
    except ValueError:
        print("Introduce una opción válida.")
os.system('cls')
if player1==1:
    if player2==2:
        print("Jugador 1: piedra\nJugador 2: papel\nResultado: ganó el jugador 2")
    elif player2==3:
        print("Jugador 1: piedra\nJugador 2: tijeras\nResultado: ganó el jugador 1")
    else:
        print("Jugador 1: piedra\nJugador 2: piedra\nResultado: empate")
if player1==2:
    if player2==1:
        print("Jugador 1: papel\nJugador 2: piedra\nResultado: ganó el jugador 1")
    elif player2==3:
        print("Jugador 1: papel\nJugador 2: tijeras\nResultado: ganó el jugador 2")
    else:
        print("Jugador 1: papel\nJugador 2: papel\nResultado: empate")
if player1==3:
    if player2==1:
        print("Jugador 1: tijeras\nJugador 2: piedra\nResultado: ganó el jugador 2")
    elif player2==2:
        print("Jugador 1: tijeras\nJugador 2: papel\nResultado: ganó el jugador 1")
    else:
        print("Jugador 1: tijeras\nJugador 2: tijeras\nResultado: empate")
