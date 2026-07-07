# un juego que dnd hay q adivinar el numero que salio
# si el numero q das es menor -> decir que un poco mayor / si es menor -> un poco menor
# si la diferencia es mas grande -> dar otro mensaje
import random


class Game:
    def __init__(self):
        self.numeroRandom = random.randint(1, 10)

    def Juego(self, numero):
        diferencia = numero - self.numeroRandom

        if numero == self.numeroRandom:
            print("!!Correcto")
            return
        elif numero < self.numeroRandom:
            if diferencia <= 2:
                print("Muy cerca, solo un poco mas alto")
            else:
                print("Un numero un poco mas alto")
