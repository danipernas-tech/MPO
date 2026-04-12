#Ejercicio 3: Escribe un programa que pida al usuario un número entero positivo y realice una cuenta atrás desde ese número hasta 0. El programa debe imprimir cada número en la cuenta atrás.
num5 = int(input("Dime un número: \n"))
for variable in range (num5, -1, -1):
    print("Cuenta atrás", variable) 