#Ejercicios de clase UT2: Estructura de control condicional

#Ejercicio 1: Escribe un programa que pida al usuario un número entero y determine si es positivo o negativo. El programa debe imprimir un mensaje indicando el resultado.

num1 = int(input("Dime un número\n"))

if num1 > 0:
    print("Es positivo")
elif num1 < 0:
    print("Es negativo")
else:
    print("Es neutro")

#Ejercicio 2: Escribe un programa que simule el trabajo de un portero de discoteca. El programa debe pedir al usuario su edad y determinar si puede entrar o no. Si la edad es menor de 18 años, el programa debe imprimir "No puedes entrar". Si la edad es mayor o igual a 18 años, el programa debe imprimir "Puedes entrar".

edad = int(input("Dime tu edad\n"))

if edad >= 18:
    print("Puedes entrar")
else:
    print("No puedes entrar")


#Ejercicio 3: Escribe un programa que pida al usuario dos números enteros correspondientes a la casilla que está Pacman (1er número) y a la que está un fantasma (2o número), luego debe recibir un texto con el formato "normal" o "caramelo". Si el texto es "normal" y los números son iguales, el programa debe imprimir "Pacman ha sido atrapado". Si el texto es "caramelo" y los números son iguales, el programa debe imprimir "Pacman ha comido al fantasma". En cualquier otro caso, el programa debe imprimir "Pacman ha escapado".

pacman = int(input("Dime la casilla de Pacman\n"))
fantasma = int(input("Dime la casilla del fantasma\n"))

if pacman == fantasma:
    estado = input("Dime el estado(nomal o caramelo)\n")
    if estado == "normal":
        print("Pacman ha sido atrapado")
    elif estado == "caramelo":
        print("Pacman ha comido al fantasma")
    else:
        print("Pacman ha escapado")
else:
    print("Pacman ha escapado")


#Ejercicio 4: Escribe un programa que pida al usuario un número entero y determine si es múltiplo de 3 o de 5. El programa debe imprimir un mensaje indicando el resultado. Si el número es múltiplo de ambos, debe imprimir "Múltiplo de 3 y 5". Si no es múltiplo de ninguno, debe imprimir "No es múltiplo de 3 ni de 5".

num2 = int(input("Dime un número\n"))
if num2 % 3 ==0:
    print("Es múltiplo de 3")
if num2 % 5 == 0:
    print("Es múltiplo de 5")
else:
    print("No es múltiplo de ninguno")

if num2 % 3 == 0 and num2 % 5 == 0:
    print("Es múltiplo de ambos")


#Ejercicio 5: Escribe un programa que pida un rol y una academia de estudios, si el rol es "alumno" y la academia es "Prometeo" el programa debe darle acceso al servidor de Discord oficial y al de los alumnos, donde se critica a los profes. Si el rol es "profesor" y la academia es "Prometeo" el programa debe darle acceso al servidor de Discord oficial, pero no al de los alumnos. En cualquier otro caso, el programa debe imprimir "No tienes acceso al servidor de Discord".

rol = input("Dime tu rol\n")
academia = input("Dime tu academia\n")
if rol == "alumno" and academia == "Prometeo":
    print("Acceso a Discord oficial y Discord de alumnos")
elif rol == "profesor" and  academia == "Prometeo":
    print("Acceso a Dsicor oficial")
else:
    print("No tienes acceso al servidor de Discord")


#Ejercicios de clase UT2: Estructura de control de repetición

#Ejercicio 1: Escribe un programa que pida al usuario un número entero positivo e imprima los números desde el 0 hasta ese número (incluido). El programa debe imprimir los números en cada iteración.

num3 = int(input("Dime un número: \n"))
contador = 0
while contador < num3:
    contador += 1
    print(contador)

# Ejercicio 2: Escribe un programa que pida al usuario un número entero positivo y cuente cuántos números pares hay desde 0 hasta ese número (incluido). El programa debe imprimir el resultado.

num4 = int(input("Dime un número: \n"))
resultado = 0
for i in range (0, num4, 2):
    resultado += i
print(resultado)

#Ejercicio 3: Escribe un programa que pida al usuario un número entero positivo y realice una cuenta atrás desde ese número hasta 0. El programa debe imprimir cada número en la cuenta atrás.
num5 = int(input("Dime un número: \n"))
for variable in range (num5, -1, -1):
    print("Cuenta atrás", variable) 
