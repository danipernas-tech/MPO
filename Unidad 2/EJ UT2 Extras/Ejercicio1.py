#Ejercicio 1: Escribe un programa que pida al usuario un número entero y determine si es par o impar. El programa debe imprimir un mensaje indicando el resultado.


num = int(input("Dime un número\n"))
if num % 2 == 0:
    print(f"{num} es par")
else:
    print(f"{num} es impar")

#Ejercicio 2: Escribe un programa que pida al usuario un número entero y determine si es positivo, negativo o cero. El programa debe imprimir un mensaje indicando el resultado.

num2 = int(input("Dime un número\n"))
if num2 > 0:
    print(f"{num2} es positivo")
elif num2 < 0:
    print(f"{num2} es negativo")
else:
    print(f"{num2} es 0")

num3 = int(input("Dime un número\n"))
if num3 % 3 == 0 and num3 % 5 == 0:
    print(f"{num3} es divisible por 3 y 5")
else:
    print(f"{num3} no es divisible por 3 y 5")