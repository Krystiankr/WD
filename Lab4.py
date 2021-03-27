##Zadanie 1
def foo(x: int, y: int, operator: str) -> int:
    if operator == '+':
        return x+y
    elif operator == '-':
        return x-y

print(foo(1,2,'-'))

##zadanie 2
import math

def foo(x0: int, y0: int, x1: int, y1: int) -> float:
    return math.sqrt((x0-x1) ** 2 + (y0-y1) ** 2)

print(foo(1,1,2,2))

##Zadanie 3
import math

def foo(a: int, b: int, c: int) -> float:
    sqrt_delta = math.sqrt(b ** 2 - 4 * a * c)
    x1 = (-b - sqrt_delta) / (2 * a)
    x2 = (-b + sqrt_delta) / (2 * a)
    return (x1,x2)

print(foo(1,2,1))
##Zadanie 4
def foo(*args: int) -> int:
    min = args[0]
    if len(args) > 1:
        for el in args:
            if min > el:
                min = el
    return min
print(foo(1,-10,3, -3, 5))

#Zadanie 5
def foo(*args: str) -> str:
    max: int = args[0]
    if len(args) > 1:
        for el in args:
            if len(max) < len(el):
                max = el
    return max

print(foo('Ala', 'ma', 'kotaaa'))

#Zadanie 6
def foo(*args: int) -> float:
    suma = 0
    ilosc = 0
    for el in args:
        suma += el
        ilosc += 1
    return suma/ilosc

print(foo(1,2,3))
#Zadanie 8
from typing import List


def lista(listaa: List[int]) -> [List, List]:
    lista_p = []
    lista_np = []
    for el in listaa:
        if el % 2 == 0:
            lista_p.append(el)
        else:
            lista_np.append(el)
    return lista_p, lista_np


if __name__ == "__main__":
    main_list = [1, 2, 3, 692, 1, 123]
    print(f"Lista parzysta: {lista(main_list)[0]}, Lista nieparzysta: {lista(main_list)[1]}")

##Zadanie 9
from typing import Generator
import math

def Palindrome(word: str) -> bool:
    n = len(word)

    if n % 2 == 0:
        for el in range(0,(math.ceil((n-1)/2))):
            if word[el] != word[n-1-el]:
                return False
    else:
        for el in range(0, int((n-1)/2)):
            if word[el] != word[n-1-el]:
                return False
    return True

if __name__ == "__main__":
    slowo = "00141005"
    if Palindrome(slowo):
        print(f"Slowo: {slowo} jest palindromem!")
    else:
        print(f"Slowo: {slowo} nie jest palindromem.")
##Zadanie 10
from typing import List, Any


def typy(*args) -> List[List[Any]]:
    lista_string = []
    lista_int = []
    lista_float = []
    lista_tuples = []
    lista_set = []

    for el in args:
        if isinstance(el, str):
            lista_string.append(el)
        elif isinstance(el, int):
            lista_int.append(el)
        elif isinstance(el, float):
            lista_float.append(el)
        elif isinstance(el, tuple):
            lista_tuples.append(el)
        elif isinstance(el, set):
            lista_set.append(el)
    return [lista_int, lista_float, lista_string, lista_tuples, lista_set]


if __name__ == "__main__":
    print(typy(3, 2.2, "eee", (2, 12, 42), {35}, {1, 45, 199}, "dom"))
##Zadanie 11
from typing import Generator


def even_numbers(n: int) -> Generator[int, None, None]:
    while True:
        yield n
        n += 2


if __name__ == "__main__":
    generator: Generator[int, None, None] = even_numbers(10)
    for x in range(10):
        print(next(generator))
        
##Zadanie 12
from typing import Generator


def artithmetic_progression(n: int) -> Generator[int, None, None]:
    ciag = 0
    while True:
        yield ciag
        ciag = 3 * n - 7
        n += 1


if __name__ == "__main__":
    generator: Generator[int, None, None] = artithmetic_progression(4)
    
    for x in range(15):
        print(next(generator))

##Zadanie 13
from typing import Generator
def prime_number() -> Generator[int, None, None]:
    licznik = 0
    tmp = 0
    while True:
        yield licznik
        if (licznik == 0):
            print(f"F{licznik}: {tmp}")
            prev = 0
        elif (licznik == 1):
            print(f"F{licznik}: 1")
            next = 1
        else:
            tmp = prev + next
            prev = next
            next = tmp
            print(f"F{licznik}: {tmp}")
        licznik += 1
if __name__ == "__main__":
    generator: Generator[int, None, None] = prime_number()
    for x in range(27):
        next(generator)
##Zadanie 14
import math
from typing import Generator
def prime_number() -> Generator[int, None, None]:
    n = 2
    while True:
        pierwsza = True
        yield n
        n += 1
        if (n%2==0):
            pierwsza = False
            continue
        for x in range(2,round(math.sqrt(n)+1)):
            if (n%x==0):
                pierwsza = False
                break
        if pierwsza:
            print(f"Liczba {n} jest pierwsza")

if __name__ == "__main__":
    generator: Generator[int, None, None] = prime_number()
    for x in range(33):
        next(generator)
