Algoritmo Ejercicio_12_Promedio_general_de_materias
	
	Escribir "Ingrese la calificación del examen de Matemática: "
	Leer examen_matematica
	Escribir "Ingrese las tres calificaciones de tareas de Matemática: "
	Leer tarea1_matematica, tarea2_matematica, tarea3_matematica
	
	Escribir "Ingrese la calificación del examen de Física: "
	Leer examen_fisica
	Escribir "Ingrese las dos calificaciones de tareas de Física: "
	Leer tarea1_fisica, tarea2_fisica
	
	Escribir "Ingrese la calificación del examen de Química: "
	Leer examen_quimica
	Escribir "Ingrese las tres calificaciones de tareas de Química: "
	Leer tarea1_quimica, tarea2_quimica, tarea3_quimica
	
	promedio_matematica <- (examen_matematica * 0.90) + ((tarea1_matematica + tarea2_matematica + tarea3_matematica) / 3 * 0.10)
	promedio_fisica <- (examen_fisica * 0.80) + ((tarea1_fisica + tarea2_fisica) / 2 * 0.20)
	promedio_quimica <- (examen_quimica * 0.85) + ((tarea1_quimica + tarea2_quimica + tarea3_quimica) / 3 * 0.15)
	
	
	promedio_general <- (promedio_matematica + promedio_fisica + promedio_quimica) / 3
	
	
	Escribir "Promedio en Matemática: ", promedio_matematica
	Escribir "Promedio en Física: ", promedio_fisica
	Escribir "Promedio en Química: ", promedio_quimica
	Escribir "Promedio General: ", promedio_general
	
	
FinAlgoritmo