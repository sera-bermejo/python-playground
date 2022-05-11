import random


class Jugador:

    def __init__(self, nombre, puntuacion):
        self.nombre = nombre
        self.puntuacion = puntuacion

    def mostrar_nombre(self):
        print(self.nombre)

    def mostrar_puntuacion(self):
        print(self.puntuacion)

    def tirar_dado(self):
        self.puntuacion = random.randint(1, 6)



sera = Jugador("sera", 0)
pablo = Jugador("Pablo", 0)
mercedes = Jugador("Mercedes", 0)
