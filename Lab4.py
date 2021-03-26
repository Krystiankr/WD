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
