#Ejercicio 7: Escribe un programa que pida al usuario un número entero positivo y muestre la tabla de multiplicar de ese número. Por ejemplo, si el usuario ingresa 3, el programa debe imprimir:


num2 = int(input("Dime un número positivo\n"))
resultado = 0
for i in range (1, 11, 1):
    resultado = num2 * i
    print(f"{num2} x {i} = {resultado}")