# Asal Sayı Sorgulayıcı

while True:
    kullaniciGirisi = int(input("Sorgulanacak sayi: "))
    bolenlerinTamami = []
    for bolenler in range(1, kullaniciGirisi):
        if kullaniciGirisi % bolenler == 0:
            bolenlerinTamami.append(bolenler)

    if len(bolenlerinTamami) > 1:
        print(kullaniciGirisi, "asal değildir. Bölenleri:", *bolenlerinTamami)
    else:
        print(kullaniciGirisi, "asaldır. Sadece kendisine ve 1'e tam bölünür.")