#Escribe un programa que pida al usuario un número entero y determine si es positivo o negativo. El programa debe imprimir un mensaje indicando el resultado.

numero = int(input("Dime un número entero\n"))
if numero <= 0:
    print("Es negativo")
else:
    print("Es positivo")