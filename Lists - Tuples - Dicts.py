#Listeler!
# Oluşturma:
ornekListe = ["deger1", 2, 3.14, False]
print(*ornekListe)

#Erişim:
print(ornekListe[2]) #3.14

#Metodları:
#append() - deger ekleme
ornekListe.append("nihil")
print(*ornekListe)

#pop() - Değer cıkarma
#parametre vermezsek listedeki son elemanı atar.
ornekListe.pop()
print("Listedeki son eleman olan 'nihil' atıldı:\n",
*ornekListe)

#sort() - Sıralama
# eğer liste sayısal bir liste ise: sayısal olarak küçükten büyüge
#Sözel bir liste ise alfabetik olarak sıralar.

sozelListe = ["okan", "burak", "nihil"]
sozelListe.sort()
print(sozelListe)

sayisalList = [2,1,4,8,12,-1]
sayisalList.sort() #Reverse = True parametresi de verebiliriz.
print(sayisalList)

#Listedeki bir elemanı değişirmek?
theList = ["ssssss", "aaaaaa"]
theList[0]= "abc"
print(theList)





# DEMETLER !
#değiştirilemezler, bu yüzden metodları azdır.

#Oluşturma?
OrnekDemet = [12, True, "nihil"]

#Erişim?
print(OrnekDemet[2]) #nihil

#Metodlar:
#count() - sayıyor işte. Parametre olarak verilen değerin
#kaç kere geçtiğini söyler. Yoksa 0 değerini döndürür.

print(OrnekDemet.count(True)) #1
print(OrnekDemet.count("kkk")) #0

#index() - parametre olarak verilen değerin ilk index numarasını
#verir. Verilen parametre demetin içinde yoksa hata verir.

print(OrnekDemet.index("nihil")) #2
print(OrnekDemet.index("hhh")) #error





#SOZLUKLER !
# keys and values!

#Olusturma:
ornekSozluk = {"keyOne": "valueOne", 2: 2.0, False: True}

#Erisim:
print(ornekSozluk["keyOne"]) #valueOne
print(ornekSozluk[False]) #True

#Deger Eklemek:
ornekSozluk["olmayanAnahtar"] = "olmayanDeger"
#eklenen bu yeni değer sozlugun sonuna gider.
# Ama zaten sozluklerde index olmadıgı için bunun bir önemi yok.

print(ornekSozluk["olmayanAnahtar"]) #olmayanDeger

#Deger Cıkarmak:
del ornekSozluk["olmayanDeger"]
print(ornekSozluk["olmayanDeger"]) #hata

#Metodlar:
#keys() - sözlükte bulunan anahtarları bir liste seklinde verir.
print("Sözlükteki anahtarlar:", ornekSozluk.keys())

#values() - sözlükte bulunan değerleri bir liste seklinde verir.
print("Sözlükteki değerler:", ornekSozluk.values())

#items() - sözlükte bulunan anahtar ve değerleri birlikte verir.
print("Sözlükteli anahtarlar ve değerler:", ornekSozluk.items())