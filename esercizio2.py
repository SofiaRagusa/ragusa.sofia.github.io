# dichiara lista e stampa, usa parentesi quadre
thislist = ["apple", "banana", "cherry"]
print(thislist)

# gli oggetti sono indicizzati (partendo da 0) e quindi possono essere ripetuti
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#funzione per vedere la lunghezza della lista
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# le liste possono contenere tutti i tipi di data anche diversi in una stessa lista
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list1 = ["abc", 34, True, 40,]

# per sapere di che tipo è la lista usare:
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# per creare una lista
thislist = list(("apple", "banana", "cherry")) # da notare la doppia parentesi tonda
print(thislist)

# puoi stampare un oggetto di una lista riferendoti ad esso con il suo index
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# iniziando anche dalla fine con termini negativi
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# specifica da dove partire per stampare e dove finire (primo estremo compreso, ultimo escluso)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #considera che stamperà idal terzo oggetto al quinto (perché si parte  da 0)

# per escludere degli oggetti :
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #dal quinto in poi non stamperà gli oggetti 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) # dal terzo in poi inizierà a stampare 

# per partire dalla fine utilizza:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) 

# controlla se un oggetto è presente
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# per cambiare valore ad un oggetto riferisciti al suo indice
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# per cambiare il valore a diversi oggetti usa:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#  puoi sostituire al tuo oggetto più valori
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
thislist = ["apple", "banana", "cherry"] # oppure a più oggetti dai un unico valore
thislist[1:3] = ["watermelon"]
print(thislist)

#per aggiungere un oggetto senza sostituirne un altro usare:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#oppure
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#per estendere la lista  e incorporarla ad un'altra lista:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) #che verranno aggiunti alla fine della prima

# può anche essere usato per altri tipi di variabili
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# per rimuovere usare il comando 
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#per rimuovere un oggetto con indice usare 
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) #se non si indicizza pop elimirà l'ultimo oggetto

#rimuovere l'intera lista
thislist = ["apple", "banana", "cherry"]
del thislist

# per ripulire la lista, svuotandola
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# per stapare gli oggetti uno per uno 
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# 
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]





