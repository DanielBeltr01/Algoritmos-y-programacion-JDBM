# Leer el número de estudiantes
num_estudiantes = int(input("Ingrese el número de estudiantes: "))

# Inicializar la variable para la altura máxima
max_altura = 0

# Leer las alturas de los estudiantes y encontrar la mayor
for i in range(num_estudiantes):
    altura = float(input(f"Ingrese la altura del estudiante {i+1}: "))
    
    # Actualizar max_altura si la nueva altura es mayor
    if altura > max_altura:
        max_altura = altura

# Imprimir la altura más alta
print("La altura más alta es:", max_altura)