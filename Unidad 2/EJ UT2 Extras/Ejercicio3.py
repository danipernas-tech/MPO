
#Escribe un programa que pida al usuario un número entero y determine si es divisible por 3 y 5. El programa debe imprimir un mensaje indicando el resultado.


num3 = int(input("Dime un número\n"))
if num3 % 3 == 0 and num3 % 5 == 0:
    print(f"{num3} es divisible por 3 y 5")
else:
    print(f"{num3} no es divisible por 3 y 5")