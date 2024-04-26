from random import *
from Character import *

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
