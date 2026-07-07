import random


class Game:
    def __init__(self):
        self.numeroRandom = random.randint(1, 10)

    def Juego(self, numero):
        while True:
            diferencia = abs(numero - self.numeroRandom)

            if numero == self.numeroRandom:
                print("!!Correcto")
                return
            elif numero < self.numeroRandom:
                if diferencia <= 2:
                    print("Muy cerca, solo un poco mas alto")
                else:
                    print("Un numero un poco mas alto")
            elif numero > self.numeroRandom:
                if diferencia <= 2:
                    print("Muy cerca, solo un poco mas bajo")
                else:
                    print("Un numero un poco mas bajo")

    def Pedirnumero(self):
        valor = int(input("Dame un numero: "))
        return valor

    def Usuario(self):
        self.Juego(self.Pedirnumero())


def main():  # El menu principal
    gg = Game()

    while True:
        print("\n" + "=" * 60)
        print("1. Iniciar")
        print("2. Salir")
        elige = input("Elige: ")

        if elige == "2":
            print("Saliendo...")
            break
        elif elige == "1":
            gg.Usuario()
        else:
            print("Ingrese un valor válido")


if __name__ == "__main__":
    main()
