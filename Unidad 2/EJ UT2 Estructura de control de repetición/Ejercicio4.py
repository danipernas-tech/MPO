#Ejercicio 4: Escribe un programa que pida al usuario un número entero positivo y calcule su factorial. EL programa debe imprimir el resultado. EL factorial de un número (n) se define como el producto de todos los números enteros desde 1 hasta (n)

numero = int(input("Dime un número entero positivo\n"))

#5 = 5 x 4 x 3 x 2 x 1

resultado = 1
for i in range (1, numero + 1):
    resultado *= i
print(resultado)

numero = 5
for i in range (0, numero, 1):
    print(i)