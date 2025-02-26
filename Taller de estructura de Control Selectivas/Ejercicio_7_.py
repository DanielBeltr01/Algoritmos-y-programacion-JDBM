# Entrada de datos
distancia = float(input("Ingrese la distancia recorrida en km: "))

# Cálculo del costo según las condiciones
if distancia <= 300:
    costo = 50000
elif distancia <= 1000:
    costo = 70000 + (distancia - 300) * 30000
else:
    costo = 150000 + (distancia - 1000) * 9000

# Salida del resultado
print(f"\nEl costo total a pagar es: ${costo:,.2f} COP")