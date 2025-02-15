Algoritmo Ejercicio_10_Cambio_de_divisas
    
    tasa_chelines_pesetas <- 956.871 / 100
    tasa_dracmas_pesetas <- 88.607 / 100
    tasa_francos_pesetas <- 20.110
    tasa_dolares_pesetas <- 1 / 122.499
    tasa_liras_pesetas <- 100 / 9.289
    
    
    Escribir "Ingrese la cantidad en chelines austriacos: "
    Leer chelines
    en_pesetas <- chelines * tasa_chelines_pesetas
    Escribir "Equivalente en pesetas: ", en_pesetas
	
	
    Escribir "Ingrese la cantidad en dracmas griegos: "
    Leer dracmas
    en_francos <- (dracmas * tasa_dracmas_pesetas) / tasa_francos_pesetas
    Escribir "Equivalente en francos franceses: ", en_francos
    
	
    Escribir "Ingrese la cantidad en pesetas: "
    Leer pesetas
    en_dolares <- pesetas * tasa_dolares_pesetas
    en_liras <- pesetas * tasa_liras_pesetas
    Escribir "Equivalente en dólares estadounidenses: ", en_dolares
    Escribir "Equivalente en liras italianas: ", en_liras
FinAlgoritmo