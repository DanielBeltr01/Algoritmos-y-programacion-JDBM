def obtener_monto():
    while True:
        try:
            inversion = float(input("Introduce el monto de la inversión: "))
            if inversion < 0:
                print("Por favor, ingrese un valor positivo.")
            else:
                return inversion
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Solicitar inversión
inversion = obtener_monto()

# Calcular el 2% de rendimiento
rendimiento = inversion * 0.02

# Mostrar el resultado
print(f"El resultado del 2% para una inversión de {inversion:} en un mes es {rendimiento:}")