Algoritmo ejercicio_11_Calculo_de_asignaciones_deducciones_y_sueldo_neto
		
	actualizacion_academica <- 250000
	prima_hogar <- 180000
	
	Escribir "Ingrese el nombre del trabajador: "
	Leer nombre
	Escribir "Ingrese el número de horas normales trabajadas: "
	Leer horas_normales
	Escribir "Ingrese el pago por hora normal: "
	Leer pago_hora
	Escribir "Ingrese el número de horas extras trabajadas: "
	Leer horas_extras
	Escribir "Ingrese el número de hijos: "
	Leer hijos
	
	sueldo_base <- horas_normales * pago_hora
	
	pago_extras <- horas_extras * (pago_hora * 1.25)
	
	asignacion_hijos <- hijos * 173000
	total_ingresos <- sueldo_base + pago_extras + actualizacion_academica + asignacion_hijos + prima_hogar
	
	
	deduccion_pago_forzoso <- sueldo_base * 0.05
	deduccion_politica <- sueldo_base * 0.02
	deduccion_ahorro <- sueldo_base * 0.07
	total_deducciones <- deduccion_pago_forzoso + deduccion_politica + deduccion_ahorro
	
	
	sueldo_neto <- total_ingresos - total_deducciones
	
	
	
	Escribir "Trabajador: ", nombre
	Escribir "Sueldo base: ", sueldo_base
	Escribir "Pago por horas extras: ", pago_extras
	Escribir "Asignaciones:"
	Escribir "  - Actualización académica: ", actualizacion_academica
	Escribir "  - Asignación por hijos: ", asignacion_hijos
	Escribir "  - Prima por hogar: ", prima_hogar
	Escribir "Total asignaciones: ", total_ingresos - sueldo_base
	
	Escribir "Deducciones:"
	Escribir "  - Pago forzoso (5%): ", deduccion_pago_forzoso
	Escribir "  - Política habitacional (2%): ", deduccion_politica
	Escribir "  - Caja de ahorro (7%): ", deduccion_ahorro
	Escribir "Total deducciones: ", total_deducciones
	
	Escribir "Sueldo neto del trabajador: ", sueldo_neto
	
	
FinAlgoritmo