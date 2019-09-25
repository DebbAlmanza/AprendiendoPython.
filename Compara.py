Numero1=input("Numero1:")
Numero2=input("Numero2:")
Salida="Numeros proporcionados: {} y {}. {}"
if (Numero1==Numero2):
    print(Salida.format(Numero1, Numero2, "Los numeros son iguales."))
else:
    if (Numero1>Numero2):
        print(Salida.format(Numero1, Numero2, "El primer numero es mayor."))
    else:
       print(Salida.format(Numero1, Numero2, "El segundo numero es mayor."))