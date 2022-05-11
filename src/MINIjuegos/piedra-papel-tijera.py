import random

def obtener_datos():
    print("PIEDRA, PAPEL O TIJERA!")
    jugador1 = input("Diga el nombre del jugador 1: ")
    jugador2 = input("Diga el nombre del jugador 2: ")
    return jugador1, jugador2

def sacar_manos(jugador1, jugador2):
    
    while True:
        jugada1 = random.randint(1, 3)
        jugada2 = random.randint(1, 3)

        if jugada1 != jugada2:
            break
        else:
            print("habéis empatado")

    return [jugada1, jugada2]

def ganador(jugador1, jugador2, jugadas):
    piedra = 1
    papel = 2
    tijera = 3
    if jugadas[0] == piedra and jugadas[1] == tijera:
        return jugador1
    elif jugadas[0] == tijera and jugadas[1] == papel:
        return jugador1
    elif jugadas[0] == papel and jugadas[1] == piedra:
        return jugador1
    else:
        return jugador2
      
def main():

    midict = {1:"piedra", 2: "papel", 3: "tijera"}
    jugador1, jugador2 = obtener_datos()
    jugadas = sacar_manos(jugador1, jugador2)
    resultado = ganador(jugador1, jugador2, jugadas)
    print("El jugador",jugador1, "ha sacado: ", midict[jugadas[0]])
    print("El jugador", jugador2, "ha sacado: ", midict[jugadas[1]])

    print("El ganador es: ", resultado)

main()