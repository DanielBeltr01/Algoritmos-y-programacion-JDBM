def obtener_metros():
    while True:
        try:
            metros = float(input("Ingrese la cantidad de metros: "))
            if metros < 0:
                print("Por favor, ingrese un valor positivo.")
            else:
                return metros
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Solicitar la cantidad de metros al usuario
metros = obtener_metros()

# Conversión de metros a pulgadas y pies
pulgadas_totales = metros * 39.37  # Corrección: el factor correcto es 39.37
pies = int(pulgadas_totales // 12)  # División entera para obtener pies completos
pulgadas_restantes = pulgadas_totales % 12  # Resto de la división para obtener pulgadas restantes

# Mostrar el resultado
print(f"La conversión es: {pies} pies y {pulgadas_restantes:.2f} pulgadas.")
