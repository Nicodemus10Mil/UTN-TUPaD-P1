# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla.

# Solicitamos al usuario que ingrese su nombre en una variable
nombre = str(input("Ingrese su nombre: "))
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")

# El usuario elige la opción
numero = int(input("Ingrese 1, 2 ó 3: "))

# Aplicamos la estructura condicional. Según sea el caso, se imprimira el nombre aplicando un método pertinente.

if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
elif numero == 3:
    print(nombre.title())
else:
    print("El número ingresado es incorrecto. Ingrese otro, por favor")