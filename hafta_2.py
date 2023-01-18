#main
a = 5
b = 4
c = -5
if __name__ == "__main__":
    print(a)

#if
a = 5
b = 4
c = -5
if a > c:
    print("a c'den büyüktür")
if c < 0: print("c 0'dan küçüktür")
if c > 0: print("c 0'dan büyüktür"); print("c 5 oldu"); c=5

#elif
a = 5
if a > 5:
    print("a 5'ten büyüktür")
elif a == 5:
    print("a 5'e eşittir")
else:
    print("a 5'ten küçüktür")

#short_if
a = 5
b = 5
print("a ile b farklı") if a != b else print("a ile b aynı")
print("a b'den büyüktür") if a > b else print("a ie b eşittir") if a == b else print("b a'dan büyüktür")

#and_or
a = 5
b = 10
if a < 10 or c < 10:
    print("a ya da b'10 dan küçüktür")
if a == 5 and c == 10:
    print("a 5'e ve b 10'a eşittir")

#is
a = 5
if a is 4:
    print("a 4'e eşittir")
if a is not 4:
    print("a 4'e eşit değildir")

#ic_ice_kosul
a = 4
c = 11
if a < 5:
    if c > 10:
        print("python")

#pass
a = 5
if a > 5:
    pass
print("python")

#while
a = 5
while a < 10:
    a += 1
    if a == 8:
        continue
    if a == 12:
        break
    print(a)
else:
    print("a artık 15 ya da daha büyük")

#for
for i in range(0, 10):
    print(i)
for i in range(0, 10, 2):
    print(i)
for i in range(10, 0, -2):
    print(i)

#for_2
liste = ["as", True, 1.9, 5, ["mor", "siyah", "sarı"]]
for i in liste:
    print(i)
for i in liste[4]:
    print(i)

#for_else
for i in range(0, 3):
    print(i)
else:
    print("for bitti")

#enumerate
liste = ["as", True, 1.9, 5, ["mor", "siyah", "sarı"]]
for i, eleman in enumerate(liste):
    print(i+1, ". eleman : ", eleman, sep="")

#fonksiyon
def yazdir():
    print("Yazıyorum")
yazdir()

#parametrik_fonksiyon
def topla(a, b):
    return a+b
print(topla(3, 5))

#iki_deger_dondurme
def topla_carp(a, b):
    return a + b, a * b
toplam, carpim = topla_carp(3, 5)
print(topla_carp(3, 5))
print(toplam, carpim)

#birden_cok_parametre
def hepsini_topla(*a):
    toplam = 0
    for deger in a:
        toplam += deger
    return toplam
print(hepsini_topla(3, 5, 9, 15.2, 36))


#dictionary_parametre
def birim_islem(**birim):
  print("birimin tipi :", type(birim))
  print("Birim Adı : " + birim["ad"])
  print("Birim Tipi : ", birim["tip"])
  print("Birim Yılı : ", birim["yil"])
birim_islem(ad="Balıkesir", tip="Üniversite", yil=1992)

#lambda
lambda_fonksiyonu = lambda a: a + 10
print(lambda_fonksiyonu(5))

#cok_parametreli_lambda
topla = lambda a, b: a + b
def toplama(a, b):
    return a + b
print(topla(3, 5))
print(toplama(3, 5))
print(type(topla))
print(type(toplama))

#lambdanin_gucu
#sinav sorusu
def fonksiyonum(n):
  return lambda a: a * n
katini_al = fonksiyonum(2)
print(katini_al(5))
katini_al = fonksiyonum(5)
print(katini_al(5))