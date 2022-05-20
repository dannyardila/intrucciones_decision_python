"""Dado un rango de números enteros obtener la
cantidad de números pares que contiene."""

print("---------------------")
print("-------OBTENER LOS NUMEROS PARES-------")
print("-----------------------")

#Input

a= int (input("digite el valor de a: "))

b= int (input("digite el valor de b :"))

#Proccesing

if (a<b):
    cant_num=0
    a=a+1
    while a <= b:
       r= a % 2
       if (r==0):
        cant_num=cant_num+1
        a=a+1
    print(cant_num)

# Output
else:
    print ("a debe ser menor que b")

print ("los valores son",cant_num )   

