#esercizio 1

import random

z= random.randint(10,20)

print (z)

#esercizio 2

listone1= []

for i in range (z):
    listone1.append(random.randint(0,20))

print (listone1)

#esercizio 3

listone2=[]
for x in listone1:
    if x < z:
        listone2.append(x)
print(listone2)

#esercizio 4

for x in listone1:
    if x in listone2:
        pass
    else:
        print(x)

#esercizio 5 
listone2quadrato=[]
for x in listone2:
    listone2quadrato.append(x*x)

#esercizio  6

risultone=0
for x in listone2:
    if x>z:
        risultone=risultone+x

print(risultone)

#esercizio 7

if risultone+18 > len(listone2):
    print("evviva")
else:
    print("buuu")




