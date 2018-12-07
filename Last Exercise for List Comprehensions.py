# 1'den 100'e kadar olan sayıları list comprehensions 
# kullanarak yazdır.

CiftSayilar = [x for x in range(1, 101) if x % 2 == 0]
print(CiftSayilar)