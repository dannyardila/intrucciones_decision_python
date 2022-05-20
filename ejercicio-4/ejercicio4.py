"""Obtener la cantidad de los primeros N números
múltiplos de 5."""

print("--------------")
print("--------MULTIPLOS DE 5-----------")
print("-------------")

#Input

a=int(input("digite el valor de a :"))
b=int(input("digite el valor de b :"))


#Proccesing

if a<b:
    cant_num=0
    a=a+1
    while(a<=b):
        r= a%5
        if r==0:
            cant_num=cant_num+1
        a=a+1
else:
    print ("a debe ser menor que b")

# Output

print("los numeros son", cant_num)

