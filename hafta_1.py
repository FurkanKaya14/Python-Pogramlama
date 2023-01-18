#hello_world
print("Merhaba Dünya")

#syntax
print("Merhaba")
print("Dünya")
print("Dünya")
if 1 > 2:
 print("Dünya")
print("Merhaba")
if 1 > 2:
      print("1")
      print("2")

#degiskenler
a = 5
b = None
c = 7.2
d = -354631351
print(d)
e = True
print(e)
print(a, b, c, d, e)
print(a, b, c, d, e, sep=", ")
print(a, b, end="")
print("aynı satırdayım")
print(a); print(b); print(c)
a, b, c = 3, 5, 7
print(a, b, c)
t = "ghyf"
f = 'tg'
g = 'a'
print(t, f, g)

#degisken_tipleri
a = 5
b = None
c = 7.2
d = "cfdfgvbfd"
e = 'edc'
f = False
g = 3265468786352468768435112
print("a :", type(a))
print("b :", type(b))
print("c :", type(c))
print("d :", type(d))
print("e :", type(e))
print("f :", type(f))
print("g :", type(g))
h = [1, 2]
i = {a:"dsvs", d:"jmn"}
j = (1, 2, 3)
print("h :", type(h))
print("i :", type(i))
print("j :", type(j))

#aciklama_yorum_satirlari
#tek satır için
"""
birden
fazla
satır
için
"""
'''
açıklama
için
'''
a='''gfgcvh
jdch
kcj
ddkco
'''
print(a)

#tip_donusumu
a = 10
print(type(a))
a = float(10)
print(type(a))
a = str(10)
print(type(a))
class a:
    b = 10
t = a
print(type(a))
print(type(t))
print(t.b)
print(type(t.b))

#kucuk_buyuk_harf
a = 5
A = 10
print(a, " : ", A)

#evrensel_degiskenler
a = 5
def b():
    a = 10
    print(a)
b()
print(a)
def c():
    global a
    a = 10
    print(a)
c()
print(a)

#buyuk_sayilar
a = 313584685231654684631313546468313187681316546654
b = 321586765214687896138761231687879431468316764313
print(a*b)

#rastgele_sayi
from random import randrange
rastgele_sayi = randrange(1, 20)
print(rastgele_sayi)

#metinler
a = "frefr"
b = """tgegetg
vgregvv
gbgtrb"""
print(a, b)
print(a[0])
print(a[1])
print(b[4])
print(b[5])
print("a'nın uzunluğu :", len(a))
print("b'nin uzunluğu :", len(b))

#metin_karsilastirma
a = "Balikesir"
if a == "Balikesir":
    print("a balıkesire eşit")
if "kes" in a:
    print("a'da kes var")
if "KES" in a:
    print("a'da KES var")
if "eks" in a:
    print("a'da eks var")

#metni_bicimli_yazdırma
a = 5
b = 10
c = 15
print("a = {} - b = {} - c = {}".format(a, b, c))
print("balikesir".capitalize())
print("balikesir".upper())

#escape_char
a = 'Balıkesir\'in esnafı'
print(a)
a = 'Balıkesir\\in esnafı'
print(a)

#boolean
print(10 > 5)
print(10 < 5)
a = 10 > 5
print(a)

#operatorler
print(3 + 5)
print(3 - 5)
print(3 * 5)
print(3 / 5)
print(9 % 2)
print(9 // 2)
print(3 ** 5)

#listeler
a = [1, 2, 3]
b = [True, 1.6, 35464313548, None, [1, "ad", 7.2]]
print(a)
print(b)
print(b[0])
print(b[4][1])
tr = "Türkiye"
print(tr[1:4])
b[4][1] = [6, 99, 2.8, "soyad"]
print(b[4][1])
print(b[4][1][3])

#listeler_2
a = [1, 6]
a.append(5)
print(a)
a.pop()
print(a)
a.append(5)
a.remove(1)
print(a)
a.insert(1, 100)
print(a)
print(a.pop())
print(a)
a.clear()
print(a)

#listeler_3
liste = ["Elma", "Armut", "Ayva"]
liste.sort()
print(liste)
liste.reverse()
print(liste)
def fonksiyon(n):
  return abs(n - 50)
sayi_listesi = [100, 50, 65, 82, 23]
sayi_listesi.sort(key=fonksiyon)
print(sayi_listesi)

#listeler_4
sayi_listesi = [3, 5, 10, -8, 9, 15]
a = sayi_listesi
print(a)
sayi_listesi.sort()
print(a)
sayi_listesi = [3, 5, 10, -8, 9, 15]
a = sayi_listesi.copy()
print(a)
sayi_listesi.sort()
print(a)

#tuples
degisitirilemez = ("Elma", "Armut", "Ayva")
print(degisitirilemez)

print(degisitirilemez[0])

#dictionary
sozluk = {"marka": "Ford","model": "Mustang","yıl": 1964
}
print(sozluk)
print(sozluk["marka"])
print(sozluk["model"])
print(sozluk["yıl"])
sozluk["renk"] = "siyah"
print(sozluk)
print(sozluk["renk"])
sozluk["renk"] = "beyaz"
print(sozluk)

print(sozluk.keys())
print(sozluk.values())

for i in sozluk.keys():
    print(i, ":", sozluk[i])


