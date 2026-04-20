#Ejercicio 1: Escribe un programa que pida al usuario un número entero y determine si es par o impar. El programa debe imprimir un mensaje indicando el resultado.


num = int(input("Dime un número\n"))
if num % 2 == 0:
    print(f"{num} es par")
else:
    print(f"{num} es impar")



