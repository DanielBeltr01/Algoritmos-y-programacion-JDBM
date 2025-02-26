#Entrada de Datos
Ventas_Dept1=float(input("ingresar ventas departamento 1: "))
Ventas_Dept2=float(input("ingresar ventas departamento 2: "))
Ventas_Dept3=float(input("ingresar ventas departamento 3: "))
Salario_base_Departamentos=float(input("ingrese Salario mensual de Vendedores:"))

#Calculo total de ventas
ventas_totales= Ventas_Dept1 + Ventas_Dept2 + Ventas_Dept3

#Determinacion del 33% de las ventas totales:
Incentivo_limite = ventas_totales * 0.33

#Incentivo departamentos:
incentivo_dept1 = incentivo_dept2 = incentivo_dept3 = 0

#Departamentos que recibiran incentivo:
if Ventas_Dept1 > Incentivo_limite:
    incentivo_dept1 = Salario_base_Departamentos *0.20

if Ventas_Dept2 > Incentivo_limite:
    incentivo_dept2 = Salario_base_Departamentos *0.20

if Ventas_Dept3 > Incentivo_limite:
    incentivo_dept3 = Salario_base_Departamentos *0.20

#Determinacion de Salario mensual con Incentivos:
Salario_total_Dept1 = Salario_base_Departamentos + incentivo_dept1
Salario_total_Dept2 = Salario_base_Departamentos + incentivo_dept2
Salario_total_Dept3 = Salario_base_Departamentos + incentivo_dept3
#Salida
print("\nResumen de pagos")
print(f"Departamento 1: Salario total = ${Salario_total_Dept1:,.2f} COP")
print(f"Departamento 2: Salario total = ${Salario_total_Dept2:,.2f} COP")
print(f"Departamento 3: Salario total = ${Salario_total_Dept3:,.2f} COP")