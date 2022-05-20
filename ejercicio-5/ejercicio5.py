


#Intput

Numero = int (input("ingresa un numero"))
contador=0

#Processing
while Numero>0:
    Numero=Numero//10
    contador=contador+1

#Output
print("el numero ingresado tiene %s digitos" % (contador))