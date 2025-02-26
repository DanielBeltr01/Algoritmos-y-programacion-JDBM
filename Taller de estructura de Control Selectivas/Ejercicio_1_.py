#ejercicio_1

def calcular_interes(inversion, tasa_interes, tiempo):
    intereses = inversion * (tasa_interes / 100) * tiempo
    if intereses > 100000:
        inversion_final = inversion + intereses
        return intereses, inversion_final
    return intereses, inversion

# Solicitar datos al usuario
inversion = float(input("Ingrese la cantidad de dinero invertido: "))
tasa_interes = float(input("Ingrese la tasa de interés anual (%): "))
tiempo = float(input("Ingrese el tiempo en años: "))

# Calcular intereses e inversión final
intereses, inversion_final =(inversion, tasa_interes, tiempo)

# Mostrar resultados
print(f"Intereses generados: ${intereses:,.2f} COP")
if intereses > 100000:
    print(f"Se reinvertirán los intereses. Monto final en la cuenta: ${inversion_final:,.2f} COP")
else:
    print(f"No se reinvertirán los intereses. Monto final en la cuenta: ${inversion:,.2f} COP")
