
# Solicitamos al usuario que ingrese el hemisferio, día y mes 
hemisferio= str(input("Ingrese N para el hemisferio Norte ó S para el hemisferio Sur: "))
dia = int(input("Ingrese el número del día: "))
mes = int(input("Ingrese el mes: "))


# Estructura condicional, según la fecha y hemisferio se devolvera una estación
if (mes == 12 and dia >=21 ) or (mes in [1,2]) or (mes == 3 and dia <=20):
    if hemisferio.lower() in "s":
        estacion = "Verano"
    elif hemisferio.lower() in "n":
        estacion = "Invierno"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    if hemisferio.lower() in "s":
        estacion = "Otoño"
    elif hemisferio.lower() in "n":
        estacion = "Primavera"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    if hemisferio.lower() in "s":
        estacion = "Invierno"
    elif hemisferio.lower() in "n":
        estacion = "Verano"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    if hemisferio.lower() in "s":
        estacion = "Primavera"
    elif hemisferio.lower() in "n":
        estacion = "Otoño"

# Imprimimos el resultado por pantalla
print(f"Estamos en la estación: {estacion}")