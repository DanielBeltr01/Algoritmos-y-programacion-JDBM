# Entrada de datos
monto_total = float(input("Ingrese el monto total de la compra en COP: "))

# Cálculo según las condiciones
if monto_total > 5000000:
    inversion_empresa = monto_total * 0.55
    prestamo_banco = monto_total * 0.30
    credito_fabricante = monto_total - (inversion_empresa + prestamo_banco)
else:
    inversion_empresa = monto_total * 0.70
    prestamo_banco = 0  # No se pide préstamo al banco
    credito_fabricante = monto_total - inversion_empresa

# Cálculo de intereses del fabricante (20% sobre el crédito)
intereses_fabricante = credito_fabricante * 0.20

# Salida
print("\nResumen del pago:")
print(f"Inversión de la empresa: ${inversion_empresa:,.2f} COP")
print(f"Préstamo del banco: ${prestamo_banco:,.2f} COP")
print(f"Crédito con el fabricante: ${credito_fabricante:,.2f} COP")
print(f"Intereses a pagar al fabricante: ${intereses_fabricante:,.2f} COP")