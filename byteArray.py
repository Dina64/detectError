def pair(a):
    for i in a:
        c = bin(i).strip("0b")
        if (c.count("1") % 2 == 0):

            d = "0"+ c
            e = bytearray(d, "utf-8")
        else:
            d = "1" + c
            e = bytearray(d, "utf-8")
    print(e)

def impair(a):
    for i in a:
        c = bin(i).strip("0b")
        if (c.count("1") % 2 == 0):
            d = "1" + c
            e = bytearray(d, "utf-8")
        else:
            d = "0" + c
            e = bytearray(d, "utf-8")
    print(e)

def add():
    n = int(input("entrer un nombre binaire:"))
    m = int(input("entrer un second nombre binaire:"))
    z = n ^ m
    base2 = ''
    while z:
        if z % 2:
            z = z // 2
            base2 = ('1') + base2
        else:
            z = z / 2
            base2 = ('0') + base2
    print(base2)


arr = input("Entrer un message: ")
a = bytearray(arr, "utf-8")
print("L'entrer: ", a)
mod = input("Appuyer sur P pour mode de parite pair et I pour impair : ")
if (mod == "P"):
    pair(a)
else:
    impair(a)
print("Somme de deux binaire:")
add()


