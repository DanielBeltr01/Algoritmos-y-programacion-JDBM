# Entrada de datos
lectura_anterior = float(input("Ingrese la lectura anterior del medidor en kWh: "))
lectura_actual = float(input("Ingrese la lectura actual del medidor en kWh: "))

# Validar que la lectura actual sea mayor a la anterior
if lectura_actual < lectura_anterior:
    print("Error: La lectura actual no puede ser menor a la anterior.")
else:
    # Calcular el consumo
    consumo = lectura_actual - lectura_anterior
    costo_total = 0

    # Aplicar tarifas según el consumo
    if consumo <= 100:
        costo_total = consumo * 4_600
    elif consumo <= 300:
        costo_total = (100 * 4_600) + ((consumo - 100) * 80_000)
    elif consumo <= 500:
        costo_total = (100 * 4_600) + (200 * 80_000) + ((consumo - 300) * 100_000)
    else:
        costo_total = (100 * 4_600) + (200 * 80_000) + (200 * 100_000) + ((consumo - 500) * 120_000)

    # Salida de resultados
    print("\nResumen de Facturación")
    print(f"Consumo total: {consumo} kWh")
    print(f"Monto total a pagar: ${costo_total:,.2f} COP")
