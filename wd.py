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
####
zadanie 1 
x = int(input("Podaj liczbe calkowita"))
y = int(input("Podaj liczbe calkowita"))

if (x%y==0):
    print(f'Liczba {x} jest podzielna przez liczbe {y}')
else:
    print(f'Liczba {x} nie jest podzielna przez liczbe {y}')
#####
zadanie 2
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
#####
zadanie 3
import math
import cmath
z = cmath.sqrt(-1)
print("Czesc urojona: %d, czesc rzeczywista: %d"%(z.imag, z.real))
#####
zadanie 4
print(math.sin(15))
print(math.sin(30))
print(math.sin(45))
print(math.sin(60))
######
zadanie 5
def kolo(r):
    if r==0:
        print("Promien nie moze byc zerem")
        return 0
    obwod = 2 * math.pi * r
    pole = math.pi * pow(r,2)
    print("Pole wynosi: %f, obwod wynosi: %f"%(obwod, pole))
#####
zadanie 6
def kula(r):
    if r==0:
        print("Promien nie moze byc zerem")
    pole_powierzchni = 4 * math.pi * pow(r,2)
    objetosc = (4/3) * math.pi * pow(r, 3)
    print("Pole powierzchni wynosi: %f, objetosc wynosi: %f"%(pole_powierzchni, objetosc))
#####
zadanie 7
def rownanie_kwadratowe(a, b, c):
    delta = pow(b,2)- 4 * a * c
    x_1 = (pow(b,2)+delta)/ (2*a)
    x_2 = (pow(b,2)-delta)/ (2*a)
    print("x_1 wynosi %f, x_2 wynosi %f"%(x_1,x_2))
rownanie_kwadratowe(1,2,1)
#####
zadanie 8
from faker import Faker
fake = Faker()
losowy_text = fake.text()
print("Dlugosc tekstu wynosi: %d"%len(losowy_text))
#####
zadanie 9
import math
import wikipedia
print(wikipedia.summary("Olsztyn").upper())
####
zadanie 10
import math
import wikipedia

tekst = wikipedia.page("Guido van Rossum").content
print(tekst[-100:].title())


import math
stopnie = 30

rad = (stopnie * 2 * math.pi)/(360)

print(math.sin(rad))
########
zadanie 1 lab 3
from typing import Set

s: Set[int] = set()

while (len(s)<=10):

    s.add(int(input('Podaj liczbe')))

print(s)
####
zadanie 2

from typing import List

li: List[int] = []

while True:
    tmp = int(input('Podaj liczbe: '))
    if (tmp in li):
        break
    else:
        li.append(tmp)

print(li)
####
from typing import List

li: List[List[int]] = []

for i in range(4):
    tmp: List[int] = []
    for j in range(4):
        if j == i:
            tmp.append(1)
        else:
            tmp.append(0)
    li.append(tmp)

for el in li:
    print(el)

####
zadanie 4
from typing import List

li: List[List[int]] = []

value: int = 0

for i in range(0,4):
    tmp: List[int] = []
    for j in range(0,4):
        tmp.append(0)
    li.append(tmp)

for i in range(0,4):
    for j in range(0,4):
        if (j==i):
            li[j][i] = 0
        else:
            li[j][i] = value
        value += 1
print(li)
####
zadanie 5
from typing import Dict

dc: Dict[str, str] = {
    'one': 'jeden',
    'two': 'dwa',
    'three': 'trzy'
}
tmp: str = 't'
tmp = input('Podaj slowo: ')

while(tmp != 'end'):
    if tmp in dc:
        print(f'Tlumaczenie slowa {tmp} to: {dc[tmp]}')
    else:
        ang: str = input('Podaj tlumaczenie tego slowa: ')
        dc[tmp] = ang
        print(f'Dodalem slowo {tmp} z tlumaczeniem: {ang}')
    tmp = input('Podaj slowo: ')

print(dc)

#### LAB 4
##zadanie 1

def foo(x: int, y: int, operator: str) -> int:
    if operator == '+':
        return x+y
    elif operator == '-':
        return x-y

print(foo(1,2,'-'))

##zadanie 2 pierwiastek z sumy kwadratow roznicy
import math

def foo(x0: int, y0: int, x1: int, y1: int) -> float:
    return math.sqrt((x0-x1) ** 2 + (y0-y1) ** 2)

print(foo(1,1,2,2))

##zadanie 3
import math

def foo(a: int, b: int, c: int) -> float:
    sqrt_delta = math.sqrt(b ** 2 - 4 * a * c)
    x1 = (-b - sqrt_delta) / (2 * a)
    x2 = (-b + sqrt_delta) / (2 * a)
    return (x1,x2)

print(foo(1,2,1))
##zadanie 4
def foo(*args: int) -> int:
    min = args[0]
    if len(args) > 1:
        for el in args:
            if min > el:
                min = el
    return min
print(foo(1,-10,3, -3, 5))

#zadanie 5
def foo(*args: str) -> str:
    max: int = args[0]
    if len(args) > 1:
        for el in args:
            if len(max) < len(el):
                max = el
    return max

print(foo('Ala', 'ma', 'kotaaa'))

#zadanie 6
def foo(*args: int) -> float:
    suma = 0
    ilosc = 0
    for el in args:
        suma += el
        ilosc += 1
    return suma/ilosc

print(foo(1,2,3))

#zadanie 7
