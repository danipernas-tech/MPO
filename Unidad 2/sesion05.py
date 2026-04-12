
#ESTRUCTURAS DE CONTROL DE FLUJO

#Estructura if
edad = 22

if edad >= 18:
    print(f"Eres mayor de edad, tienes {edad} años")


#Estructura elif

if edad >=18:
    print(f"Eres mayor de edad, tienes {edad} años")
elif edad < 18:
    print("Eres menor de edad")


#Estructura else

if edad > 65:
    print(f"Eres muy mayor, tienes {edad} años")
elif edad >= 18:
    print("Eres menor de edad")
else:
    print("Eres menor de edad")


#ESTRUCTURAS DE CONTROL DE REPETICIÓN

#Bucle for

for i in range(5):
    print(i)

for i in range(0, 10, 2):
    print(i)

numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)

#Bucle while

numero2 = int(input("Introduce un numero: \n"))
suma = 0
while numero2 != 0:
    suma += numero2
    numero2 = int(input("Introduce otro número (0 para salir\n)"))
print("La suma es: ", suma)
