##1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad=int(input("coloque su edad: "))

if edad > 18: 
 print ("es mayor de edad")
else: 
 print ("es menor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
#mensaje “Desaprobado”. 

nota=int(input("coloque su nota: "))

if nota >= 6:
 print ("aprobado")
else:
 print ("desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
#operador de módulo (%) en Python para evaluar si un número es par o impar. 

par=int(input("ingrese solo numeros pares"))

if par % 2 == 0:
 print ("su numero es par")
else:
 print ("su numero es impar, porfavor ingrese uno par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
#siguientes categorías pertenece: 
#● Niño/a: menor de 12 años. 
#● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#● Adulto/a: mayor o igual que 30 años.

edad=int(input("escriba su edad: "))

if edad < 0:
    print("Coloque una edad real")
elif edad < 12:
    print("Es un niño")
elif edad < 18:
    print("Es un adolescente")
elif edad < 30:
    print("Es un adulto joven")
else:
    print("Es un adulto mayor")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
#como una lista o un string.

contraseña = (input ("escriba una contraseña que tenga entra 8 y 14 cararcteres "))

if 8 <= len(contraseña) <= 14:
    print ("su contraseña tiene ",len(contraseña), "caracteres es correcta")
elif len(contraseña) < 8: 
    print ("su contraseña es demasiado corta")
else:
    print ("su contraseña es demasiado larga")

#6 Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
#Definir la lista numeros_aleatorios de la siguiente forma: 
#import random 
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de 
#forma aleatoria. 

import statistics
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 

media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
modas = statistics.multimode(numeros_aleatorios)

if len(modas) == 1:
    moda = modas[0]
    if media > mediana and mediana > moda:
        sesgo = "Sesgo positivo (asimetría a la derecha)"
    elif media < mediana and mediana < moda:
        sesgo = "Sesgo negativo (asimetría a la izquierda)"
    else:
        sesgo = "No hay sesgo claro"
else:
    moda = modas
    sesgo = "No se puede determinar el sesgo porque hay varias modas"

print("Lista de números aleatorios:", numeros_aleatorios)
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda(s): {moda}")
print(f"Resultado: {sesgo}")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
#pantalla.

texto = input("Ingrese una frase o palabra: ")

ultima_letra = texto[-1]

if ultima_letra.lower() in "aeiou":
    texto + "!"

print(texto)


#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#lower() y title() de Python para convertir entre mayúsculas y minúsculas. 

nombre = input ("coloque su nombre ") 
numero = int(input("el numero 1 (mayusculas) el numero 2 (minusculas) y el numero 3 (la primera letra mayusculas) "))

if numero == 1:
   print (nombre.upper())
elif numero == 2:
   print (nombre.lower())
elif numero == 3:
   print (nombre.title())
else: 
   print ("seleccione una opcion correcta")






#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#por pantalla: 
#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
#débiles). 
#● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 

terremoto = float(input("coloque la magnitud del terremoto "))

if terremoto < 3:
   print ("Muy leve (imperceptible)")
elif terremoto < 4:
   print ("Leve (ligeramente perceptible)")
elif terremoto < 5:
   print ("Moderado (sentido por personas, pero generalmente no causa daños)")
elif terremoto < 6:
   print ("Fuerte (puede causar daños en estructuras débiles)")
elif terremoto < 7:
   print ("Muy fuerte (puede causar daños significativos)")
else: 
   print ("Extremo (puede causar graves daños a gran escala)")

#10 Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
#si el usuario se encuentra en otoño, invierno, primavera o verano. 

hemisferio = input("en que hemisferio se encuentre? norte o sur: ")
mes = int(input ("en que mes estas(1 al 12): "))
dia = int(input ("y en que dia estas(1 al 31): "))

if hemisferio == "norte":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia < 21):
        print ("invierno")
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia < 21):
        print ("primavera")
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia < 23):
        print ("verano")
    elif (mes == 9 and dia >= 23) or (mes in [10, 11]) or (mes == 12 and dia < 21):
        print ("otoño")
elif hemisferio == "sur":
    if (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia < 23):
        print ("invierno")
    elif (mes == 9 and dia >= 23) or (mes in [10, 11]) or (mes == 12 and dia < 21):
        print ("primavera")
    elif (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia < 21):
        print ("verano")
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia < 21):
        print ("otoño")
else:
   print("hemisferio invalido")



