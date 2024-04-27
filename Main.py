from random import *
from Character import character

class partida:
    def __init__(self, nombre):
        self.nombre = nombre

        rivals = [
            0,
            character("cagona", True, 55, 20, 70),
            character("tancarro", False, 15, 70, 10),
            character("asesino", False, 45, 15, 60),
            character("pro", True, 45, 40, 40)
        ]


    def yo(self):
        rivals[0] = character.createCharacter()

    def fight(self, maincharacter, character2):
        while maincharacter.tamano > 0 and character2.tamano > 0 :
            bucle = 0

            if maincharacter.velocidad > maincharacter :
                while bucle != 1:
                    bucle = int(input("Que quieres hacer?\n1. Atacar\n2. Coming soon..."))
                    if bucle != 1 :
                        print("Que le des al 1 (uno) hostias.")
                self.ataque(maincharacter, character2)

                print(character2.nombre, " se ha quedado con: ", character2.tamano, " hp")
                print("Turno del rival")
                self.ataque(character2, maincharacter)
                print(maincharacter.nombre, " se ha quedado con: ", maincharacter.tamano, " hp")

            else :
                print("Turno del rival")
                self.ataque(character2, maincharacter)
                print(maincharacter.nombre, " se ha quedado con: ", maincharacter.tamano, " hp")

                while bucle != 1:
                    bucle = int(input("Que quieres hacer?\n1. Atacar\n2. Coming soon..."))
                    if bucle != 1:
                        print("Que le des al 1 (uno) hostias.")
                self.ataque(maincharacter, character2)

                print(character2.nombre, " se ha quedado con: ", character2.tamano, " hp")

    def ataque(self, atacante, defensor):
        varAtaque = randint(85, 115)
        varAtaque = varAtaque / 100

        varDefensa = randint(92, 115)
        varDefensa = varDefensa / 100

        varAtaque = atacante.poder * varAtaque
        varDefensa = defensor.tamano * varDefensa

        defensor.tamano = defensor.tamano * varDefensa - atacante.poder * varAtaque

test = partida("1")
test()