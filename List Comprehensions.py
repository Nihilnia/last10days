# # LIST COMPREHENSIONS BITCH !

# #hemen hızlı bir örnek, liste aktarımı!

ListemBir = [0, 2, 4, 6, 8]
ListemIki = [sayilar for sayilar in ListemBir]
print(ListemIki)

#diger bir örnek

DemetliListe = [(1, 2), (3, 4), (5, 6)]
TekSayilar = [y for x in DemetliListe for y in x if y % 2 == 0]
CiftSayilar = [z for w in DemetliListe for z in w if z % 2 != 0]
print(TekSayilar)
print(CiftSayilar)




TupleList = [(1, 2), (3, 4), (5, 6), (7, 8)]

OddNumbers = [x for y in TupleList for x in y if x % 2 == 0]
EvenNumbers = [z for w in TupleList for z in w if z % 2 != 0]

print("Odd Numbers in the TupleList:", OddNumbers)
print("Even Numbers in the TupleList:", EvenNumbers)

# diğer bir örnek
#diyelim ki şöyle bir listemiz vaR:
TheListeLMAO = [[2, 3], [4, 5], [6, 7]]
# ve bu liste içindeki listelerin her elemanını dışarı cıkarıp
# tek bir listeye atmak istiyoruz

DamnSon = [x for y in TheListeLMAO for x in y]
print(DamnSon)

# başka bir örnek daha yapalım şimdi
#yine bir liste içinde başka listelerimiz olsun
# bu elemanları tek tek başka bir listeye atalım ve
# string olanları ekranlara basalım

GGList = [["sfda", 2], [123, True, "121"], ["nihil", 123], [8882, "hash"]]
NewList = [x for y in GGList for x in y]
# string olan elemanları yeni bir listeye atıp ekrana basalım
StringList = [z for z in NewList if isinstance(z, str)]
print("String tipindeki değerler:", StringList)