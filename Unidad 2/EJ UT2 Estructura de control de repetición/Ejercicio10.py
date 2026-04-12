#Ejercicio10: Escribe un programa que escoja un número aleatorio entre 1 y 100 y le pida al usuario que adivine el número. El programa debe dar pistas al usuario si el número es mayor o menor que el número elegido. El programa debe seguir pidiendo números hasta que el usuario adivine el número correcto.


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