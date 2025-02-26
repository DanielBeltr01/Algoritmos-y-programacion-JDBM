# Entrada de datos
P = int(input("Ingrese el valor de P: "))
Q = int(input("Ingrese el valor de Q: "))

# Evaluación de la expresión
resultado = (P**3 + Q**4 - 2 * P**2)

# Verificación de la condición
if resultado > 680:
    print("P=" + str(P) + " y Q=" + str(Q) + " satisfacen la expresión.")
else:
    print("P=" + str(P) + " y Q=" + str(Q) + " no satisfacen la expresión.")