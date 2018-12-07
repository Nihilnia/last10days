# Lambda Ifadeleri!

# "normal yolla" fonskiyon tanımlamak

def topla(x, y):
    return x + y

islemSonucu = topla(2, 3)
print(islemSonucu)

# lambda ile tanımlayalım

topla2 = lambda x, y: x + y #direkt return eder

islemSonucu2 = topla2(3, 4)
print(islemSonucu2)

# diger bir ornek

def SayHello(name = "nihil"):
    return "Hello " + name

print(SayHello("Pavel"))

# lambda versiyonu

SayHi = lambda name = "nihil": "hello " + name

print(SayHi("Grolla"))

# print ile bir ornek yapalım

sayDie = lambda nick = "nihl" : print("Die", nick)
sayDie("lMAO")


# ve baska bir ornek:

TersYaz = lambda girdi = "tersYaz": girdi[::-1]
print(TersYaz("nihil"))