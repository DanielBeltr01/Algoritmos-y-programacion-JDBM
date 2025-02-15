Algoritmo Ejercicio_7_Conversion_de_metros_a_pies_y_pulgadas
	// entrada 
	
	Escribir "Ingrese la cantidad de metros:"
	Leer metros
	
	pulgadas_totales = metros * 39.27
	pies = (pulgadas_totales / 12)
	pulgadas_restantes = pulgadas_totales - (pies * 12)
    Escribir "La conversión es: ", pies, " pies y ", pulgadas_restantes, " pulgadas."
	
	
FinAlgoritmo 