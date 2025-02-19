import math  # Importamos la librería para calcular la raíz cuadrada

def obtener_lado(mensaje):
    while True:
        try:
            lado = float(input(mensaje))
            if lado <= 0:
                print("Por favor, ingrese un valor positivo mayor que cero.")
            else:
                return lado
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Solicitar los lados del triángulo al usuario
a = obtener_lado("Ingrese el lado a: ")
b = obtener_lado("Ingrese el lado b: ")
c = obtener_lado("Ingrese el lado c: ")

# Verificar si los lados forman un triángulo válido
if (a + b > c) and (a + c > b) and (b + c > a):
    # Calcular el semiperímetro
    s = (a + b + c) / 2
    
    # Calcular el área con la fórmula de Herón
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    # Mostrar el resultado
    print(f"El área del triángulo es: {area:.2f}")
else:
    print("Los valores ingresados no forman un triángulo válido.")
