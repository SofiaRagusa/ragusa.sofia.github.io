#Crea due vettori uno con il nome di città e uno con il nome di persone.
#Stampa usando dei cicli for per ogni città tutti i nomi degli abitanti
#es: [‘torino’, ‘milano’ ] | [‘gino’, ‘lino’]
#stampa: torino - gino | torino - lino | milano - gino | milano - lino

città=["Bari", "Ancona","Genova"]
persone=["Gertrude","Herbert","Alice"]

for x in città:
    for y in persone:
        print(x , y)