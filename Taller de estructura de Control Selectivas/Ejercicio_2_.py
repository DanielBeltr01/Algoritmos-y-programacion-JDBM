#datos de entrada
Salario=int(input("ingrese Salario: $ "))
if(Salario<900000):
    print("El aumento es: $",(Salario*0.15))
elif(Salario>900000):
    print("El aumento es: $",(Salario*0.12))