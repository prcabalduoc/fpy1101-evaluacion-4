# ----------------------------------------------------------------------
# FUNCIONES DE VALIDACIÓN
# ----------------------------------------------------------------------

def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_copias(copias_texto):
    try:
        copias = int(copias_texto.strip())
    except ValueError:
        return False
    return copias >= 0

def validar_prestamo(prestamo_texto):
    try:
        prestamo = int(prestamo_texto.strip())
    except ValueError:
        return False
    return prestamo > 0

# ----------------------------------------------------------------------
# FUNCIONES DEL MENÚ
# ----------------------------------------------------------------------

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        opcion_texto = input("Seleccione una opción (1-6): ").strip()
        try:
            opcion = int(opcion_texto)
        except ValueError:
            print("Opción inválida. Debe ingresar un número entre 1 y 6.")
            continue

        if 1 <= opcion <= 6:
            return opcion
        print("Opción inválida. Debe ingresar un número entre 1 y 6.")

# ----------------------------------------------------------------------
# OPCIÓN 1 - AGREGAR LIBRO
# ----------------------------------------------------------------------

def agregar_libro(libros):
    titulo = input("Ingrese el título del libro: ").strip()
    if not validar_titulo(titulo):
        print("Error: el título no puede estar vacío ni ser solo espacios en blanco.")
        return

    copias_texto = input("Ingrese la cantidad de copias: ").strip()
    if not validar_copias(copias_texto):
        print("Error: las copias deben ser un número entero mayor o igual que cero.")
        return

    prestamo_texto = input("Ingrese el período de préstamo (días): ").strip()
    if not validar_prestamo(prestamo_texto):
        print("Error: el período de préstamo debe ser un número entero mayor que cero.")
        return

    libro = {
        "titulo": titulo,
        "copias": int(copias_texto),
        "prestamo": int(prestamo_texto),
        "disponible": False
    }
    libros.append(libro)
    print(f"Libro '{titulo}' agregado correctamente.")

# ----------------------------------------------------------------------
# OPCIÓN 2 - BUSCAR LIBRO
# ----------------------------------------------------------------------

def buscar_libro(libros, titulo):
    for posicion in range(len(libros)):
        if libros[posicion]["titulo"] == titulo:
            return posicion
    return -1

def opcion_buscar_libro(libros):
    titulo = input("Ingrese el título del libro a buscar: ")
    posicion = buscar_libro(libros, titulo)
    if posicion != -1:
        libro = libros[posicion]
        print(f"\nLibro encontrado en la posición {posicion}:")
        print(f"Título: {libro['titulo']}")
        print(f"Copias: {libro['copias']}")
        print(f"Préstamo: {libro['prestamo']}")
        print(f"Disponible: {libro['disponible']}")
    else:
        print(f"El libro '{titulo}' no se encuentra registrado.")

# ----------------------------------------------------------------------
# OPCIÓN 3 - ELIMINAR LIBRO
# ----------------------------------------------------------------------

def eliminar_libro(libros):
    titulo = input("Ingrese el título del libro a eliminar: ")
    posicion = buscar_libro(libros, titulo)
    if posicion != -1:
        libros.pop(posicion)
        print(f"Libro '{titulo}' eliminado correctamente.")
    else:
        print(f"El libro '{titulo}' no se encuentra registrado.")

# ----------------------------------------------------------------------
# OPCIÓN 4 - ACTUALIZAR DISPONIBILIDAD
# ----------------------------------------------------------------------

def actualizar_disponibilidad(libros):
    for libro in libros:
        if libro["copias"] >= 1:
            libro["disponible"] = True
        else:
            libro["disponible"] = False

# ----------------------------------------------------------------------
# OPCIÓN 5 - MOSTRAR LIBROS
# ----------------------------------------------------------------------

def mostrar_libros(libros):
    actualizar_disponibilidad(libros)

    print("\n=== LISTA DE LIBROS ===")
    if not libros:
        print("No hay libros registrados.")
        return

    for libro in libros:
        estado = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"
        print(f"Título: {libro['titulo']}")
        print(f"Copias: {libro['copias']}")
        print(f"Préstamo: {libro['prestamo']}")
        print(f"Estado: {estado}")
        print("*" * 45)

# ----------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ----------------------------------------------------------------------

libros = []  # Colección general de libros (lista de diccionarios)

while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_libro(libros)
    elif opcion == 2:
        opcion_buscar_libro(libros)
    elif opcion == 3:
        eliminar_libro(libros)
    elif opcion == 4:
        actualizar_disponibilidad(libros)
        print("Disponibilidad actualizada para todos los libros.")
    elif opcion == 5:
        mostrar_libros(libros)
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break
