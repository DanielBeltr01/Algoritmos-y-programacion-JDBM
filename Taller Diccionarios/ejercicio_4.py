estudiantes = {}
max_estudiantes = 10

print("Introduzca los datos de hasta 10 estudiantes.\n")

for i in range(1, max_estudiantes + 1):
    print(f"Estudiante {i}:")
    nombre = input("Nombre: ")
    
    while True:
        try:
            nota = float(input("Nota: "))
            if 0 <= nota <= 10:
                break
            else:
                print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Por favor, introduzca un número válido.")
    
    estudiantes[str(i)] = {
        "nombre": nombre,
        "nota": nota
    }
    
    continuar = input("¿Desea añadir otro estudiante? (s/n): ").lower()
    if continuar != "s":
        break

aprobados = []
suspensos = []
suma_notas = 0

for est in estudiantes.values():
    suma_notas += est["nota"]
    if est["nota"] >= 5:
        aprobados.append(est["nombre"])
    else:
        suspensos.append(est["nombre"])

media = suma_notas / len(estudiantes)

print("\n--- Resultados ---")
print("Aprobados:", ", ".join(aprobados) if aprobados else "Ninguno")
print("Suspensos:", ", ".join(suspensos) if suspensos else "Ninguno")
print(f"Nota media de la clase: {media:.2f}")