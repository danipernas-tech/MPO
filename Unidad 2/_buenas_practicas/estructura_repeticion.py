#Escribe un programa que pida al usuario un número entero positivo y muestre la tabla de multiplicar de ese número hasta 10


numero = int(input("Dime un número entero y positivo\n"))

for i in range (1, 11, 1):
    print(f"{numero} x {i} = {(numero * i)}")


#Escribe un programa que pida al usuario una serie de números enteros y calcule la suma acumulativa de esos números. El programa debe seguir pidiendo números hasta que el usuario ingrese un 0. Al final, imprime la suma total.

numero = int(input("Dime un número entero\n"))

suma = 0
while (numero != 0):
    suma += numero
    numero = int(input("Dime otro número (0 para salir)\n"))
print(suma)

#Escribe un programa que pida al usuario cuantas evaluaciones hay que cualificar. Seguidamente se recibirán ese número de series de notas (números decimales entre 0 y 10) y calcule la media de esas notas. El programa debe seguir pidiendo notas hasta que el usuario ingrese un -1. Al final, imprime la media.

""""
#Introduce el número de evaluaciones: 3
#Notas de la evaluación 1: 6 8 4 3.5 9 -1
#Notas de la evaluación 2: 7 5 8.5 -1
#Notas de la evaluación 3: 9 10 8.5 -1
La media de la evaluación 1 es: 6.5
La media de la evaluación 2 es: 7.5
La media de la evaluación 3 es: 9.0
"""
evaluaciones = int(input("Cuántas evaluaciones hay que cualificar?\n"))

for i in range (1, evaluaciones + 1, 1):
    suma_notas = 0
    cantidad_notas = 0
    nota = float(input(f"Dime una nota de la evaluación {i} (-1 para salir)\n"))
    while (nota != -1):
        suma_notas += nota
        cantidad_notas += 1
        nota = float(input(f"Dime otra nota de la evaluación {i} (-1 para salir)\n"))
    print(f"Nota media de la evaluación {i} = {(suma_notas / cantidad_notas)}")

    
