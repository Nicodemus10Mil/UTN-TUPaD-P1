# escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

# Importamos "random" e importamos mode, median y mean desde statistics.
from statistics import mode, median, mean;
import random;

# Definimos una lista con 50 números aleatorios del 1 al 100.
numeros_aleatorios = {random.randint(1,100) for i in range(50)}
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
print(f"{media}, {mediana}, {moda}")

# Estructura de control que nos permite corroborar si hay sesgo positivo, negativo o no hay.
if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana and mediana == moda:
    print("Sin sesgo.")
else:
    print("No hay resultados concluyentes") #En caso de que no se cumplan las condiciones he añadido esta linea de aquí.