#Ejercicio 5: Escribe un programa que pida al usuario un número entero positivo e imprima solamente los números múltiplos de 3 o de 5 dentro de ese rango.

#Si el número es múltiplo de 3, imprime el número seguido de el mensaje "es múltiplo de 3". Si el número es múltiplo de 5, imprime el número seguido del mensaje "es múltiplo de 5". Si el número es múltiplo de ambos no debes imprimir nada.

num = int(input("Dime un número positivo\n"))
for i in range (1, num + 1, 1):
    if i % 3 == 0 and i % 5 == 0:
        pass
    elif i % 3 == 0:
        print(i , " multiplo de 3")
    elif i % 5 == 0:
        print(i , " multiplo de 5")