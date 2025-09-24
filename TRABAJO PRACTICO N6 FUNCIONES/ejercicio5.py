# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mos
#trar el resultado usando esta función.

def segundos_a_horas (segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60 
    segundosrestantes = segundos % 60
    print (f"si pasamos sus segundos a horas quedarian {horas} horas, {minutos} minutos y {segundosrestantes} segundos")
    
        