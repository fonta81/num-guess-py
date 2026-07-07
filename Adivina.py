import random


class Game:
    def __init__(self):
        self.numeroRandom = random.randint(1, 20)

    def Juego(self):
        while True:
            try:
                numero = self.Pedirnumero()
                diferencia = abs(numero - self.numeroRandom)

                if numero == self.numeroRandom:
                    print("!!Correcto!!")
                    return
                elif numero > 20 or numero < 1:
                    print("Ingresa un valor dentro de los parametros")

                elif numero < self.numeroRandom:
                    if diferencia <= 5:
                        print("Muy cerca, solo un poco mas alto")
                    else:
                        print("Un numero un poco mas alto")
                elif numero > self.numeroRandom:
                    if diferencia <= 5:
                        print("Muy cerca, solo un poco mas bajo")
                    else:
                        print("Un numero un poco mas bajo")
            except ValueError:
                print("Ingresa un valor entero, o valido")
            except Exception as e:
                print(f"Ingrese un valor valido\nError: {e}")

    def Pedirnumero(self):
        valor = int(input("Dame un numero del 1-20: "))
        return valor

    def Usuario(self):
        self.Juego()


def main():  # El menu principal
    gg = Game()

    while True:
        print("\n" + "=" * 60)
        print("1. Jugar")
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
