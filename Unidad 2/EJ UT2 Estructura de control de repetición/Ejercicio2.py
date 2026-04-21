# Ejercicio 2: Escribe un programa que pida al usuario un número entero positivo y cuente cuántos números pares hay desde 0 hasta ese número (incluido). El programa debe imprimir el resultado.

numero = int(input("Dime un número: \n"))
contador = 0
for i in range (0, numero + 1, 2):
    contador += 1
print(contador)