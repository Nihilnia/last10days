###############
##### String Indexleme #####
###############

a = "Hello World!"
print(a[6]) #W

print(a[0:6]) #Hello 

print(a[::-1]) #Reverse String

print(a[:3]) #Hel

###############
##### Veri Tipi Dönüşümleri #####
###############

a = "12"
print(type(a)) #String

a = int(a)
print(type(a)) #Integer

b = "10.5"
print(type(b)) #String

b = float(b)
print(type(b)) #Float
print(b)

#UNUTMA: Kullanıcıdan aldığımız her şey String.


###############
##### Print Fonskiyonu ve Formatlama#####
###############
print("Hello {}, it's {}".format("World", "Nihil!"))

####################
##### Listeler #####
####################
ornekListe = ["Nihil", 24, "Python", 10.5]
print(ornekListe)

#Metodları?
#append() - listenin sonuna eleman ekler.
ornekListe.append("Ra Ra Rasputin!")
print(ornekListe)

#sort() - sıralama - Not: sıralama yapmak için liste içindeki elemanların tamamen sayısal olması
# ya da string olması gerekir.

#Ornek: (Sayısal listelerde küçükten büyüğe sıralar, reverse ile büyükten kücüğe)
ornekListe2 = [12, 13, 10, 10.5, 1212]
ornekListe2.sort()
print(ornekListe2)

#Ornek2: (Sözel listelerde ise alfabetik sıralar, reverse ile tersten alfabetik elbette)
ornekListe3 = ["Nihil", "Python", "Spotify", "Apple"]
ornekListe3.sort()
print("Alfabetik", ornekListe3)
ornekListe3.sort(reverse = True)
print("Tersten Alfabetik", ornekListe3)

#pop() - eleman cıkarma (parametre verilmezse en sondaki elemanı cıkarır.) parametre ise index no

ornekListe4 = ["Nihil", "Python", "Spotify", "Apple"]
print("Çıkarılmamış hali:", ornekListe4)
ornekListe4.pop()
print("Son elemanı cıkarılmıs hali:", ornekListe4)
ornekListe4.pop(2)
print("Spotify çıkarılmış hali:", ornekListe4)


####################
##### DEMETLER #####
####################

ornekDemet = ("Nihil", "Python", 2018)

#Değiştirilemezler, bu yüzden fazla metodları yoktur.
# count() Metodu: Parametre olarak verilen değerin 
# demet içinde kaç kere geçtiğini sayısal olarak verir.
# Hiç geçmiyorsa 0 değerini döndürür.

print(ornekDemet.count("Nihil"))