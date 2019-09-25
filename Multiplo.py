Numero=int(input("Dame un numero entero: "))
esMultiplo3=((Numero%3)==0)
esMultiplo5=((Numero%5)==0)
esMultiplo7=((Numero%7)==0)
if((esMultiplo3 and esMultiplo5 ) or esMultiplo7):
    print("Correcto.")
else:
    print("Incorrecto.")