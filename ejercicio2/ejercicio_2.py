"""Dado un rango de números enteros, obtener la
cantidad de números que contiene."""

print("----------------------")
print("-----------obtener la cantidad de numeros que contiene un rango------")
print("-----------------")

#Input

a= int (input("digite el valor de a: "))

b= int (input("digite el valor de b :"))

#Proccesing

if (a<b):
    cant_num=0
    a=a+1
    while a<b:
        a=a+1
        cant_num=cant_num+1

# Output
else:
    print ("a debe ser menor que b")

print ("los valores son",cant_num )
