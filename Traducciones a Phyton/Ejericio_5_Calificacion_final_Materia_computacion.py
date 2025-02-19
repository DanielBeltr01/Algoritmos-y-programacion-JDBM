def obtener_calificacion(mensaje):
    while True:
        try:
            calificacion = float(input(mensaje))
            if 0 <= calificacion <= 100:
                return calificacion
            else:
                print("Por favor, ingrese una calificación entre 0 y 100.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Solicitar calificaciones al usuario
calificacion1 = obtener_calificacion("Calificación 1: ")
calificacion2 = obtener_calificacion("Calificación 2: ")
calificacion3 = obtener_calificacion("Calificación 3: ")
examenfinal = obtener_calificacion("Examen final: ")
trabajofinal = obtener_calificacion("Trabajo final: ")

# Calcular el promedio de las calificaciones
promedio_calificaciones = (calificacion1 + calificacion2 + calificacion3) / 3 

# Calcular la nota final con los pesos indicados
nota_final = (promedio_calificaciones * 0.55) + (examenfinal * 0.30) + (trabajofinal * 0.15)

# Mostrar el resultado
print(f"La nota final del alumno es: {nota_final:.2f}")