#String Indexleme Ve Parçalama

a = "oh shit!"
print(a[3:]) #shit!

#reverse String
print(a[::-1])

print(a[:len(a)-1]) #oh shit

#Indexleme soldan başlar sağa doğru gider.
#Ilk index numarası 0.
#Parametre olarak verilen ikinci değer dahil değildir.
#Sondan başa doğru indexleme -1 ile başlar.

print(a[-1]) #!


#Veri Tipi Dönüşümleri
kullaniciGirisi = input("Bir sayi giriniz: ")
kullaniciGirisi = int(kullaniciGirisi)
print("Girdiğiniz sayinin 2 katı:", kullaniciGirisi*2)

#Not: Cevrilecek değerin cevrilen veri tipine uygun olması gerekir.

#Print Fonksiyonu Ve Formatlama
#Biliyoruz- geçelim.