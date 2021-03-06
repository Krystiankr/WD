poniżej linki do ćwiczeń z wizualizacji danych.
Zwracam się z prośbą o przekazanie studentom.


Lab 1: https://meet.google.com/vio-ceaa-cjh

Lab 2: https://meet.google.com/zwm-kuuc-fjq

Lab 3: https://meet.google.com/cmh-tubu-qvn

Lab 4: https://meet.google.com/cus-szgr-gxj

Lab 5: https://meet.google.com/zfn-rumc-gae

Lab 6: https://meet.google.com/yiz-oryh-itz

Lab 7: https://meet.google.com/ahg-vfvi-fxo

Lab 8: https://meet.google.com/ccy-uoem-cwm

Lab 9: https://meet.google.com/ojk-ugoo-miq

Lab 10: https://meet.google.com/rrs-xqxw-tuc


Z wyrazami szacunku,
Magdalena Zaczek.


C:\Users\Krystian\PycharmProjects\Lab2\venv
C:\Users\Krystian\AppData\Local\Programs\Python\Python39\python.exe

pip install -r requirements.txt

import wikipedia

wikipedia.set_lang("pl")

#print(wikipedia.page("Galapagos").content)

print(wikipedia.summary("Python"))

print(wikipedia.page("Python").url)

#print(wikipedia.page("Galapagos").content)

x = int(input("Podaj liczbe calkowita: "))
y = int(input("Podaj liczbe calkowita: "))

if (x%y==0):
    print("%d jest podzielne przez %d"%(x, y))
else:
    print("%d nie jest podzielne przez %d"%(x,y))

import math

def wyr_1(x, y ,z):
    return pow((x+y/z),(x-z))

def wyr_2(x, z):
    if (pow(x,1/z)-pow(x,1/z))==0:
        print("Nie dzielimy przez 0")
    else:
        return (pow(x,1/2)-pow(x,1/z))/(pow(x,1/z)-pow(x,1/z))

print(wyr_2(1,2))

import math

def wyr_1(x, y ,z):
    return pow((x+y/z),(x-z))

def wyr_2(x, z):
    if (pow(x,1/z)-pow(x,1/z))==0:
        print("Nie dzielimy przez 0")
    else:
        return (pow(x,1/2)-pow(x,1/z))/(pow(x,1/z)-pow(x,1/z))

def wyr_3(x,y):
    if x==0:
        print("Nie dzielimy przez 0")
    else:
        return math.pi/x - math.atan(y)

def wyr_4(x,y,z):
    if (pow(z,y)/math.exp(10))==0:
        print("Nie dzielimy przez 0")
    else:
        return pow((pow(x,3)-y),math.pi)/(pow(z,y)/math.exp(10))

def wyr_6(x, y):
    return ((math.sin(x)+math.cos(x))/(math.sin(x)+math.cos(x)))

def wyr_7(x,y):
    return math.log(x,y)

zad 3
import math
import cmath
z = cmath.sqrt(-1)
print("Czesc urojona: %d, czesc rzeczywista: %d"%(z.imag, z.real))

print(math.sin(15))
print(math.sin(30))
print(math.sin(45))
print(math.sin(60))

zad 5
def kolo(r):
    if r==0:
        print("Promien nie moze byc zerem")
        return 0
    obwod = 2 * math.pi * r
    pole = math.pi * pow(r,2)
    print("Pole wynosi: %f, obwod wynosi: %f"%(obwod, pole))

def kula(r):
    if r==0:
        print("Promien nie moze byc zerem")
    pole_powierzchni = 4 * math.pi * pow(r,2)
    objetosc = (4/3) * math.pi * pow(r, 3)
    print("Pole powierzchni wynosi: %f, objetosc wynosi: %f"%(pole_powierzchni, objetosc))

def rownanie_kwadratowe(a, b, c):
    delta = pow(b,2)- 4 * a * c
    x_1 = (pow(b,2)+delta)/ (2*a)
    x_2 = (pow(b,2)-delta)/ (2*a)
    print("x_1 wynosi %f, x_2 wynosi %f"%(x_1,x_2))
rownanie_kwadratowe(1,2,1)

import math
import wikipedia
#print(wikipedia.summary("Olsztyn").upper())

tekst = wikipedia.page("Guido van Rossum").content

print(tekst[-100:])

import math
import wikipedia

tekst = wikipedia.page("Guido van Rossum").content
print(tekst[-100:].title())
