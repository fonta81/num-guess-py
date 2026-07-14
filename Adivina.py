# importan librerias
import random


class Game:
    def __init__(self):
        self.numeroRandom = random.randint(1, 20)  # genera un numero random entre 1-20

    def Juego(self):
        while True:
            try:
                numero = self.Pedirnumero()  # pide un numero al Usuario
                # que tan cerca del numero ersta el valor que dio el Usuario:
                diferencia = abs(numero - self.numeroRandom)

                if numero == self.numeroRandom:  # si le atino
                    print("!!Correcto!!")
                    return
                elif numero > 20 or numero < 1:  # si se sale del los parametros
                    print("Ingresa un valor dentro de los parametros")

                elif numero < self.numeroRandom:  # si puso un numero bajo
                    if diferencia <= 5:  # si esta cerca por 5 numeros
                        print("Muy cerca, solo un poco mas alto")
                    else:  # si no esta cerca
                        print("Un numero un poco mas alto")
                elif numero > self.numeroRandom:  # si puso un numero alto
                    if diferencia <= 5:  # si esta cerca por 5 numeros
                        print("Muy cerca, solo un poco mas bajo")
                    else:  # si no esta cerca
                        print("Un numero un poco mas bajo")
            except ValueError:  # en caso de error por numeros
                print("Ingresa un valor entero, o valido")
            except Exception as e:  # en caso de error:
                print(f"Ingrese un valor valido\nError: {e}")

    def Pedirnumero(self):  # pide numero al Usuario
        valor = int(input("Dame un numero del 1-20: "))
        return valor  # devuelve el numero

    def Usuario(self):  # inicia el juego
        self.Juego()


def main():  # El menu principal
    gg = Game()  # asigna variable a Game

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


if __name__ == "__main__":  # inicia el programa
    main()
