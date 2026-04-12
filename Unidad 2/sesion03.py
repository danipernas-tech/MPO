
#Ejercicios unidad 01 clase

print("Dime la temperatura en la que estas cocinando el pollo\n")
temperatura = float(input())

# 0-60 no se cocina
# 60 -200 optima
# >200 se quema
if temperatura > 200.0:
    print("Se quema")
elif temperatura > 60.0:
    print("Se quema")
elif temperatura < 60.0:
    print("No se cocina")