Acumulado=int(0)
Numero=str("")

while True:
    Numero=input("Dame un número entero:")
    if Numero=="":
        print("Vacio. Salida del programa.")
        break
    else:
        Acumulado+=int(Numero)
        Salida= "Monto acumulado {}"
        print(Salida.format(Acumulado))

