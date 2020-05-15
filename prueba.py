import time
import os
a=0
b="\nHola mundo"

os.system("cls")
def imp(a):
    print(a*b)
    return  
while True:
    a=int(input("Ingrese un numero: "))
    if a>=1:
        imp(a)
        break
    else:
        print('Ingrese un numero mayor que 0')
        imp(a)

print ("Gracias por participar... :)")