#Riempi una lista di 10 numeri casuali (utilizza un ciclo for) e stampa solo i numeri pari

casuali = [x for x in range (10)]
for x in casuali:
    if x%2==0:
        print(x) 