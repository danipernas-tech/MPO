#Ejercicio 6: Escribe un programa que pida al usuario un número entero positivo y dibuje un triángulo de asteriscos con la altura especificada. Por ejemplo, si el usuario ingresa 5, el triángulo debe verse así:

num = int(input("Dime un número positivo\n"))
for i in range (1, num + 1, 1):
    print("*" * i)

