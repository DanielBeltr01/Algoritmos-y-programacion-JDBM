def obtener_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero < 0:
                print("Por favor, ingrese un número positivo.")
            else:
                return numero
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

# Solicitar datos al usuario
total_de_estudiantes = obtener_numero("Total de estudiantes: ")

# Validar que haya al menos un estudiante
if total_de_estudiantes == 0:
    print("No hay estudiantes en el grupo.")
else:
    cantidadhombre = obtener_numero("Cantidad de hombres: ")
    cantidadmujeres = obtener_numero("Cantidad de mujeres: ")

    # Validar que la suma de hombres y mujeres coincida con el total
    if cantidadhombre + cantidadmujeres