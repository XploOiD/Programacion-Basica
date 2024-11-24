#Cajero Automatico

#Saldo inicial del usuario

saldo = 1000

#Funcion para consultar saldo

def consultar_saldo():
    print(f"Su saldo actual es: ${saldo}")

#Funcion para depositar dinero

def depositar_dinero():
    global saldo #Declaramos que usaremos la variable global "saldo"
    cantidad= float(input("Ingrese la cantidad que desea depositar: $"))
    if cantidad > 0:
        saldo += cantidad #Aunmenta el saldo en la cantidad depositada
        print(f"Has depositado ${cantidad}. Su nuevo saldo es: ${saldo}")
    else:
        print("La cantidad debe ser mayor a 0.")

#Funcion para retirar dinero

def retirar_dinero():
    global saldo
    cantidad= float(input("Ingrese la cantidad que desea retirar: $"))
    if 0 < cantidad <= saldo:
        saldo -= cantidad
        print(f"Has retirado ${cantidad}. Su nuevo saldo es:${saldo}")
    elif cantidad > saldo:
        print("Fondos insuficientes")
    else:
        print("La cantidad debe ser mayor a 0.")        

# Funcion principal para mostrar el menú y realizar las operaciones

def menu():
    while True:
        print("\nCajero Automatico")
        print("1.Consultar saldo")
        print("2.Depositar dinero")
        print("3.Retirar dinero")
        print("4.Salir")

        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            consultar_saldo()
        elif opcion == "2":
            depositar_dinero()
        elif opcion == "3":
            retirar_dinero()
        elif opcion == "4":
            print("Gracias por usar el cajero automatico.")
            break
        else:
            print("Opcion no valida.porfavor, intente de nuevo")
#Llamar para iniciar el programa
menu()                        