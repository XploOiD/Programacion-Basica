class Empleado:
    def __init__(self,nombre,salario_mensual):
        self.nombre = nombre
        self.salario_mensual = salario_mensual
#Metodo para calcular el salario mensual
    def calcular_salario_anual(self):
        return self.salario_mensual * 12
#Metodo para mostrar la informacion del empleado
    def mostrar_informacion(self):
        print(f"Empleado:{self.nombre},Salario mensual:{self.salario_mensual}")
#Crear instancia
empleado1 = Empleado("Ana",2000)

empleado1.mostrar_informacion()
print(f"Salario Anual:{empleado1.calcular_salario_anual()}")



        