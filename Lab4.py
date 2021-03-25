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
