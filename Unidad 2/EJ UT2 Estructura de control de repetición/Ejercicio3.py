#Ejercicio 3: Escribe un programa que pida al usuario un número entero positivo y realice una cuenta atrás desde ese número hasta 0. El programa debe imprimir cada número en la cuenta atrás.
numero = int(input("Dime un número entero positivo\n"))

contador = 0
for i in range (numero, 0, -1):
    print(i, end=", ")
print(0)