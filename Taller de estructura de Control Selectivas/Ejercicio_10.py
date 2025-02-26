# Entrada de datos
categoria = int(input("Ingrese la categoría del trabajador (1-5): "))

# Definición de los aumentos y sueldos por categoría
aumentos = {1: 0.10, 2: 0.15, 3: 0.20, 4: 0.40, 5: 0.60}
sueldos_brutos = {1: 5000000, 2: 4300000, 3: 3600000, 4: 2000000, 5: 900000}

# Verificación de categoría válida
if categoria in aumentos:
    sueldo_bruto = sueldos_brutos[categoria]
    aumento = sueldo_bruto * aumentos[categoria]
    nuevo_sueldo = sueldo_bruto + aumento

    # Salida de resultados
    print("\n--- Resumen del salario ---")
    print(f"Categoría del trabajador: {categoria}")
    print(f"Sueldo bruto anterior: ${sueldo_bruto:,.2f} COP")
    print(f"Aumento aplicado: {aumentos[categoria]*100:.0f}%")
    print(f"Nuevo sueldo bruto: ${nuevo_sueldo:,.2f} COP")
else:
    print("Categoría no válida. Ingrese un número entre 1 y 5.")