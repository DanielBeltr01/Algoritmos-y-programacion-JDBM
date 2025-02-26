from datetime import datetime

# Función para determinar el signo zodiacal
def obtener_signo_zodiaco(dia, mes):
    signos = [
        ("Capricornio", (22, 12), (20, 1)),
        ("Acuario", (21, 1), (19, 2)),
        ("Piscis", (20, 2), (19, 3)),
        ("Aries", (21, 3), (20, 4)),
        ("Tauro", (21, 4), (21, 5)),
        ("Géminis", (22, 5), (21, 6)),
        ("Cáncer", (22, 6), (22, 7)),
        ("Leo", (23, 7), (23, 8)),
        ("Virgo", (24, 8), (22, 9)),
        ("Libra", (23, 9), (22, 10)),
        ("Escorpión", (23, 10), (21, 11)),
        ("Sagitario", (22, 11), (21, 12))
    ]

    for signo, inicio, fin in signos:
        if (mes == inicio[1] and dia >= inicio[0]) or (mes == fin[1] and dia <= fin[0]):
            return signo

# Función para calcular la edad
def calcular_edad(dia, mes, año):
    fecha_nacimiento = datetime(año, mes, dia)
    fecha_actual = datetime.today()
    edad = fecha_actual.year - fecha_nacimiento.year
    
    # Ajustar si aún no ha cumplido años este año
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1

    return edad

# Entrada de datos
fecha_nacimiento = input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")
dia, mes, año = map(int, fecha_nacimiento.split('/'))

# Obtener signo zodiacal y edad
signo = obtener_signo_zodiaco(dia, mes)
edad = calcular_edad(dia, mes, año)

# Salida de resultados
print(f"\nSu signo zodiacal es: {signo}")
print(f"Su edad es: {edad} años")