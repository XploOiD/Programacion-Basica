class pelicula:

    #Constructor de clase
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
    

    def __str__(self):
        return '{}({})'.format(self.titulo, self.lanzamiento)

class Catalogo:

    peliculas = [] #Esta lista contendra objetos de la clase pelicula

    def __init__(self,peliculas=[]):
        self.peliculas = peliculas

    def agregar(self,p): #p sera un objeto de la pelicula
        self.peliculas.append(p)

    def mostrar(self):
        for p in  self.peliculas:
            print('Se ha creado la pelicula:',p) #print toma por defecto str(p)

p = pelicula("El padrino",175,1972)
c = Catalogo([p]) #Añado una lista con una pelicula desde el principio
c.mostrar()
c.agregar(pelicula("El padrino: Parte 2",202,1974)) #añadimos otra
c.mostrar()