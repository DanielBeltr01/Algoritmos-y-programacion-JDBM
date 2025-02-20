def obtener_numero(mensaje):
    """Función para obtener un número válido del usuario"""
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Por favor, ingrese un número positivo.")
            else:
                return valor
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Definir montos fijos
ACTUALIZACION_ACADEMICA = 250000
PRIMA_HOGAR = 180000

# Solicitar datos al usuario
nombre = input("Ingrese el nombre del trabajador: ")
horas_normales = obtener_numero("Ingrese el número de horas normales trabajadas: ")
pago_hora = obtener_numero("Ingrese el pago por hora normal: ")
horas_extras = obtener_numero("Ingrese el número de horas extras trabajadas: ")
hijos = obtener_numero("Ingrese el número de hijos: ")

# Cálculos de sueldo
sueldo_base = horas_normales * pago_hora
pago_extras = horas_extras * (pago_hora * 1.25)  # Horas extras con 25% adicional
asignacion_hijos = hijos * 173000

# Total ingresos
total_ingresos = sueldo_base + pago_extras + ACTUALIZACION_ACADEMICA + asignacion_hijos + PRIMA_HOGAR

# Cálculo de deducciones
deduccion_pago_forzoso = sueldo_base * 0.05
deduccion_politica = sueldo_base * 0.02
deduccion_ahorro = sueldo_base * 0.07
total_deducciones = deduccion_pago_forzoso + deduccion_politica + deduccion_ahorro

# Cálculo del sueldo neto
sueldo_neto = total_ingresos - total_deducciones

# Mostrar resultados
print("\n--- Resumen de Nómina ---")
print(f"Trabajador: {nombre}")
print(f"Sueldo base: {sueldo_base:.2f}")
print(f"Pago por horas extras: {pago_extras:.2f}")
print("\nAsignaciones:")
print(f"  - Actualización académica: {ACTUALIZACION_ACADEMICA:.2f}")
print(f"  - Asignación por hijos: {asignacion_hijos:.2f}")
print(f"  - Prima por hogar: {PRIMA_HOGAR:.2f}")
print(f"Total asignaciones: {total_ingresos - sueldo_base:.2f}")
print("\nDeducciones:")
print(f"  - Pago forzoso (5%): {deduccion_pago_forzoso:.2f}")
print(f"  - Política habitacional (2%): {deduccion_politica:.2f}")
print(f"  - Caja de ahorro (7%): {deduccion_ahorro:.2f}")
print(f"Total deducciones: {total_deducciones:.2f}")
print("\nSueldo neto del trabajador:", f"{sueldo_neto:.2f}")