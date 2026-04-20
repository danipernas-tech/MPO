#Escribe un programa que pida al usuario dos números enteros correspondientes a la casilla que está Pacman (1er número) y a la que está un fantasma (2o número), luego debe recibir un texto con el formato "normal" o "caramelo". Si el texto es "normal" y los números son iguales, el programa debe imprimir "Pacman ha sido atrapado". Si el texto es "caramelo" y los números son iguales, el programa debe imprimir "Pacman ha comido al fantasma". En cualquier otro caso, el programa debe imprimir "Pacman ha escapado".

pacman = int(input("Dime un número (casilla Pacman)\n"))
fantasma = int(input("Dime otro número (casilla fantasma)\n"))

if pacman == fantasma:
    estado = input("Dime el estado (normal o caramelo)\n")
    if estado == "normal":
        print("Pacman ha sido atrapado")
    elif estado == "caramelo":
        print("Pacman ha comido al fantasma")
else:
    print("Pacman ha escapado")

