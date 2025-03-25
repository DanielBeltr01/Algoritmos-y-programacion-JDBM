
dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))

cociente = 0

if divisor == 0:
    print("Error: No se puede dividir por cero.")
else:
    
    while dividendo >= divisor:
        dividendo = dividendo - divisor
        cociente = cociente + 1  

    
    print("Cociente:", cociente)
    print("Residuo:", dividendo)
