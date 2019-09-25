import random
Numero1= float(10.5)
def miFuncion():
    Numero2=float(random.randrange(1,10))
    Mensaje="La suma de {} y {} es {}"
    print(Mensaje.format(Numero1, Numero2, Numero1+Numero2)
miFuncion()
