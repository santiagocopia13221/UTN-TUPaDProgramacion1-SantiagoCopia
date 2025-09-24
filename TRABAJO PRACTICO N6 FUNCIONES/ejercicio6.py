# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la fun
#ción.

def tabla_multiplicar(numero):
    for i in range (1, 11):
        multiplicacion = numero * i 
        print (f"{numero} multiplicado por {i} es {multiplicacion} ")