#Ejercicio12: Escribe un programa que pida al usuario una serie de números enteros y determine cuál es el mayor y cuál es el menor. El programa debe seguir pidiendo números hasta que el usuario ingrese un 0. Al final, imprime el mayor y el menor.

numero = int(input("Dime un número:\n"))

mayor = numero
menor = numero
while numero != 0:
    if numero > mayor:
        mayor = numero
    elif numero < menor:
        menor = numero
    numero = int(input("Dime otro número (0 para salir)\n"))

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")

num = int(input("DIme un número\n"))
if num % 2 == 0:
    print(f"{num} es par")
else:
    print(f"{num} es impar")