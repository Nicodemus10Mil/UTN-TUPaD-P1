# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.



# Pedimos la contraseña al usuario
contraseña = str(input("Ingrese una contraseña de entre 8 y 14 carácteres: "))

# Comparamos si la cantidad de carácteres de la variable "contraseña" en una estructura de control
if len(contraseña) >= 8 and len(contraseña) <= 14:
    # En caso de cumplir con la condición se imprimirá un mensaje afirmativo.
    print("Ha ingresado una contraseña correcta!")
else:
    # En caso de no cumplir con lo solicitado, se vuelve a solicitar.
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

