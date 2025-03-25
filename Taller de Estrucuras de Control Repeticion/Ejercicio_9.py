# Inicializar variables
total_estudiantes = 0
suma_puntajes = 0
estudiante_max = ""
puntaje_max = float('-inf')
estudiante_min = ""
puntaje_min = float('inf')
puntajes = []

# Bucle para ingresar datos
while True:
    nombre = input("Ingrese el nombre del estudiante: ").strip()
    puntaje = float(input("Ingrese el puntaje del estudiante: "))

    # Sumar puntajes y contar estudiantes
    suma_puntajes += puntaje
    total_estudiantes += 1
    puntajes.append(puntaje)

    # Verificar puntaje máximo
    if puntaje > puntaje_max:
        puntaje_max = puntaje
        estudiante_max = nombre

    # Verificar puntaje mínimo
    if puntaje < puntaje_min:
        puntaje_min = puntaje
        estudiante_min = nombre

    # Preguntar si se desea continuar
    continuar = input("¿Desea ingresar otro estudiante? (Sí/No): ").strip().lower()
    if continuar == "no":
        break

# Verificar que hay datos antes de calcular estadísticas
if total_estudiantes > 0:
    # Calcular promedio
    promedio = suma_puntajes / total_estudiantes

    # Calcular porcentajes de estudiantes por debajo y por encima del promedio
    inferiores = sum(1 for p in puntajes if p < promedio)
    superiores = sum(1 for p in puntajes if p > promedio)
    porcentaje_inferiores = (inferiores / total_estudiantes) * 100
    porcentaje_superiores = (superiores / total_estudiantes) * 100

    # Mostrar resultados
    print("\nResultados:")
    print(f"Estudiante con el puntaje más alto: {estudiante_max} ({puntaje_max})")
    print(f"Estudiante con el puntaje más bajo: {estudiante_min} ({puntaje_min})")
    print(f"Puntaje máximo obtenido: {puntaje_max}")
    print(f"Puntaje mínimo obtenido: {puntaje_min}")
    print(f"Promedio de todos los puntajes: {promedio:.2f}")
    print(f"Porcentaje de estudiantes con puntajes inferiores al promedio: {porcentaje_inferiores:.2f}%")
    print(f"Porcentaje de estudiantes con puntajes superiores al promedio: {porcentaje_superiores:.2f}%")
else:
    print("No se ingresaron datos.")