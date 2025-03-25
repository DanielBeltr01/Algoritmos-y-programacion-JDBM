#Entradas
num = int(input("Ingrese un número entero positivo: "))


suma = 0
# Caja negra
for i in range(1, num):  
    if num % i == 0:  
        suma += i  


if suma == num:
    print(f"{num} es un número perfecto.")
else:
    print(f"{num} no es un número perfecto.")