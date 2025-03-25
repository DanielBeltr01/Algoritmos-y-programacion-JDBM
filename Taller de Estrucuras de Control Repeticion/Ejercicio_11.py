#Entradas
saldo = 1000  

while True:
    print("\nMENÚ CAJERO AUTOMÁTICO")
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1": 
        monto = float(input("Ingrese el monto a depositar: "))
        if monto > 0:
            saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
        else:
            print("Monto no válido.")

    elif opcion == "2": 
        monto = float(input("Ingrese el monto a retirar: "))
        if 0 < monto <= saldo:
            saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: ${saldo:.2f}")
        else:
            print("Fondos insuficientes o monto no válido.")

    elif opcion == "3":  
        print(f"Su saldo actual es: ${saldo:.2f}")

    elif opcion == "4":
        print("Gracias por usar el cajero automático. Hasta luego.")
        break

    else:
        print("Opción no válida. Intente de nuevo.")
