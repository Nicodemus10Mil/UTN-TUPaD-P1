# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar

# Pedimos al usuario que ingrese un número
num = int(input("Ingrese un número para la comprobación de numeros pares: "))

# Iniciamos estructura de control
if num % 2 == 0:
    # En caso de ser par, mostrar el siguiente mensaje:
    print("Ha ingresa un número par.")
else:
    # De lo contrario mostrará el siguiente:
    print("Por favor, ingrese un número par. ")
