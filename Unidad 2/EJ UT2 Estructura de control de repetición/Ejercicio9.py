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
