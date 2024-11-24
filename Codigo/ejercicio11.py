#Define la cantidad de puntos de tu linea
length = int(input("Ingrese la longitud de la linea de puntos: "))
direction = input("Horizontal(h) o Vertical(v): ").lower()

if direction == "h":
    print("#" * length)
elif direction == "v":
    for _ in range(length):
        print("#")
else:
    print("Direccion no valida.")      
        