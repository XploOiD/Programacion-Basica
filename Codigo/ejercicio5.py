#Definir la lcase persona
class persona:
    #Contructor de la clase
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    #Metodo para mostrar la informacion de la persona
    def mostrar_informacion(self):
        print(f"Nombre:{self.nombre},Edad:{self.edad}")


    #metodo para verificar si es mayor de edad 
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False    

 #Crear una instancia de la clase persona
persona1 = persona("Carlos",16)

#Llamar al metado para mostrar la informacion
persona1.mostrar_informacion()

#Comprobar si la persona es mayor de edad 
if persona1.es_mayor_de_edad():
    print(f"{persona1.nombre} es mayor de edad.")
else:
    print(f"{persona1.nombre} no es mayor de edad")    
    