#función pida nº dados
#función tire los dados
#función dé puntuación a cada jugador según pares o nones
import random

def obtener_datos():
    dados = int(input("Diga el número de dados: "))
    while dados == 0:
        dados = int(input("Imposible!\nDiga número de dados again: "))
    return dados

def tirar_dados(dados):
    tiradas = []
    for j in range(dados):
        tiradas.append(random.randint(1, 6)) 
    return tiradas

def quien_gana(tiradas):
    jugador_pares = []
    jugador_nones = []
    for elemento in tiradas:
        if elemento % 2 == 0:
            jugador_pares.append(elemento)
        else:
            jugador_nones.append(elemento)
    
    if len(jugador_pares) > len(jugador_nones):
        ganador = "el jugador de los pares"
    elif len(jugador_pares) == len(jugador_nones):
        ganador = "han empatado"
    else:
        ganador = "el jugador de los nones"

    return ganador 

def main():
    dados = obtener_datos()
    tiradas = tirar_dados(dados)
    ganador = quien_gana(tiradas)
    print("Dados: ", tiradas,"\nHa ganado", ganador )

main()
