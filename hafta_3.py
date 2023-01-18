#class
class sinif:
    pass
nesne = sinif()
print(type(nesne))

#class_degisken
class sinif:
    a = 0
    b = "dfg"
    c = [1, 3, 5]
nesne = sinif()
print(nesne.a)
nesne.a = 999
print(nesne.a)

#class_method
class sinif:
    a = 5
    b = "dfg"
    c = [1, 3, 5]
    def yazdir(self):
        d = 100
        print(d, self.a)
    def yazdir2(self, t):
        self.yazdir()
        print(t)
nesne = sinif()
nesne.yazdir()
nesne.yazdir2("jbhjv")

#class_init
class sinif:
    metin = ""
    def __init__(self, a):
        self.metin = a
nesne = sinif("Metin")
print(nesne.metin)

#class_del
class sinif:
    metin = ""
    def __init__(self, a):
        self.metin = a
    def __del__(self):
        print("beni siliyorlar")
nesne = sinif("Metin")
del nesne

#class_str
class sinif:
    metin = ""
    def __init__(self, a):
        self.metin = a
    def __str__(self):
        return "Yazdırılan : " + self.metin
nesne = sinif("python")
print(nesne)

#try_except
x = "ghb"
try:
    y = 5 + x
except:
    print("'int' and 'str'")

#termcolor
from termcolor2 import c

print(c("hello").red.on_white.blink.underline.dark)

#file_operations
dosya = open("metin.txt", 'r')
for satir in dosya:
    print(satir[:-1])

#file_write
dosya = open("cop.txt", 'w')
print("dsgfd", file=dosya)
dosya.close()

#python_python
dosya = open("kod.txt", 'w')
print("print('efsane python')", file=dosya)
dosya.close()
dosya = open("kod.txt", 'r')
satir = dosya.readline()
eval(satir)

