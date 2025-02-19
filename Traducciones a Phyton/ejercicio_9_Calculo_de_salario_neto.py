def obtener_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Por favor, ingrese un número positivo.")
            else:
                return valor
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Solicitar datos al usuario
horas_trabajadas = obtener_numero("Ingrese el número de horas trabajadas: ")
precio_hora = obtener_numero("Ingrese el precio por hora: ")

# Calcular salario bruto y neto
salario_bruto = horas_trabajadas * precio_hora
salario_neto = salario_bruto * 0.80  # Se descuenta el 20%

# Mostrar el resultado
print(f"El salario bruto es: {salario_bruto:.2f}")
print(f"El salario neto del trabajador es: {salario_neto:.2f}")