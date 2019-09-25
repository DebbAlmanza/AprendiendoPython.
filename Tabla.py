Numero=input("Dame un número del 1 al 9: ")
Numero=int(Numero)
for i in range(1,11):
    salida="{} x {} ={}"
    print(salida.format(Numero,i,i*Numero))