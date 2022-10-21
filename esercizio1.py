x = 5  #assegnazione a variabile x il valore 5
y = "John" #assegnazione a variasbile y il valore "Jhon"
print(x) #stampare vaiabile x
print(y) #stampare variabile y

x = 4       # x è di tipo int
x = "Sally" # x adesso è di tipo str
print(x) #stampare variabile

    # se si vuole specificare il tipo si può fare con casting
x = str(3)    # x sarà '3'
y = int(3)    # y sarà be 3
z = float(3)  # z sarà be 3.0

    # puoi usare le virgolette doppie o singole
x = "John"
# è lo stesso di
x = 'John'

    #ogni variabile è diversa dalla sua maiuscola
a = 4
A = "Sally"
#A non riscriverà su a

    # i nomi delle variabili devono rispettare determinate regole
2myvar = "John" #non può iniziare con un numero
my-var = "John" #non può contenere (-)
my var = "John" # non può contenere spazi

    # si possono assegnare valori a diverse variabili sulla stessa riga
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
    #assegnare un valore solo a più variabili
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
    # puoi spacchettare una collezione assegnando a ogni valore una variabile
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

    #per stampare una variabile
x = "Python is awesome"
print(x)

    # più variabili posso essere stampate insieme separate da una virgola
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)



    # + è un operatore somma che non può essere combinato con un tipo "str"
x = 5
y = "John"
print(x + y)



    # se stampi all'interno della funzione, riassegnando un valore alla variabile all'interno della funzione, stamperà il nuovo valore
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x) #all'esterno della funzione la variabile torna al valore iniziale


    # se si vuole definire una variabile all'interno di una func che valga anche all'esterno, bisogna aggiungere la keyword global
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
