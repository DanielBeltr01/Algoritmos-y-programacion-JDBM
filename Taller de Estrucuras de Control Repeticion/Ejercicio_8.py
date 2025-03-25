# Inicialización de contadores y acumuladores
total_consumidores = 0
total_encuestados = 0
mujeres_menores = 0
hombres_sin_aguardiente_20_25 = 0
suma_edades_cerveza = 0
conteo_cerveza = 0
conteo_whisky = 0

while True:
    # Solicitar datos al usuario
    consume = input("¿Consume licor? (Sí/No): ").strip().lower()
    if consume == "sí":
        total_consumidores += 1
    
    if consume == "sí":
        licor = int(input("Licor preferido (1-Aguardiente, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro): "))
    else:
        licor = 0  # No consume licor

    edad = int(input("Ingrese la edad: "))
    sexo = input("Ingrese el sexo (M/F): ").strip().upper()

    # Contar total de encuestados
    total_encuestados += 1

    # Contar mujeres menores de edad
    if sexo == "F" and edad < 18:
        mujeres_menores += 1

    # Contar hombres que no consumen aguardiente y tienen entre 20 y 25 años
    if sexo == "M" and 20 <= edad <= 25 and (consume == "no" or licor != 1):
        hombres_sin_aguardiente_20_25 += 1

    # Sumar edades de quienes consumen cerveza
    if consume == "sí" and licor == 3:
        suma_edades_cerveza += edad
        conteo_cerveza += 1

    # Contar personas que consumen whisky
    if consume == "sí" and licor == 5:
        conteo_whisky += 1

    # Preguntar si desea continuar con la encuesta
    continuar = input("¿Desea continuar con la encuesta? (Sí/No): ").strip().lower()
    if continuar != "sí":
        break

# Calcular estadísticas
promedio_cerveza = suma_edades_cerveza / conteo_cerveza if conteo_cerveza > 0 else 0
porcentaje_whisky = (conteo_whisky / total_encuestados) * 100 if total_encuestados > 0 else 0

# Mostrar resultados
print("'\nResultados de la encuesta:")
print("Total de personas que consumen licor:", total_consumidores)
print("Total de mujeres menores de edad:", mujeres_menores)
print("Total de hombres que no consumen aguardiente y tienen entre 20 y 25 años:", hombres_sin_aguardiente_20_25)
print(f"Promedio de edad de quienes consumen cerveza: {promedio_cerveza:.2f}")
print(f"Porcentaje de personas que consumen whisky respecto al total encuestado: {porcentaje_whisky:.2f}%")