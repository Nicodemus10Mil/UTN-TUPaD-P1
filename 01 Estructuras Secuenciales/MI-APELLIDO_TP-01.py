# Trabajo práctico 1: Estructuras secuenciales
# Estudiante: Paz Isaías Nicolás
import math

# Actividad 1 : Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

# Actividad 2: Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

nombre = str(input("Ingrese su nombre: "))
print(f"Hola {nombre}!")

# Actividad 3: Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre2 = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
lugar_de_residencia = str(input("Ingrese su lugar de residencia: "))

print(f"Soy {nombre2} {apellido}, tengo {edad} y vivo en {lugar_de_residencia} ")

# Actividadad 4: Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro

# Asignamos el valor de las variables
radio = float(input("Ingrese el radio del circulo: "))
pi = math.pi

# Hacemos los cálculos 
area = pi * (radio * radio)
perimetro = 2 * radio * pi 

# Imprimimos
print(f"El área del circulo es {area} y su perímetro es {perimetro}")

# Actividad 5: Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundos = float(input("Ingrese la cantidad de segundos: "))

horas = segundos / 3600

print(f"Equivale a {horas} horas")

# Actividad 6: Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

numero = int(input("Ingrese número para saber la tabla: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero}x{i}={resultado}")

# Actividad 7: Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos

num1 = int(input("Ingrese un entero distinto a 0: "))
num2 = int(input("Ingrese otro: "))

if num1 != 0 and num2 != 0:
    suma = num1 + num2
    division = num1 / num2
    multiplicación = num1 * num2
    resta = num1 - num2
    print(f"Los resultados son: suma= {suma}, resta= {resta}, división= {division}, multiplicación= {multiplicación}")
else:
    print("Uno o ambos números ingresados son distintos de 0")
    
# Actividad 8: Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.

peso_en_kg = float(input("Ingrese su peso en Kg: "))
altura_en_m = float(input("Ingrese su altura en metros: "))

imc = peso_en_kg / (altura_en_m * altura_en_m)

print(f"Su índice de masa corporal es: {imc}")

# Actividadd 9: Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit.

grados_celcius = int(input("Ingrese la temperatura en grados celcius: "))

grados_fahrenheit = (9 / 5) * grados_celcius + 32

print(f"Su equivalente en Fahrenheit es: {grados_fahrenheit}")

# Actividad 10: Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

num3= float(input("Ingrese un número: "))
num4= float(input("Ingrese un número: "))
num5= float(input("Ingrese un número: "))
promedio = (num3 + num4 + num5) / 3

print(f"El promedio de los tres números ingresados es: {promedio}")