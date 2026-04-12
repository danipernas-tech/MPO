#Ejercicios de clase UT2: Estructura de control de repetición

#Ejercicio 1: Escribe un programa que pida al usuario un número entero positivo e imprima los números desde el 0 hasta ese número (incluido). El programa debe imprimir los números en cada iteración.

num3 = int(input("Dime un número: \n"))
contador = 0
while contador < num3:
    contador += 1
    print(contador)

# Ejercicio 2: Escribe un programa que pida al usuario un número entero positivo y cuente cuántos números pares hay desde 0 hasta ese número (incluido). El programa debe imprimir el resultado.

num4 = int(input("Dime un número: \n"))
resultado = 0
for i in range (0, num4, 2):
    resultado += i
print(resultado)

#Ejercicio 3: Escribe un programa que pida al usuario un número entero positivo y realice una cuenta atrás desde ese número hasta 0. El programa debe imprimir cada número en la cuenta atrás.
num5 = int(input("Dime un número: \n"))
for variable in range (num5, -1, -1):
    print("Cuenta atrás", variable) 