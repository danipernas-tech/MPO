#Escribe un programa que pida al usuario un número entero y determine si es múltiplo de 3 o de 5. El programa debe imprimir un mensaje indicando el resultado. Si el número es múltiplo de ambos, debe imprimir "Múltiplo de 3 y 5". Si no es múltiplo de ninguno, debe imprimir "No es múltiplo de 3 ni de 5".

numero = int(input("Dime un número\n"))

if numero % 5 == 0 and numero % 3 == 0:
    print("Multiplo de 3 y 5")
elif numero % 5 == 0:
    print("Multiplo de 5")
elif numero % 3 == 0:
    print("Multiplo de 3")
else:
    print("No es multiplo ni de 3 ni de 5")
