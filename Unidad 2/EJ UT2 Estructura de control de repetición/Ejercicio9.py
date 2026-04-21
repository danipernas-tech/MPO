#Ejercicio 9: Escribe un programa que pida al usuario una serie de números enteros y calcule la suma acumulativa de esos números. El programa debe seguir pidiendo números hasta que el usuario ingrese un 0. Al final, imprime la suma total.

suma = 0

num3 = int(input("Dime un número entero\n"))
while num3!=0:
    suma += num3
    num3 = int(input("Dime un número entero\n"))

print(f"Suma total: {suma}")


