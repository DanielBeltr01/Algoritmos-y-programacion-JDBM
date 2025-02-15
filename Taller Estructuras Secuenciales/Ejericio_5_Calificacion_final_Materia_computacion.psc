Algoritmo Ejericio_5_Calificacion_final_Materia_computacion
	// entrada
	Escribir "calificacion_1: "
	Leer calificacion1
	Escribir "calificacion_2: "
	Leer calificacion2
	Escribir "calificacion_3: "
	Leer calificacion3
	
	Escribir "examen final: "
	leer examenfinal
	Escribir "trabajo final: "
	leer trabajofinal
	// caja negra
	
	promedio_calificaciones = (calificacion1+calificacion2+calificacion3) /3 
	nota_final = (promedio_calificaciones * 0.55) +  (examenfinal  * 0.30) + (trabajofinal * 0.15) 
	// salida
	
	Escribir "la nota final del alumno es: ", nota_final 
	
FinAlgoritmo