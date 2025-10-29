# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad

with open("productos.txt", "w") as file:
    file.write("Manzana,0.50,100\n")
    file.write("Banana,0.30,150\n")
    file.write("Naranja,0.80,200\n")

# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30


def leer_productos():
    productos = []
    with open("productos.txt", "r") as file:
        for linea in file:
            nombre, precio, cantidad = linea.strip().split(",")
            productos.append(
                {"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)}
            )
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
    return productos


productos = leer_productos()

# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

nuevo_nombre = input("Ingrese el nombre del nuevo producto: ")
nuevo_precio = input("Ingrese el precio del nuevo producto: ")
nuevo_cantidad = input("Ingrese la cantidad del nuevo producto: ")

with open("productos.txt", "a") as file:
    file.write(f"{nuevo_nombre},{nuevo_precio},{nuevo_cantidad}\n")


# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.

# (Esto ya se hizo en la función leer_productos)

# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.

buscar_nombre = input("Ingrese el nombre del producto a buscar: ")
encontrado = False
for producto in productos:
    if producto["nombre"].lower() == buscar_nombre.lower():
        print(
            f"Producto encontrado: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}"
        )
        encontrado = True
        break

if not encontrado:
    print("Producto no encontrado.")

# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.

with open("productos.txt", "w") as file:
    for producto in productos:
        file.write(
            f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
        )


# Consejo final:
# Antes de empezar, analizá cada problema y pensá cómo dividirlo en partes:
# ● Leer archivo
# ● Procesar datos
# ● Mostrar o actualizar información
# ● Guardar los cambios
# Al terminar, probá tu programa varias veces:
# ● ¿Se puede agregar más de un producto?
# ● ¿Se guarda todo correctamente?
# ● ¿Se muestra bien el resultado?
