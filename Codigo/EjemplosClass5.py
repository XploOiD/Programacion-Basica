class Cancion:

    def __init__(self,autor,titulo,duracion):
        self.duracion = duracion
    

    def __len__(self):
        return self.duracion

cancion = Cancion("Metallica","Master of Puppets",220)

print(len(cancion))
print(cancion.__len__)        