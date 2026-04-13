# Ejercicio 2: Escribe un programa que pida al usuario un número entero positivo y cuente cuántos números pares hay desde 0 hasta ese número (incluido). El programa debe imprimir el resultado.

num4 = int(input("Dime un número: \n"))
resultado = 0
for i in range (0, num4+1, 2):
    resultado += i
print(resultado)