from random import *

class character:
    def __init__(self, nombre, rango, poder, tamano, velocidad):
        self.nombre = nombre
        self.rango = rango
        self.poder = poder
        self.tamano = tamano
        self.velocidad = velocidad

    def createCharacter(self):
        int(input())