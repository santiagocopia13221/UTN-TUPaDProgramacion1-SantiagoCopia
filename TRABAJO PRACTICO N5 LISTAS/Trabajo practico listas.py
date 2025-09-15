#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función 
#range.

numeros = list(range(4, 101, 4))
print (numeros)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el 
#penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el 
#indexing con números negativos! 

elementos = ["madera", "metal", "cobre", "oro", "cristal"]
print (elementos[3])

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por 
#pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por 
#ejemplo: 
#lista_vacia = [] 

lista = [] 

for i in range (1,4):
    lista.append(input(f"coloque el elemento numero {i}: "))

print (lista)


#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
#respectivamente.  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra 
#en los videos o bien investigar cómo funciona el indexing con números negativos! 
"""animales = ["perro", "gato", "conejo", "pez"]"""

animales = ["perro", "gato", "conejo", "pez"]
print (animales)

animales[1] = "loro"
animales[3] = "oso"
print (animales)


#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
"""numero = [8, 15, 3, 22, 7]
numero.remove(max(numeros))
print (numeros)"""


"""Lo que pasa en ese codigo es que realmente tiraria un error pq (numeros) no existe, pero en el caso de que se corrija
la funcion (numero.remove)eliminaria un numero y (max) hace que eliminen al numero mas alto"""

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por 
#pantalla los dos primeros. 

numeros = list(range(10,35,5))
print (numeros)

print (numeros[0])
print (numeros[1])

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores 
#cualesquiera. 
"""autos = ["sedan", "polo", "suran", "gol"]""" 

autos = ["sedan", "polo", "suran", "gol"]
print("Autos originales:", autos)

nuevos = input("Coloque 2 autos que le gusten, separados por espacio: ").split()

autos[1:3] = nuevos

print("Autos actualizados:", autos)


#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append 
#directamente. Imprimir la lista resultante por pantalla. 

dobles = []
dobles.append(2*5)
dobles.append(10*2)
dobles.append(15*2)
print (dobles)


#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por 
#diferentes clientes: 
"""#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 
#a) Agregar "jugo" a la lista del tercer cliente usando append. 
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
#c) Eliminar "pan" de la lista del primer cliente.  
#d) Imprimir la lista resultante por pantalla """

compras = [
    ["pan", "leche"], 
    ["arroz", "fideos", "salsa"], 
    ["agua"]
]
print (compras)

compras[2].append("Jugo")
print (compras)

compras[1][1] = ("tallarines")
print (compras)

compras[0].remove ("pan")
print (compras)


#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
"""● Posición lista_anidada[0]: 15 
● Posición lista_anidada[1]: True 
● Posición lista_anidada[2][0]: 25.5 
● Posición lista_anidada[2][1]: 57.9 
● Posición lista_anidada[2][2]: 30.6 
● Posición lista_anidada[3]: False 
Imprimir la lista resultante por pantalla."""

listaanidada = [
    15, 
    True, 
    [25.5, 57.9, 30.6], 
    False 
] 

print (listaanidada)

print (f"La posicion [0] es: {listaanidada[0]}")
print (f"La posicion [1] es: {listaanidada[1]}")
print (f"La posicion [2][0] es: {listaanidada[2][0]}")
print (f"La posicion [2][1] es: {listaanidada[2][1]}")
print (f"La posicion [2][2] es: {listaanidada[2][2]}")
print (f"La posicion [3] es: {listaanidada[3]}")
