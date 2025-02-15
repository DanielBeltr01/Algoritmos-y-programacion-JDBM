Algoritmo ejercicio_20_Porcentaje_recargo_por_cuotas
	
    Escribir "Ingrese el precio del computador al contado (P en COP): "
    Leer P
    Escribir "Ingrese el valor de cada cuota mensual (T en COP): "
    Leer T
    
    precio_cuotas <- 12 * T
    
    recargo <- precio_cuotas - P
    
    porcentaje_recargo <- (recargo / P) * 100
    
    Escribir "Precio al contado: ", P, " COP"
    Escribir "Precio total a cuotas: ", precio_cuotas, " COP"
    Escribir "Recargo total: ", recargo, " COP"
    Escribir "Porcentaje de recargo: ", porcentaje_recargo, " %"
	
FinAlgoritmo