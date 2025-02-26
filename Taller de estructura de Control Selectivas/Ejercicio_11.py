#Entradas
t=int(input("ingrese Temperatura: "))
d=""#deporte
#Caja negra
if(t>85):
    d="Natación"
elif(t>70 and t<=85):
    d="Tenis"
elif(t>32 and t<=70):
    d="Golf"
elif(t>10 and t<=32):
    d="Esqui"
elif(t<0 and t<=10):
    d="Marcha"
else:
    d="La temperatura no corresponde a ningun deporte"
#Salida
print(f"El deporte a practicar es: {d}")