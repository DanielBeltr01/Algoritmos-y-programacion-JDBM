#Entrada

suma = 0
k = 1
contador = 0

while suma + ((k**2 + 1) / k) <= 1000:
    N = (k**2 + 1) / k  
    suma = suma + N 
    contador = contador + 1  
    k = k + 1 

print("Número de términos necesarios:", contador)