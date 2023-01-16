
import random

z= random.randint(10,20)

print (z)

listone1= []

for i in range (z):
    listone1.append(random.randint(0,20))

print (listone1)

listone2=[]
for x in listone1:
    if x < z:
        listone2.append(x)
print(listone2)

for x in listone1:
    if x in listone2:
        pass
    else:
        print(x)
