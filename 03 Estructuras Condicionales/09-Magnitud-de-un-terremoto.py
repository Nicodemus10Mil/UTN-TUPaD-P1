# Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla

# Pedimos al usuario que ingrese un número
magnitud = float(input("Ingrese la magnitud del terremoto: "))

# Implementamos estructura condicional

if magnitud < 3:
    print("'Muy leve'(imperceptible)")
elif magnitud >= 3 and magnitud < 4 :
    print("'Leve'(ligeramente perceptible)")
elif magnitud >= (4) and magnitud <5:
    print("'Moderado'(sentido por personas, pero generalmente no causa daños)")
elif magnitud >=5 and magnitud < 6:
    print("'Fuerte' (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("'Muy Fuerte' (puede causar daños significativos)")
elif magnitud >= 7:
    print("'Extremo' (puede causar graves daños a gran escala).")