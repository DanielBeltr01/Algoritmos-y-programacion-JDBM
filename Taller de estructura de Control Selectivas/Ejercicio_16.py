import math

# Entrada de datos
A = float(input("Ingrese el coeficiente A: "))
B = float(input("Ingrese el coeficiente B: "))
C = float(input("Ingrese el coeficiente C: "))

# Cálculo del discriminante
D = B**2 - 4*A*C

# Evaluación del discriminante y cálculo de las soluciones
if D > 0:
    X1 = (-B + math.sqrt(D)) / (2 * A)
    X2 = (-B - math.sqrt(D)) / (2 * A)
    print(f"\nLa ecuación tiene dos soluciones reales:")
    print(f"X1 = {X1:.2f}")
    print(f"X2 = {X2:.2f}")
elif D == 0:
    X = -B / (2 * A)
    print(f"\nLa ecuación tiene una única solución real:")
    print(f"X = {X:.2f}")
else:
    print("\nLa ecuación no tiene solución en los números reales (D < 0).")