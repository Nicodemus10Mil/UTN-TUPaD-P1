# ) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

# Solicitamos el parametro "Edad"
edad = int(input("Ingrese su edad: "))

# Iniciamos estructura de control
# Caso Niño
if edad >= 0 and edad < 12:
    print("Categoría: Niño/a")
# caso Adolescente
elif edad >= 12 and edad < 18:
    print("Categoría: Adolescente")
# Caso Adulto joven
elif edad >= 18 and edad < 30:
    print("Categoría: Adulto/a joven")
# Caso Adulto
elif edad >= 30:
    print("Categoría: Adulto/a")