#) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

#Solicitamos al usuario que ingrese una nota y la almacenamos en una variable llamada nota
nota = float(input("Ingrese la nota de su examen: ")); 

# Iniciamos estructura condicional
# En caso de cumplirse la condición imprimimos "Aprobado"
if nota >= 6:
    print("Aprobado");

# Caso contrario imprimimos "Desaprobado"
else:
    print("Desaprobado")