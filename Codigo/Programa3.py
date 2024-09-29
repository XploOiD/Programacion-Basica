def calcularIncremento(salario,x):
    nuevoSalario=salario + (salario*(x/100))
    return nuevoSalario

salarioActual=float(input("Ingrese el salario actual del trabajador: "))
incremento=float(input("Ingrese el porcentaje de incremento que tendra el salario del trabajador: "))
nuevoSalario=calcularIncremento(salarioActual,incremento)
print("El nuevo salario del trabajador es: ", nuevoSalario)
