#Dichiara due liste. Una con nomi di animali e l’altra con numeri. Aggiungi tutti gli elementi della seconda lista alla prima.
#Stampa soltanto i numeri maggiori di 5

animali_lista=["Grifone", "Canguro Australiano", "Lince", "Bradipo", "Pulcino"]
num_lista =[0,6,2,8,4]
fusion_lista = num_lista+animali_lista
for x in num_lista:
    if x>5:
        print(x) 