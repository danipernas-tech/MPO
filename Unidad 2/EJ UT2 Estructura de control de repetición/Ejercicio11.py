#Ejercicio 11: Escribe un programa que pida al usuario cuantas evaluaciones hay que cualificar. Seguidamente se recibirán ese número de series de notas (números decimales entre 0 y 10) y calcule la media de esas notas. El programa debe seguir pidiendo notas hasta que el usuario ingrese un -1. Al final, imprime la media.

evaluaciones = int(input("Cuántas evaluaciones hay que calificar?\n"))

for i in range(1, evaluaciones + 1):
    suma = 0
    cantidad = 0
    notas = float(input(f"Dime la notas de la evalucación {i}(-1 para salir)\n"))
    while notas != -1:
        suma += notas
        cantidad += 1
        notas = float(input("Dime mas notas (-1 para salir)\n"))
    media = suma / cantidad
    print(f"La media de la evaluación {i} es {media}")

numero = int(input("Dime un número:\n"))

mayor = 0
menor = 0
while numero != 0:
    if numero > mayor:
        mayor = numero
    elif numero < menor:
        menor = numero
    numero = int(input("Dime otro número (0 para salir)\n"))

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")

