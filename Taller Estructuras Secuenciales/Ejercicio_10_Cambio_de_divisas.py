# Definir las tasas de conversión
tasa_chelines_pesetas = 956.871 / 100
tasa_dracmas_pesetas = 88.607 / 100
tasa_francos_pesetas = 20.110
tasa_dolares_pesetas = 1 / 122.499
tasa_liras_pesetas = 100 / 9.289

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

# Conversión de chelines austriacos a pesetas
chelines = obtener_numero("Ingrese la cantidad en chelines austriacos: ")
en_pesetas = chelines * tasa_chelines_pesetas
print(f"Equivalente en pesetas: {en_pesetas:.2f}")

# Conversión de dracmas griegos a francos franceses
dracmas = obtener_numero("Ingrese la cantidad en dracmas griegos: ")
en_francos = (dracmas * tasa_dracmas_pesetas) / tasa_francos_pesetas
print(f"Equivalente en francos franceses: {en_francos:.2f}")

# Conversión de pesetas a dólares y liras italianas
pesetas = obtener_numero("Ingrese la cantidad en pesetas: ")
en_dolares = pesetas * tasa_dolares_pesetas
en_liras = pesetas * tasa_liras_pesetas
print(f"Equivalente en dólares estadounidenses: {en_dolares:.2f}")
print(f"Equivalente en liras italianas: {en_liras:.2f}")