#Funciones
#Se define una funcion saludar() y se la utiliza para crear un 
#mensaje de saludo personalizado

def saludar(nombre):
    return "!Hola," + nombre + "!"
    
    mensaje_saludo = saludar("Estudiante")
    
#Manejo de Errores
try:
    resultado_division = 0 / 0
    except ZeroDivisionError:
        print("¡Error! No se puede dividir por cero.")
        finally:
            print("Bloque 'finally': Este código se ejecuta siempre, haya o no haya errores.")
            
            #Trabajo con Archivos
            with open("archivo.txt", "w") as archivo:
                archivo.write("¡Hola desde un archivo!")
            
                
    