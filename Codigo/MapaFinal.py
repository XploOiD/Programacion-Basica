import random
from tkinter import *

# Definimos los tipos de terreno
TIPOS_DE_TERRITORIO = ['🏞', '🌊', '🌳', '⛰️']  # '🏞' = Tierra, '🌊' = Agua, '🌳' = Bosque, '⛰️' = Montaña

class GeneradorDeMapa:
    """
    Clase que genera un mapa con terrenos aleatorios.

    Atributos:
        ancho (int): Ancho del mapa en celdas.
        alto (int): Alto del mapa en celdas.
        mapa (list): Lista bidimensional que representa el mapa generado.
    """

    def __init__(self, ancho, alto):
        """
        Inicializa el generador de mapas con las dimensiones especificadas.

        Parámetros:
            ancho (int): El número de columnas del mapa.
            alto (int): El número de filas del mapa.
        """
        self.ancho = ancho
        self.alto = alto
        self.mapa = self.generar_mapa()

    def generar_mapa(self):
        """
        Genera un mapa aleatorio de tipo de terrenos.

        Retorna:
            list: Una lista bidimensional que representa el mapa, 
                  donde cada celda tiene un tipo de terreno aleatorio.
        """
        mapa = []
        
        for i in range(self.alto):
            fila = []
            for j in range(self.ancho):
                terreno = random.choice(TIPOS_DE_TERRITORIO)  # Elegimos un terreno aleatorio
                fila.append(terreno)
            mapa.append(fila)
        
        return mapa

    def mostrar_mapa(self):
        """
        Muestra el mapa de manera legible en la consola.

        Este método imprime el mapa en la consola, con los terrenos representados 
        por sus respectivos símbolos.
        """
        for fila in self.mapa:
            print(' '.join(fila))

class InterfazGrafica:
    """
    Clase que crea una interfaz gráfica para mostrar el mapa generado usando Tkinter.

    Atributos:
        generador (GeneradorDeMapa): Instancia del generador de mapas.
        root (Tk): Instancia de la ventana principal de Tkinter.
    """

    def __init__(self, generador):
        """
        Inicializa la interfaz gráfica para mostrar el mapa generado.

        Parámetros:
            generador (GeneradorDeMapa): El generador de mapas con los datos que se van a mostrar.
        """
        self.generador = generador
        self.root = Tk()
        self.root.title("Generador de Mapa")

        # Crear la interfaz gráfica
        self.crear_interfaz()

    def crear_interfaz(self):
        """
        Crea la interfaz gráfica para mostrar el mapa en una cuadrícula.

        Cada celda del mapa es representada por un `Label` con el símbolo del terreno y un color de fondo.
        """
        for i in range(self.generador.alto):
            for j in range(self.generador.ancho):
                terreno = self.generador.mapa[i][j]
                color = self.obtener_color(terreno)
                label = Label(self.root, text=terreno, width=4, height=2, bg=color, relief="solid")
                label.grid(row=i, column=j)

    def obtener_color(self, terreno):
        """
        Determina el color de fondo basado en el tipo de terreno.

        Parámetros:
            terreno (str): El tipo de terreno (🏞, 🌊, 🌳, ⛰️).

        Retorna:
            str: El color correspondiente al terreno.
        """
        if terreno == '🏞':  # Tierra
            return 'saddlebrown'
        elif terreno == '🌊':  # Agua
            return 'blue'
        elif terreno == '🌳':  # Bosque
            return 'green'
        elif terreno == '⛰️':  # Montaña
            return 'gray'

    def mostrar(self):
        """
        Muestra la ventana de Tkinter con el mapa generado.

        Este método inicia el ciclo de eventos de Tkinter para que la interfaz sea interactiva.
        """
        self.root.mainloop()

# Usamos el generador de mapas
ancho = 60  # Ancho del mapa
alto = 30  # Alto del mapa

generador = GeneradorDeMapa(ancho, alto)

# Mostrar el mapa generado en consola
print("Mapa Aleatorio:")
generador.mostrar_mapa()

# Crear la interfaz gráfica para mostrar el mapa
interfaz = InterfazGrafica(generador)
interfaz.mostrar()