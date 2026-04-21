#Ejercicio 11: Escribe un programa que pida al usuario cuantas evaluaciones hay que cualificar. Seguidamente se recibirán ese número de series de notas (números decimales entre 0 y 10) y calcule la media de esas notas. El programa debe seguir pidiendo notas hasta que el usuario ingrese un -1. Al final, imprime la media.

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


