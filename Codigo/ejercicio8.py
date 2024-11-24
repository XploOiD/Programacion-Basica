import random

# Dimensiones de la cuadrícula
filas = 10
columnas = 10

# Crear una cuadrícula vacía
cuadricula = [[' ' for _ in range(columnas)] for _ in range(filas)]

# Número de puntos a dibujar
num_puntos = random.randint(5, 20)

# Colocar puntos aleatorios en la cuadrícula
for _ in range(num_puntos):
    x = random.randint(0, filas - 1)
    y = random.randint(0, columnas - 1)
    cuadricula[x][y] = '.'

# Dibujar la cuadrícula
for fila in cuadricula:
    print(' '.join(fila))