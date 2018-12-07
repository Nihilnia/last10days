# Fonksyionlar!

#Notlar:
# Return bir fonksiyon için son demektir, unutma.
# Fonskiyon olustururken parametre belirtmek zorunda değiliz.
#Fakat belirtirsek kullanırken parametre girmek durumdayız.
# Bunun için default = Parametreler vardır. 
#ESNET PARAMETRELER COK ONEMLI!


def SayHello (a = "World!"):
    print("Hello " + a)

userInput = input("Adınız: ")
SayHello(userInput)


#return kullanalım

def SayHi (a = "World!"):
    return "Hello " + a

userName = input("Isminiz: ")
print(SayHi(userName))

#Faktoriyel için bir fonksiyon yaratalım!

def CalculateFac ():
    sayi = int(input("Faktoriyelini almak istediğiniz sayi: "))
    toplam = 1

    if sayi != 1 or sayi != 0:
        for sayilar in range(2, sayi + 1):
            toplam *= sayilar
        print(sayi, "'nin faktoriyeli =", toplam)
    else:
        print(sayi, "'nin faktoriyeli 1.")
        

while True:
    CalculateFac()

#return kullanarak yapalım

def CalculateFac2 ():
    sayi = int(input("Faktoriyelini almak istediğiniz sayi: "))
    toplam = 1

    if sayi != 1 or sayi != 0:
        for sayilar in range(2, sayi + 1):
            toplam *= sayilar
        return toplam
    else:
        return 1
        

while True:
    print(CalculateFac2())


#ESNEK PARAMETRELERE GUZEL BIR ORNEK YAPALIM!
# Kullanıcı istedigi kadar sayı girecek ve biz bunu
#esnek parametre kullanarak yapacağız.

def EsnekParametreOrnegi(*sayi):
    sayilarToplami = 0
    ilkSayi = int(input("Bir sayi veriniz: "))
    sayilarToplami = ilkSayi
    while True:
        sayi = input("Bir sayi veriniz: ")
        if sayi.lower() != "q":
            sayilarToplami += int(sayi)
            print("Anlık toplam:", sayilarToplami)
        else:
            print("Cya!")
            return sayilarToplami

print(EsnekParametreOrnegi())

