def obtener_precio():
    while True:
        try:
            precio_original = float(input("Ingrese el precio de la compra: "))
            if precio_original < 0:
                print("Por favor, ingrese un precio válido (número positivo).")
            else:
                return precio_original
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Solicitar el precio al usuario
precio_original = obtener_precio()

# Calcular descuento y precio final
descuento = precio_original * 0.15
precio_final = precio_original - descuento

# Mostrar los resultados
print(f"El descuento aplicado es: {descuento:.2f}")
print(f"El precio final a pagar es: {precio_final:.2f}")