import math

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