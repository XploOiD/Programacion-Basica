import random

# Definimos los tipos de terreno
TIPOS_DE_TERRITORIO = ['T', 'W', 'F', 'M']  # 'T' = Tierra, 'W' = Agua, 'F' = Bosque, 'M' = Montaña

class GeneradorDeMapa:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.mapa = self.generar_mapa()

    def generar_mapa(self):
        # Creamos una matriz vacía para el mapa
        mapa = []
        
        # Llenamos la matriz con terrenos aleatorios
        for i in range(self.alto):
            fila = []
            for j in range(self.ancho):
                terreno = random.choice(TIPOS_DE_TERRITORIO)  # Elegimos un terreno aleatorio
                fila.append(terreno)
            mapa.append(fila)
        
        return mapa

    def mostrar_mapa(self):
        # Mostrar el mapa de manera legible
        for fila in self.mapa:
            print(' '.join(fila))

# Usamos el generador de mapas
ancho = 10  # Ancho del mapa
alto = 6  # Alto del mapa

generador = GeneradorDeMapa(ancho, alto)

# Mostrar el mapa generado
print("Mapa Aleatorio:")
generador.mostrar_mapa()