Algoritmo ejercicio_14_Calculo_pago_total_LUZ
    
    Escribir "Ingrese la lectura anterior del medidor (kWh): "
    Leer lectura_anterior
    Escribir "Ingrese la lectura actual del medidor (kWh): "
    Leer lectura_actual
    Escribir "Ingrese el costo por kilovatio (COP): "
    Leer costo_kilovatio
	
    consumo <- lectura_actual - lectura_anterior
    
    monto_a_pagar <- consumo * costo_kilovatio
    
    Escribir "Consumo del mes: ", consumo, " kWh"
    Escribir "Monto total a pagar: ", monto_a_pagar, " COP"
    
FinAlgoritmo