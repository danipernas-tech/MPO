#Ejercicio 4: Escribe un programa que pida al usuario un número entero positivo y calcule su factorial. EL programa debe imprimir el resultado. EL factorial de un número (n) se define como el producto de todos los números enteros desde 1 hasta (n)

num6 = int(input("Dime un número positivo\n"))
resultado = 1
for i in range (1, num6 + 1):
    resultado *= i
print(resultado)