# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Ingresá un número: "))

for i in range(1, num + 1):
    print(f"Factorial de {i} = {factorial(i)}")


# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.


def fibonacci(n):
    if n <= 1:  # casos base
        return n
    else:  # caso recursivo
        return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("Hasta qué posición querés la serie: "))

for i in range(num):
    print(fibonacci(i), end=" ")

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un
# algoritmo general.


def potencia(base, exp):
    if exp == 0:  # caso base
        return 1
    else:  # caso recursivo
        return base * potencia(base, exp - 1)


b = int(input("Base: "))
e = int(input("Exponente: "))
print(f"{b}^{e} =", potencia(b, e))


# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
# unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
# procedimiento:
# 1. Dividir el número por 2.
# 2. Guardar el resto (0 o 1).
# 3. Repetir el proceso con el cociente hasta que llegue a 0.
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
# Convertir el número 10 a binario:
# 10 ÷ 2 = 5     resto: 0
#  5 ÷ 2 = 2     resto: 1
#  2 ÷ 2 = 1     resto: 0
#  1 ÷ 2 = 0     resto: 1
# Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".


def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)


num = int(input("Número decimal: "))
print("Binario:", decimal_a_binario(num))


# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
#      Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().


def es_palindromo(palabra):
    if len(palabra) <= 1:  # caso base
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


texto = input("Palabra: ")
print("Es palíndromo:", es_palindromo(texto))


# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
#      Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234)   → 10  (1 + 2 + 3 + 4)
# suma_digitos(9)      → 9
# suma_digitos(305)    → 8   (3 + 0 + 5)


def suma_digitos(n):
    if n < 10:  # caso base
        return n
    else:  # caso recursivo
        return n % 10 + suma_digitos(n // 10)


num = int(input("Número: "))
print("Suma de dígitos:", suma_digitos(num))


# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.

# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.

#       Ejemplos:
# contar_bloques(1)   → 1         (1)
# contar_bloques(2)   → 3         (2 + 1)
# contar_bloques(4)   → 10        (4 + 3 + 2 + 1)


def contar_bloques(n):
    if n == 1:  # caso base
        return 1
    else:
        return n + contar_bloques(n - 1)


niveles = int(input("Bloques en el nivel más bajo: "))
print("Total de bloques:", contar_bloques(niveles))


# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
#       Ejemplos:
# contar_digito(12233421, 2)   → 3
# contar_digito(5555, 5)       → 4
# contar_digito(123456, 7)     → 0


def contar_digito(numero, digito):
    if numero == 0:  # caso base
        return 0
    else:
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)


num = int(input("Número: "))
d = int(input("Dígito a contar: "))
print("Aparece", contar_digito(num, d), "veces.")
