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
