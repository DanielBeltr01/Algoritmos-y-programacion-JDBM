Algoritmo Ejercicio_9
    Definir numero, numeroInvertido, residuo, copiaNumero Como Entero
    Definir cadenaNumero, cadenaInvertida Como Cadena
    
    Escribir "Ingrese un n�mero: "
    Leer numero
    
    copiaNumero <- numero
    numeroInvertido <- 0
    
    Mientras copiaNumero > 0 Hacer
        residuo <- copiaNumero MOD 10
        numeroInvertido <- (numeroInvertido * 10) + residuo
        copiaNumero <- Trunc(copiaNumero / 10)
    Fin Mientras
    
    Si numero = numeroInvertido Entonces
        Escribir "Es un pal�ndromo"
    Sino
        Escribir "No es un pal�ndromo"
    FinSi
FinProceso