Algoritmo ejercicio_18_calculo_por_ciento_anual
    
    Escribir "Ingrese el monto del préstamo (capital en Bolívares X): "
    Leer capital
    Escribir "Ingrese el total de intereses pagados (Bolívares Y): "
    Leer intereses
    Escribir "Ingrese el tiempo del préstamo en años: "
    Leer tiempo
    
    tasa_interes <- (intereses * 100) / (capital * tiempo)
    
    Escribir "Tasa de interés anual: ", tasa_interes, " %"
    
FinProceso