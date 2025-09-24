#1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

print ("EJERCICIO 1")
from ejercicio1 import imprimir_hola_mundo

imprimir_hola_mundo()

print ("-----------------------------------------------------------------")

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
#volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

print ("EJERCICIO 2")
from ejercicio2 import saludar_usuario

nombre = (input("Coloque su nombre: "))
saludar_usuario(nombre)

print ("-----------------------------------------------------------------")

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
#dir los datos al usuario y llamar a esta función con los valores in
#gresados

print ("EJERCICIO 3")
from ejercicio3 import informacion_personal

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

print ("-----------------------------------------------------------------")

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
#dio como parámetro y devuelva el área del círculo. calcular_peri
#metro_circulo(radio) que reciba el radio como parámetro y devuel
#va el perímetro del círculo. Solicitar el radio al usuario y llamar am
#bas funciones para mostrar los resultados.

print ("EJERCICIO 4")
from ejercicio4 import calcular_area_circulo
from ejercicio4 import calcular_perimetro_circulo

radio = float(input("coloque el radio de su circulo para que le digamos el area y perimetro: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

print ("-----------------------------------------------------------------")

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mos
#trar el resultado usando esta función.

print ("EJERCICIO 5")
from ejercicio5 import segundos_a_horas

segundos = int(input("coloque la cantidad de segundos que quiera pasar a horas: "))
segundos_a_horas (segundos) 

print ("-----------------------------------------------------------------")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la fun
#ción.

print ("EJERCICIO 6")
from ejercicio6 import tabla_multiplicar

numero = int (input("coloque un numero: "))

tabla_multiplicar(numero)

print ("-----------------------------------------------------------------")

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resulta
#do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
#sultados de forma clara.

print ("EJERCICIO 7")
from ejercicio7 import operaciones_basicas

a = int(input("coloque el primer numero: "))
b = int(input("coloque el segundo numero: "))

tupla = operaciones_basicas(a, b)

print(f"Suma: {tupla[0]}")
print(f"Resta: {tupla[1]}")
print(f"Multiplicación: {tupla[2]}")
print(f"División: {tupla[3]}")


print ("-----------------------------------------------------------------")

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
#ción para mostrar el resultado con dos decimales.

print ("EJERCICIO 8")
from ejercicio8 import calcular_imc

peso = float (input("coloque su peso en kilogramos: "))
altura = float (input("coloque su altura en metros: "))

calcular_imc (peso, altura)

print ("-----------------------------------------------------------------")

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

print ("EJERCICIO 9")
from ejercicio9 import celsius_a_fahrenheit

celsius = float (input("coloque la temperatura en grados Celsius: "))
celsius_a_fahrenheit (celsius)

print ("-----------------------------------------------------------------")

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función

print ("EJERCICIO 10")
from ejercicio10 import calcular_promedio

a = int(input("coloque el primer numero: "))
b = int(input("coloque el segundo numero: "))
c = int(input("coloque el tercer numero: ")) 

promedio = calcular_promedio (a,b,c)
print (f"el promedio de los 3 es de {promedio}")

print ("-----------------------------------------------------------------")