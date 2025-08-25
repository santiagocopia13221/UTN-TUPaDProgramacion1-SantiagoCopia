# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print ("hola mundo")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

nombre = input("Por favor, ingresa tu nombre: ")
print (f"Hola {nombre}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input("Por favor, ingresa tu nombre: ")
apellido = input("Por favor, ingresa tu apellido: ")  
edad = input("Por favor, ingresa tu edad: ")  
lugar_residencia = input("Por favor, ingresa tu lugar de residencia: ")

print (f"Soy {nombre} {apellido}, tengo {edad} y vivo en {lugar_residencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro

radio = int(input("coloque el radio de tu circulo"))
area = 3.14 * radio ** 2
perimetro = 2 * 3.14 * radio
print(f"el area de tu circulo es {area} y el perimetro es {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

segundos = int(input("dame una cantidad de segundos "))
horas = segundos // 3600
print (f"tus segundos equivalen a {horas} horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número

numero = int(input("coloque un numero "))

print (f"su numero multiplicado por 1 es {numero * 1}")
print (f"su numero multiplicado por 2 es {numero * 2}")
print (f"su numero multiplicado por 3 es {numero * 3}")
print (f"su numero multiplicado por 4 es {numero * 4}")
print (f"su numero multiplicado por 5 es {numero * 5}")
print (f"su numero multiplicado por 6 es {numero * 6}")
print (f"su numero multiplicado por 7 es {numero * 7}")
print (f"su numero multiplicado por 8 es {numero * 8}")
print (f"su numero multiplicado por 9 es {numero * 9}")
print (f"su numero multiplicado por 10 es {numero * 10}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1 = int(input("escribe un numero entero distinto de 0: "))
numero2 = int(input("escribe un numero entero distinto de 0: "))

suma = numero1 + numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2
resta = numero1 - numero2

print (f"la suma de sus numeros es {suma}")
print (f"la division de sus numeros es {division}")
print (f"la multiplicacion de sus numeros es {multiplicacion}")
print (f"la resta de sus numeros es {resta}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:

altura = float(input("coloque su altura "))
peso = int(input("coloque su peso "))

imc = peso / altura ** 2

print (f"su indice de masa corporal es de {imc}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

celsius = float(input("coloque la temperatura en grados celcius "))

farenheit = 9/5 * celsius + 32

print (f"el equivalente en grados farenheit de su temperatura es de {farenheit}")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números

num1 = int(input("coloque el primer numero: "))
num2 = int(input("coloque el segundo numero: "))
num3 = int(input("coloque el tercer numero: "))

total = num1 + num2 + num3
promedio = total / 3

print (f"el promedio de sus numeros es de {promedio}")
