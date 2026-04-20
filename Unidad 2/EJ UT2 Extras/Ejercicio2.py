#Ejercicio 2: Escribe un programa que pida al usuario un número entero y determine si es positivo, negativo o cero. El programa debe imprimir un mensaje indicando el resultado.

num2 = int(input("Dime un número\n"))
if num2 > 0:
    print(f"{num2} es positivo")
elif num2 < 0:
    print(f"{num2} es negativo")
else:
    print(f"{num2} es 0")