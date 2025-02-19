def obtener_calificacion(mensaje):
    """Función para obtener una calificación válida entre 0 y 100"""
    while True:
        try:
            valor = float(input(mensaje))
            if 0 <= valor <= 100:
                return valor
            else:
                print("Por favor, ingrese una calificación válida (0-100).")
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Solicitar calificaciones de Matemática
examen_matematica = obtener_calificacion("Ingrese la calificación del examen de Matemática: ")
tarea1_matematica = obtener_calificacion("Ingrese la calificación de la primera tarea de Matemática: ")
tarea2_matematica = obtener_calificacion("Ingrese la calificación de la segunda tarea de Matemática: ")
tarea3_matematica = obtener_calificacion("Ingrese la calificación de la tercera tarea de Matemática: ")

# Solicitar calificaciones de Física
examen_fisica = obtener_calificacion("Ingrese la calificación del examen de Física: ")
tarea1_fisica = obtener_calificacion("Ingrese la calificación de la primera tarea de Física: ")
tarea2_fisica = obtener_calificacion("Ingrese la calificación de la segunda tarea de Física: ")

# Solicitar calificaciones de Química
examen_quimica = obtener_calificacion("Ingrese la calificación del examen de Química: ")
tarea1_quimica = obtener_calificacion("Ingrese la calificación de la primera tarea de Química: ")
tarea2_quimica = obtener_calificacion("Ingrese la calificación de la segunda tarea de Química: ")
tarea3_quimica = obtener_calificacion("Ingrese la calificación de la tercera tarea de Química: ")

# Cálculo de promedios por materia
promedio_matematica = (examen_matematica * 0.90) + ((tarea1_matematica + tarea2_matematica + tarea3_matematica) / 3 * 0.10)
promedio_fisica = (examen_fisica * 0.80) + ((tarea1_fisica + tarea2_fisica) / 2 * 0.20)
promedio_quimica = (examen_quimica * 0.85) + ((tarea1_quimica + tarea2_quimica + tarea3_quimica) / 3 * 0.15)

# Cálculo del promedio general
promedio_general = (promedio_matematica + promedio_fisica + promedio_quimica) / 3

# Mostrar resultados
print("\n--- Resultados Finales ---")
print(f"Promedio en Matemática: {promedio_matematica:.2f}")
print(f"Promedio en Física: {promedio_fisica:.2f}")
print(f"Promedio en Química: {promedio_quimica:.2f}")
print(f"Promedio General: {promedio_general:.2f}")