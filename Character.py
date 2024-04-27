class character:
    def __init__(self, nombre, rango, poder, tamano, velocidad):
        self.nombre = nombre
        self.rango = rango
        self.poder = poder
        self.tamano = tamano
        self.velocidad = velocidad

    def createCharacter(self):
        vNombre = input("Introduce el nombre de tu personaje")
        vRango = input("Introduce el rango de tu personaje (True o False)")
        vPoder = int(input("Introduce el poder de tu personaje (int 1-100)"))
        vTamano = int(input("Introduce el tamaño de tu personaje (int 1-100)"))
        vVelocidad = int(input("Introduce la velocidad de tu personaje (int 1-100)"))

        return character(vNombre, vRango, vPoder, vTamano, vVelocidad)