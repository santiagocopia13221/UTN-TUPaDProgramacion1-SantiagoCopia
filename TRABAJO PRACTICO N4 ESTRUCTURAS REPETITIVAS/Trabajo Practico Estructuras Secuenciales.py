#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

for i in range (101):
    print (i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene. 

numero = int(input("Ingrese un número entero: "))

cantidad_digitos = len(str(abs(numero)))

print("El número tiene", cantidad_digitos, "dígitos.")


#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores. 

numero1 = int(input("coloque el primer numero: "))
numero2 = int(input("coloque el segundo numero: "))

suma = 0 

if numero1 < numero2:
    for i in range (numero1+1, numero2):
        print (i)
        suma += i
elif numero1 > numero2:
    for i in range (numero2+1, numero1):
        print (i)
        suma += i

print(f"La suma de sus numeros es: {suma}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0. 

print ("coloque numeros enteros y al finalizar el programa se mostrara la suma de sus numeros")
print ("lo puede finalizar colocando un 0")

numero = int(input("coloque un numero distinto de 0: "))
suma = 0

while numero != 0 :
    suma = suma + numero 
    numero = int(input("coloque otro numero entero : "))

print (f"la suma de sus numeros es: {suma}")


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

import random
num = random.randint (0, 9)

intentos = 1
numero = int(input("adivine el numero aleatorio entre el 0 y el 9, se le contaran los intentos que haga: "))

while numero != num :
    intentos += 1 
    numero = int(input("incorrecto, coloque otro numero: "))

print (f"ADIVINASTE, tus intentos fueron {intentos}")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente. 

for i in range (99, 0, -1):
    print (i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario.

numero = int(input("coloque un numero entero positivo: "))

if numero < 0:
    numero = -numero
    print (f"su numero era negativo y como te pedi positivo te lo transformo en {numero}")

suma = 0

for i in range (0, numero):
     suma += i
    
print (f"la suma de los numeros que hay entre 0 y {numero} es de: {suma}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

cantidad = int(input("de cuantos numeros queres saber cuales son pares, cuántos son impares, " \
"cuántos son negativos y cuántos son positivos : "))
par = 0
impar = 0
negativo = 0
positivo = 0
neutro = 0 

for i in range (cantidad):
    numero = int(input(f"ingrese el numero {i+1}: "))

    if numero % 2 == 0:
        par += 1
    elif numero % 2 != 0:
        impar += 1

    if numero > 0:
        positivo += 1
    elif numero < 0:
        negativo +=1

print (f"Hay {par} numeros pares y {impar} numeros impares.") 
print (f"Tambien hay {positivo} numeros positivos y hay {negativo} numeros negativos.")


#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor). 

cantidad = int(input("ingrese de cuantos numeros quiere que le calcule la media: "))
suma = 0

for i in range (cantidad):
    numero = int(input(f"coloque el numero {i+1}: "))
    suma += numero  

promedio = suma / cantidad 
print (f"la media de todos sus numeros es de: {promedio}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

numero = int(input("Coloque un número: "))
invertido = int(str(abs(numero))[::-1])  
if numero < 0:
    invertido = -invertido               
print(f"Su número invertido es: {invertido}")
