# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#Le pedimos al usuario que ingrese su edad y almacenamos en una variable
edad_usuario= int(input(f"Ingrese su edad: " ))

if edad_usuario > 18:  # Iniciamos el secuencia de control
    print("Es mayor de edad.") # Mostramos en pantalla en caso de que se cumpla la condición
else :
    print("No es mayor")
