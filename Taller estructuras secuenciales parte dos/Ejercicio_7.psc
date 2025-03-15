Algoritmo Ejercicio_7
    Definir numero, i Como Entero
    Definir esPrimo Como Logico
    
    Escribir "Ingrese un número entero:"
    Leer numero
    
    Si numero <= 1 Entonces
        Escribir "No es primo"
    Sino
        esPrimo <- Verdadero
        Para i <- 2 Hasta numero - 1 Hacer
            Si numero MOD i = 0 Entonces
                esPrimo <- Falso
                
            FinSi
        FinPara
        
        Si esPrimo Entonces
            Escribir "Es primo"
        Sino
            Escribir "No es primo"
        FinSi
    FinSi
FinAlgoritmo