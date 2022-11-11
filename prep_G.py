#Riempi una lista di 5 numeri e stampa il minore.

num_lista =[0,6,2,8,4]
a=999
for x in num_lista:
    if a>x:
        a=x
print(a)