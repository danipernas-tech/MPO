#Ejercicio 9: Escribe un programa que pida al usuario una serie de números enteros y calcule la suma acumulativa de esos números. El programa debe seguir pidiendo números hasta que el usuario ingrese un 0. Al final, imprime la suma total.

suma = 0

num3 = int(input("Dime un número entero\n"))
while num3!=0:
    suma += num3
    num3 = int(input("Dime un número entero\n"))

print(f"Suma total: {suma}")

import random
numeroAleatorio = random.randint(1, 100)
numero = int(input("Intenta adivinar un número del 1 al 100\n"))
while numero != numeroAleatorio:
    if numero > numeroAleatorio:
        print("Es mayor\n")
        numero = int(input("Prueba otra vez\n"))     
    else:
        print("Es menor\n")
        numero = int(input("Prueba otra vez\n"))   
print(f"Lo has acertado! El número es el {numeroAleatorio}")  

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

