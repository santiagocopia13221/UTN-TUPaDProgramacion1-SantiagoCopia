#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
#dio como parámetro y devuelva el área del círculo. calcular_peri
#metro_circulo(radio) que reciba el radio como parámetro y devuel
#va el perímetro del círculo. Solicitar el radio al usuario y llamar am
#bas funciones para mostrar los resultados.

import math 

def calcular_area_circulo(radio):
    area = math.pi * (radio**2)
    print (f"el area del circulo es {area}")
    

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio 
    print (f"el perimetro del circulo es {perimetro}")

    
    