#Escribe un programa que pida un rol y una academia de estudios, si el rol es "alumno" y la academia es "Prometeo" el programa debe darle acceso al servidor de Discord oficial y al de los alumnos, donde se critica a los profes. Si el rol es "profesor" y la academia es "Prometeo" el programa debe darle acceso al servidor de Discord oficial, pero no al de los alumnos. En cualquier otro caso, el programa debe imprimir "No tienes acceso al servidor de Discord".

rol = input("Dime un rol (Alumno/Profesor)\n")
academia = input("Dime la academia (Prometeo)\n")

if academia == "Prometeo":
    if rol == "Alumno":
        print("Acceso servidor discord oficial y alumnos")
    elif rol == "Profesor":
        print("Acceso servidor discord oficial")
else:
    print("No tienes acceso al servidor de Discord")

