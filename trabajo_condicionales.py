#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#solicitar la edad del usuario
edad= int(input ("ingrese su edad:"))
if edad > 18:
    print ("eres mayor de edad")
    
#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

nota= float(input("ingrese su nota:"))
if nota >= 6:
    print ("estas aprobado")
else:
    print("estas desaprobado")    

#Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

numero= int(input("ingrese un numero:"))
if (numero % 2 ==0):
    print ("numero par")
else:
    print("numero impar ")


#Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:

edad_numero= int(input("ingrese su edad:"))
if  edad_numero < 12:
    print ("eres un niño/a.")
elif edad_numero >= 12 and edad_numero < 18:
    print ("eres un adolecente.")
elif edad_numero >= 18 and edad_numero <30:
    print ("eres adulto/a.")        
else:
    print ("eres mayor.")

#Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#  incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

contraseña= input("por favor ingrese una contraseña que contenga entre 8 y 14 caracteres:" )
if 8<= len(contraseña) <=14:
    print ("usted ha ingresado una contraseña correcta")
else:
    print("por favor ingrese una contraseña de entra 8 y 14 caracteres")    


#punto 6

import random
from statistics import mode, median, mean


numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda= mode (numeros_aleatorios)
mediana= median (numeros_aleatorios)
media= mean(numeros_aleatorios)

if media > mediana > moda:
    print("sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("sin sesgo")
else:
    print("no se puede determinar si esta funcion tiene sesgo o no")





#punto 7
texto = input("Ingresa una frase o palabra: ")

if texto[-1].lower() in "aeiou":
    texto += "!"

print("Resultado:", texto)  


#punto8
# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingresa tu nombre: ")

print("Elige una opción:")
print("1. Convertir a MAYÚSCULAS")
print("2. Convertir a minúsculas")
print("3. Primera letra en mayúscula")

opcion = input("Ingresa 1, 2 o 3: ")

if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción inválida. Debes ingresar 1, 2 o 3.")


#punto 9

magnitud = float(input("Ingresa la magnitud del terremoto: "))

    # Clasifica según la escala de Richter
if magnitud < 3:
    print("Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else: 
    print("Extremo (puede causar graves daños a gran escala).")


#punto 10
hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
mes = int(input("¿En qué mes estamos? (1-12): "))
dia = int(input("¿Qué día del mes es hoy? (1-31): "))


if hemisferio not in ['N', 'S'] or not (1 <= mes <= 12) or not (1 <= dia <= 31):
    print("Datos inválidos. Verifica que el hemisferio sea 'N' o 'S', el mes entre 1 y 12, y el día entre 1 y 31.")
else:
    
    fecha = (mes, dia)

    
    if hemisferio == 'N':
        if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
            estacion = "Invierno"
        elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
            estacion = "Primavera"
        elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
            estacion = "Verano"
        else:  
            estacion = "Otoño"
    else:  
        if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
            estacion = "Verano"
        elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
            estacion = "Otoño"
        elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
            estacion = "Invierno"
        else:  
            estacion = "Primavera"


    print(f"En el hemisferio {'Norte' if hemisferio == 'N' else 'Sur'}, en la fecha {dia}/{mes}, estás en {estacion}.")
