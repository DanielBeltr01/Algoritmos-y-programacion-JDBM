Algoritmo ejercicio_19_Porcentaje_de_ganancia_Inversion
    Escribir "Ingrese la cantidad total de naranjas compradas (X): "
    Leer X
    Escribir "Ingrese el precio por docena de naranjas (u en Bs): "
    Leer u
    Escribir "Ingrese el dinero obtenido por la venta de todas las naranjas (K en Bs): "
    Leer K
    
    costo_total <- (X / 12) * u
    
    ganancia <- K - costo_total
    
    porcentaje_ganancia <- (ganancia / costo_total) * 100
	
    Escribir "Costo total de compra: ", costo_total, " Bs"
    Escribir "Ganancia obtenida: ", ganancia, " Bs"
    Escribir "Porcentaje de ganancia: ", porcentaje_ganancia, " %"
	
FinAlgoritmo