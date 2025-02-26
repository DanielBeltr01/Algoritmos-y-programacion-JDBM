# Función para determinar si hay anemia según la edad y el sexo
def determinar_anemia(edad, sexo, hemoglobina):
    if edad <= 1/12:  # 0 a 1 mes (1/12 representa 1 mes en años)
        rango_min, rango_max = 13, 26
    elif edad <= 6/12:  # Mayor de 1 mes y hasta 6 meses
        rango_min, rango_max = 10, 18
    elif edad <= 1:  # Mayor de 6 meses y hasta 1 año
        rango_min, rango_max = 11, 15
    elif edad <= 5:  # Mayor de 1 año y hasta 5 años
        rango_min, rango_max = 11.5, 15
    elif edad <= 10:  # Mayor de 5 años y hasta 10 años
        rango_min, rango_max = 12.6, 15.5
    elif edad <= 15:  # Mayor de 10 años y hasta 15 años
        rango_min, rango_max = 13, 15.5
    elif sexo.lower() == "mujer":  # Mujeres mayores de 15 años
        rango_min, rango_max = 12, 16
    elif sexo.lower() == "hombre":  # Hombres mayores de 15 años
        rango_min, rango_max = 14, 18
    else:
        return "Sexo inválido. Debe ser 'hombre' o 'mujer'."

    # Determinar si tiene anemia
    if hemoglobina < rango_min:
        return f"Resultado: POSITIVO para anemia. Nivel de hemoglobina ({hemoglobina} g%) es menor que el rango {rango_min} - {rango_max} g%."
    else:
        return f"Resultado: NEGATIVO para anemia. Nivel de hemoglobina ({hemoglobina} g%) está dentro del rango {rango_min} - {rango_max} g%."

# Entrada de datos
edad = float(input("Ingrese la edad en años (Ejemplo: 0.5 para 6 meses, 3 para 3 años): "))
sexo = input("Ingrese el sexo (hombre/mujer): ")
hemoglobina = float(input("Ingrese el nivel de hemoglobina en g%: "))

# Salida del resultado
resultado = determinar_anemia(edad, sexo, hemoglobina)
print("\n" + resultado)