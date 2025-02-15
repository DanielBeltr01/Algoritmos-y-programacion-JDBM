Algoritmo calcular_comisiones_por_ventas
    Definir sueldo_base, venta1, venta2, venta3, comision, total_pagar Como Real
	// entrada 
    Escribir "Ingrese el sueldo base: "
    Leer sueldo_base
    Escribir "Ingrese el valor de la primera venta: "
    Leer venta1
    Escribir "Ingrese el valor de la segunda venta: "
    Leer venta2
    Escribir "Ingrese el valor de la tercera venta: "
    Leer venta3
	// Caja negra
	comision = (venta1 + venta2 + venta3) * 0.10
	total_pagar = sueldo_base + comision
	// salida
    Escribir "La comisión total es: ", comision
    Escribir "El total a pagar (sueldo base + comisión) es: ", total_pagar
FinAlgoritmo