Algoritmo ejercicio_8_Calculo_de_area_de_triangulo
    
    Escribir "Ingrese el lado a: "
    Leer a
    Escribir "Ingrese el lado b: "
    Leer b
    Escribir "Ingrese el lado c: "
    Leer c
    
    Si (a + b > c) Y (a + c > b) Y (b + c > a) Entonces
		
		s <- (a + b + c) / 2
		
		area <- Raiz(s * (s - a) * (s - b) * (s - c))
		
		Escribir "El área del triángulo es: ", area
    Sino
		Escribir "Los valores ingresados no forman un triángulo válido."
    FinSi
FinAlgoritmo