# Entrada de los 4 dígitos
A = int(input("Ingrese el dígito (A): "))
B = int(input("Ingrese el dígito (B): "))
C = int(input("Ingrese el dígito (C): "))
D = int(input("Ingrese el dígito (D): "))

# Calculo del Número entero N
N = A * 1000 + B * 100 + C * 10 + D

# Redondeo a la centena más cercana
N_redondeado = round(N, -2)

# Salida del resultado
print(f"\nNúmero original: {N}")
print(f"Número redondeado a la centena más cercana: {N_redondeado}")