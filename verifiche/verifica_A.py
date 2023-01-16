casuali=[x for x in range (3)]
x, y, z, = casuali
if x<y and x<z:
    print(x)
    if y<z:
        print (y,z)
    else:
        print (z,y)
elif y<z:
    print(y)
    if x<z:
        print(x,z)
    else:
        print(z,x)
else:
    print(z)
    if x<y:
        print(x,y)
    else:
        print(y<x)
