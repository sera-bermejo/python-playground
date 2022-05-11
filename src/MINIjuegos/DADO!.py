import random

jugadores = int(input("¿Cuántos jugadores van a pasárselo pipa?: "))
nombres = []
for j in range (1, jugadores+1):
    nombres.append(input(f"¿Cuál es tu nombre, jugador {j}?: "))

respuesta = input("¿Estáis listos para empezar?: ")
if respuesta == "no":
    quit("¡Qué pena, otra vez será! :(")

tiradas = []

for j in range(jugadores):
  tiradas.append(random.randint(1, 6)) 

for j in range(jugadores):
    print("El jugador",nombres[j], "ha sacado una puntuación de: ", tiradas[j])