# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas = {"Banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450}

print("lista de frutas y precios")
print(precios_frutas)

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print("lista actualizada con nuevas frutas y precios")
print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print("lista de precios actualizada")
print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.

frutas = list(precios_frutas.keys())
print("lista de frutas")
print(frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# # • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# # • Luego, pedí un nombre y mostrale el número asociado, si existe.
# Ejemplo:

contactos = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número telefónico: ")
    contactos[nombre] = numero

print("Contactos almacenados:")

for nombre, numero in contactos.items():
    print(f"{nombre}: {numero}")

nombre_consulta = input("Ingrese el nombre del contacto que desea consultar: ")

if nombre_consulta in contactos:
    print(f"El número de {nombre_consulta} es: {contactos[nombre_consulta]}")
else:
    print(f"No se encontró el contacto con el nombre {nombre_consulta}")


# # 5) Solicita al usuario una frase e imprime:
# # • Las palabras únicas (usando un set).
# # • Un diccionario con la cantidad de veces que aparece cada palabra.
# Ejemplo:

frase = input("Ingrese una frase: ")

palabras = frase.split()
palabras_unicas = set(palabras)

print("Palabras únicas:", palabras_unicas)

contador_palabras = {}

for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

print("Contador de palabras:", contador_palabras)


# # # 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# # Luego, mostrá el promedio de cada alumno.
# Ejemplo:

nombres_alumnos = []
notas_alumnos = {}
for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    nombres_alumnos.append(nombre)
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    notas_alumnos[nombre] = tuple(notas)

for nombre in nombres_alumnos:
    promedio = sum(notas_alumnos[nombre]) / len(notas_alumnos[nombre])
    print(f"El promedio de {nombre} es: {promedio:.2f}")


# # 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# # y Parcial 2:
# # • Mostrá los que aprobaron ambos parciales.
# # • Mostrá los que aprobaron solo uno de los dos.
# # • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_1 = {1, 2, 3, 4, 5}
parcial_2 = {4, 5, 6, 7, 8}

aprobados_ambos = parcial_1.intersection(parcial_2)
print("Estudiantes que aprobaron ambos parciales:", aprobados_ambos)

aprobados_solo_uno = parcial_1.symmetric_difference(parcial_2)
print("Estudiantes que aprobaron solo uno de los dos parciales:", aprobados_solo_uno)

aprobados_al_menos_uno = parcial_1.union(parcial_2)
print("Estudiantes que aprobaron al menos un parcial:", aprobados_al_menos_uno)


# # 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# # Permití al usuario:
# # • Consultar el stock de un producto ingresado.
# # • Agregar unidades al stock si el producto ya existe.
# # • Agregar un nuevo producto si no existe.

productos_stock = {"Manzanas": 50, "Bananas": 30, "Naranjas": 20}

print("Productos y sus stocks:")
for producto, stock in productos_stock.items():
    print(f"{producto}: {stock} unidades")


# # 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Ejemplo:

agenda = {
    ("Lunes", "10:00"): "Reunión con el equipo",
    ("Martes", "14:00"): "Cita médica",
    ("Miércoles", "09:00"): "Clase de yoga",
}
print("Agenda de eventos:")
for (dia, hora), evento in agenda.items():
    print(f"{dia} a las {hora}: {evento}")


# # 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# # diccionario donde:
# # • Las capitales sean las claves.
# # • Los países sean los valores.
# Ejemplo:

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Colombia": "Bogotá",
}
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print("Diccionario de capitales y países:")
print(capitales_paises)
