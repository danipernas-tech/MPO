#Ejercicios de clase UT2: Estructura de control de repetición

#Ejercicio 1: Escribe un programa que pida al usuario un número entero positivo e imprima los números desde el 0 hasta ese número (incluido). El programa debe imprimir los números en cada iteración.

num3 = int(input("Dime un número: \n"))

for i in range(num3):
    print(i, end=", ")
print(num3)
