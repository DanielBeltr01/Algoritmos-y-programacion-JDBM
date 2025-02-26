# Entrada de datos
cantidad = int(input("Ingrese la cantidad en COP: "))

# Lista de billetes y monedas en orden descendente
denominaciones = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50]

# Resultado del desglose
resultado = []

# Proceso de descomposición
for valor in denominaciones:
    if cantidad >= valor:
        cantidad_billetes = cantidad // valor  # Cantidad de billetes o monedas
        cantidad %= valor  # Resto de la cantidad
        resultado.extend([valor] * cantidad_billetes)

# Mostrar salida
print("\nDesglose en billetes y monedas:")
print(", ".join(map(str, resultado)))