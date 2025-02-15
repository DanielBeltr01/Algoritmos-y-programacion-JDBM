Algoritmo ejercicio_16_Calculo_de_costo_gasolina
	
    precio_por_litro <- 50000
    
    Escribir "Ingrese la cantidad de galones llenos: "
    Leer galones_llenos
    
    litros_surtidos <- galones_llenos * 3.785
    
    total_a_pagar <- litros_surtidos * precio_por_litro
    
    Escribir "Cantidad surtida: ", galones_llenos, " galones"
    Escribir "Equivalente en litros: ", litros_surtidos, " litros"
    Escribir "Total a pagar: ", total_a_pagar, " COP"
    
FinProceso