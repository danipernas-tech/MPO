#FOR
# for variable in secuencia:
#     # Bloque de código a repetir
#     instrucciones

frutas = ["manzana", "banana", "naranja"] #Lista

for i in frutas:
    print(i)

#WHILE
#while condicion:
    # Bloque de código a repetir
    #instrucciones
    
contador = 0
while contador < 5:
    print(contador)
    contador += 1

#BREAK
contador = 0

while True: 
	print(contador)
	contador += 1
	if contador == 5:
		break

#CONTINUE
for i in range(10):
	if i % 2 == 0:
		continue
	print(i)

#PASS
for i in range(5):
    pass