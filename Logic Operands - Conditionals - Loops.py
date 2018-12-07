import time

#Mantıksal Değerler ve Operatorler
# biliyoruz zaten, geç.

#Koşullu Durum Blokları - Ef & Elif - Else
# Biliyoruz, geç.

#Döngüler.
# Biliyoruz, geç.

#For döngüsü ile çift Sayı ayıklama örneği.

listem = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cifstSayilar = []
for sayilar in listem:
    if sayilar % 2 == 0:
        cifstSayilar.append(sayilar)
print("Listedeki çift sayılar:", cifstSayilar)


while True:
#Ünlü harfleri ayıklayalım.
    kullaniciGirisi = input("Lütfen bir kelime giriniz: ")
    if kullaniciGirisi.lower() != "q":
        UnluHarfler = ["a", "e", "i", "ı", "o", "ö", "u", "ü"]
        Yakalananlar = []
        for harfler in kullaniciGirisi:
            if harfler in UnluHarfler:
                Yakalananlar.append(harfler)
        print("Girdiğiniz kelimedeki ünlü harfler:", Yakalananlar)
    else:
        print("Çıkılıyor..")
        time.sleep(2)
        break

#Döngüler ile ilgili son örnek:
SozlukNo1 = {"okan": "topal", "nihil": False, "pi": 3.14}
SozlukNo2 = {"burak": "topal", "muffin": True, "yariCap": "r"}
#bu iki sözlükteki tüm anahtarları ve degerleri ayrı iki liste
# seklinde yazdıralım.

AnahtarlarListesi = []
DegerlerListesi = []
for anahtarlar, degerler in SozlukNo2.items():
    SozlukNo1[anahtarlar] = degerler
print("Sözlüklerin birleşmiş hali:\n", SozlukNo1)

for butunAnahtarlar, butunDegerler in SozlukNo1.items():
    AnahtarlarListesi.append(butunAnahtarlar)
    DegerlerListesi.append(butunDegerler)
print("Sözlüklerdeki anahtarlar sırasıyla:", AnahtarlarListesi)
print("Sözlüklerdeki degerler sırasıyla:", DegerlerListesi)


#range Fonskiyonu ile ilgili örnek:
# 1-100 arası çift sayılar :p

for sayilar in range(1, 101):
    if sayilar % 2 == 0:
        print(sayilar)