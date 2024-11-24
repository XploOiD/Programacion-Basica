#Solicito al usuario el numero de ondas
waves = int(input("Ingrese un numero: "))
#Generar el Patron de Ondas
for _ in range(3):
    for _ in range(waves):
        print("~", end="")
        print()
        for _ in range(2):
            print("~", end="")
            print()