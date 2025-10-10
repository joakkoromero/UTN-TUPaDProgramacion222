#punto1
# Crear lista con los múltiplos de 4 entre 1 y 100
multiplos = []
for i in range(1, 101):
    if i % 4 == 0:
        multiplos.append(i)

print("Lista de múltiplos de 4:", multiplos)

#punto2
# Lista con cinco elementos
cosas = ["pizza", "guitarra", "auto", "helado", "montaña"]

# Mostrar el penúltimo elemento (posición -2)
print("El penúltimo elemento es:", cosas[-2])

#punto3
# Crear lista vacía
lista_vacia = []

# Agregar tres palabras
lista_vacia.append("sol")
lista_vacia.append("mar")
lista_vacia.append("arena")

print("Lista resultante:", lista_vacia)



#punto4
animales = ["perro", "gato", "conejo", "pez"]

# Reemplazar segundo (índice 1) y último (índice -1)
animales[1] = "loro"
animales[-1] = "oso"

print("Lista de animales modificada:", animales)


#punto 5
#1-Se crea una lista llamada numeros con los valores.[8, 15, 3, 22, 7].

#2-La función max(numeros) busca el número más grande dentro de la lista.En este caso, el máximo es 22.

#3-Luego, el método remove() elimina ese valor (el mayor) de la lista.
# Después de eliminar 22, la lista queda así:[8, 15, 3, 7]

#Finalmente, el print(numeros) muestra la lista resultante por pantalla.




#punto 6
# Lista con números del 10 al 30, de 5 en 5
numeros = list(range(10, 31, 5))

# Mostrar los dos primeros
print("Los dos primeros son:", numeros[0], "y", numeros[1])

#punto7
autos = ["sedan", "polo", "suran", "gol"]

# Reemplazar los índices 1 y 2
autos[1] = "fiesta"
autos[2] = "focus"

print("Lista de autos modificada:", autos)


#punto8

dobles = []

# Agregar los valores dobles
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print("Lista de dobles:", dobles)


#punto9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" al tercer cliente
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines"
compras[1][1] = "tallarines"

# c) Eliminar "pan" del primer cliente
del compras[0][0]

# d) Mostrar lista final
print("Lista de compras actualizada:", compras)


#punto10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print("Lista anidada:", lista_anidada)
