import math

#Ejercicio 01
nombre = input("Dime tu nombre\n")
edad = int(input("Dime tu edad\n"))
print(f"Bienvenido {nombre}, tienes {edad} años.")

#Ejercicio 02
numero1 = int(input("Dime un número\n"))
numero2 = int(input("Dime otro número\n"))
suma = numero1 + numero2
resta = numero1 - numero2
multi = numero1* numero2
div = numero1 / numero2
print(f"Suma: {suma}\nResta: {resta}\nMulti: {multi}\nDiv: {div}")

#Ejercicio 03
numero3 = int(input("Dime un número\n"))
numero4 = int(input("Dime otro número\n"))
print(f"Son iguales: {numero3 == numero4}")

#Ejercicio 04
numero5 = int(input("Dime un número\n"))
numero6 = int(input("Dime otro número\n"))
print(f"Son divisibles?: {numero5 % numero6 == 0}")

#Ejercicio 05
numero7 = int(input("Dime un número para decirte el siguiente\n"))
numero7 += 1
print(f"El siguiente número es {numero7}")

#Ejercicio 06
numero8 = int(input("Dime un número\n"))
doble = numero8 * 2
triple = numero8 * 3
mitad = numero8 / 2
cuadrado = numero8 ** 2
raiz = math.sqrt(numero8)
print(f"Doble: {doble}\nTriple: {triple}\nMitad: {mitad}\nCuadrado: {cuadrado}\nRaiz: {raiz}")

#Ejercicio 07
numero9 = int(input("Dime un número\n"))
numero10 = int(input("Dime otro número\n"))
numero11 = int(input("Dime un número más\n"))
print(f"Son mayores que 0 : {numero9 > 0 and numero10 > 0 and numero11 > 0}")

#Ejercicio 08
nombre2 = input("Dime un nombre\n")
nombre3 = input("Dime otro nombre\n")
nombre4 = input("Dime otro nombre más\n")
print(f"Alguno es Juan? {nombre2 == "Juan" or nombre3 == "Juan" or nombre4 == "Juan"}")

#Ejercicio 09
numero12 = int(input("Dime un número\n"))
print(f"Es mayor o igual que 18 y menor que 65: {numero12 >= 18 and numero12 < 65}")

#Ejercicio 10
numero13 = int(input("Dime un número\n"))
numero14 = int(input("Dime otro número que no sea 0\n"))
entera = (numero13 / numero14)
decimal = numero13 // numero14
resto = numero13 % numero14
print(f"Entera: {entera}\nDecimal: {decimal}\nResto: {resto}")











'''
#01
nombre = input("Dime tu nombre\n")
edad = input("Dime tu edad\n")
print(f"Hola {nombre}, tienes {edad} años")

#02
num1 = float(input("Dime un número\n"))
num2 = float(input("Dime otro número\n"))
suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
div = num1 / num2
print(f"La suma es: {suma}\nLa resta es: {resta}\nLa multi es: {multi}\nLa división es: {div}")

#03
num3 = int(input("Dime un número\n"))
num4 = int(input("Dime otro número\n"))
print(f"Son iguales?: {num3==num4}")

#04
num5 = int(input("Dime un número\n"))
num6 = int(input("Dime otro número\n"))
resto = num5%num6
print(f"El primer número es divisible por el segundo?: {resto==0}")

#05
num7 = int(input("Dime un número\n"))
num7 += 1
print(f"Sumamos uno: {num7}")

#06
num8 = int(input("Dime un número\n"))
doble = num8 * 2
triple = num8 * 3
mitad = num8 / 2
cuadrado = num8 **2
raiz = math.sqrt(num8)
print(f"Su doble: {doble}\nSu triple: {triple}\nSu mitad: {mitad}\nSu cuadrado: {cuadrado}\nSu raiz: {raiz}")

#07
num9 = int(input("Dime un número\n"))
num10 = int(input("Dime otro número\n"))
num11 = int(input("Dime otro número\n"))
print(f"Son myores que 0: {num9>0 and num10>0 and num11>0}")

#08
name1 = input("Dime un nombre\n")
name2 = input("Dime otro nombre\n")
name3 = input("Dime otro nombre\n")
print(f"Alguno es Juan? {name1=="Juan" or name2=="Juan" or name3=="Juan"}")

#09
num12 = int(input("Dime un número\n"))
print(f"Es mayor o igual que 18 y menor que 65 el {num12}: {num12 >= 18 and num12<65}")

#10
num13 = int(input("Dime un número\n"))
num14 = int(input("Dime otro número\n"))
decimal = (num13 / num14)
entera = (num13//num14)
resto = (num13%num14)
print(f"Decimal {decimal}\nEntera {entera}\nResto {resto}")


edad10 = 10
print("Tengo", edad10,"años")
'''