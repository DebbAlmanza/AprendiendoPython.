Entrada=input()
print(type(Entrada))
esEntero=(Entrada.isdigit() and Entrada.find(".")==-1)
if (esEntero):
    print("Dato Entero. ¡Muy bien!")
else:
    print("Dato no es entero. Intentar nuevamente.")