Algoritmo ejercicio_9_Calculo_de_salario_neto
    
    Escribir "el número de horas trabajadas: "
    Leer horas_trabajadas
    
    Escribir "el precio por hora: "
    Leer precio_hora
    
    salario_bruto <- horas_trabajadas * precio_hora
    
    salario_neto <- salario_bruto * 0.80
    
    Escribir "El salario neto del trabajador es: ", salario_neto
FinAlgoritmo