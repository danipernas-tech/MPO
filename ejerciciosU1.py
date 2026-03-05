import math

nombre_ej = "Dani" #Nombre variables snake_case.
edad = 20
print(edad) #20
edad = 30
print(edad) #30
edad2 = "22"

print(type(edad)) #tipo int
print(type(nombre_ej)) #tipo str

entero = 25 #int
decimal = 9.9 #float
texto = "Hola" #str
booleano = True #boolean


#casting
edad = str(30) #seria "30" una cadena de texto
edad2 = int("22") #seria 20 un entero


#Salidas
print("hola Dani")
print(50)
print(True)

#Entradas
name = input("Como te llamas:")
print(f"Hola {name}")


#Operadores Artitmeticos
a = 10
b = 3
print(a + b)   # Suma:            13
print(a - b)   # Resta:            7
print(a * b)   # Multiplicación:  30
print(a / b)   # División:         3.333...
print(a // b)  # División entera:  3  (descarta los decimales)
print(a % b)   # Módulo (resto):   1  (10 = 3×3 + 1)
print(a ** b)  # Potencia:      1000  (10³)


#Operadores Lógicos
edad = 20
tiene_carnet = True
# and: las DOS condiciones deben ser True
print(edad >= 18 and tiene_carnet)   # True
# or: al menos UNA debe ser True
print(edad >= 18 or tiene_carnet)    # True
# not: invierte el resultado
print(not tiene_carnet)              # False

#Operadores Comparación
#devuelven True o False
edad = 20
print(edad == 18)   # False  (¿es igual a 18?)
print(edad != 18)   # True   (¿es distinto de 18?)
print(edad > 18)    # True   (¿es mayor que 18?)
print(edad < 18)    # False  (¿es menor que 18?)
print(edad >= 18)   # True   (¿es mayor o igual que 18?)
print(edad <= 18)   # False  (¿es menor o igual que 18?)


#Ejercicio 1
#Escribir un programa que solicite al usuario su nombre y edad y luego imprima un mensaje de bienvenida personalizado.
nombre = input("Cual es tu nombre?\n")
edad = int(input("Cual es tu edad?\n"))
print(f"Hola {nombre}, tienes {edad} años.")

#Ejercicio 2
#Escribe un programa en Python que pida al usuario dos números y luego imprime la suma, resta, muultiplicación y división de amos números
num1 = float(input("Dime un número\n"))
num2 = float(input("Dime otro número\n"))
suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
divi = num1 / num2
print(f"La suma es: {suma}\nLa resta es: {resta}\nLa multi es: {multi}\nLa division es: {divi}")

#Ejercicio 3
#Pide dos numeros e imprime True si son iguales y False si no son iguales
num3 = int(input("Dime un numero\n"))
num4 = int(input("Dime otro numero\n"))
print(f"Son iguales?: {num3==num4}")

#Ejercicio 4
#Pide al usuario dos numeros enteros e imprime True si el primero es divisible por el segundo
num5 = int(input("Dime un numero\n"))
num6 = int(input("Dime otro numero\n"))
print(f"El primer numero es divisible por el segundo?: {num5%num6 == 0}")

#Ejercicio 5
#Pide al usuario un número entero e imprima el siguiente, contador
num7 = int(input("Dime un numero:"))
num7 += 1
print(f"El siguiente numero del que me has dicho es: {num7}")

#Ejercicio 6
#Escribe un programa que pida al usuario un número entero e imprima, su doble, triple, mitad, cuadrado y raiz cuadrada
num8 = int(input("Dime un numero:\n"))

doble = num8 * 2
triple = num8 * 3
mitad = num8 / 2
cuadrado = num8 **2
raiz = math.sqrt(num8)

print(f"El doble es: {doble}")
print(f"El triple es: {triple}")
print(f"La mitad es: {mitad}")
print(f"El cuadrado es: {cuadrado}")
print(f"La raiz cuadrada es: {raiz}")

#Ejercicio 7
#Pide al usuario 3 numeros enteros e imprime True si todos de ellos son mayores que cero, False lo contrario
num9 = int(input("Dime un numero: \n"))
num10 = int(input("Dime otro numero: \n"))
num11 = int(input("Dime otro numero mas: \n"))
print(f"Los 3 numeros son mayores que 0?: {num9 > 0 and num10 > 0 and num11 > 0}")

#Ejercicio 8
#Pide 3 nombres al usuario y si uno es Juan imprime True, si no False
nombre1 = (input("Dime un nombre:\n"))
nombre2 = (input("Dime otro nombre:\n"))
nombre3 = (input("Dime otro nombre mas:\n"))
print(nombre1 == "Juan" or nombre2 == "Juan" or nombre3 == "Juan")

#Ejercicio 9
#Pide un numero entero al usuario e imprime True si es myor que 18 y menor que 65, False si es lo contrario
num12 = int(input("Dime un numero:\n"))
print(num12>18 and num12<65)

#Ejercicio 10
#Pide dos numeros enteros e imprime su division decimal, entera y resto
num13 = int(input("Dime un numero:\n"))
num14 = int(input("Dime otro numero:\n"))
decimal2 = num13 / num14
entera2 = num13 // num14
resto2 = num13 % num14
print(f"Division decimal: {decimal2}")
print(f"Division entera: {entera2}")
print(f"Resto: {resto2}")






