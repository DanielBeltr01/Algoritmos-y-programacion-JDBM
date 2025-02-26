# Entrada de datos
nombre_cliente = input("Ingrese el nombre del cliente: ")
monto_compra = float(input("Ingrese el monto de la compra en COP: "))

# Determinación del descuento según el monto de compra
if monto_compra < 50000:
    descuento = 0
elif monto_compra <= 100000:
    descuento = 0.05
elif monto_compra <= 700000:
    descuento = 0.11
elif monto_compra <= 1500000:
    descuento = 0.18
else:
    descuento = 0.25

# Cálculo del valor del descuento y total a pagar
valor_descuento = monto_compra * descuento
monto_final = monto_compra - valor_descuento

# Salida de resultados
print("\n--- Resumen de la compra ---")
print(f"Cliente: {nombre_cliente}")
print(f"Monto de la compra: ${monto_compra:,.2f} COP")
print(f"Descuento aplicado: {descuento*100:.0f}%")
print(f"Valor del descuento: ${valor_descuento:,.2f} COP")
print(f"Total a pagar: ${monto_final:,.2f} COP")