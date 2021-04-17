from typing import List, Any, Iterator
import math

class Square:
    def __init__(self, side: int) -> None:
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return self.side * 4

class Triangle:
    def __init__(self, side: int, base: int):
        self.side = side
        self.base = base
    def area(self):
        h: float = math.sqrt(self.side ** 2 - (self.base/2) ** 2)
        return (h * self.base) / 2
    def perimeter(self):
        return 2 * self.side + self.base


class Tree:
    def __init__(self, name: str, height: int, leafs: int):
        self.name = name
        self.height = height
        self.leafs = leafs

    def grow_up(self, increase: int):
        self.height += increase

    def grow_wide(self, increase):
        self.leafs = increase

    def show(self):
        print(f"Name={self.name}, Height={self.height}, Leafs={self.leafs}")


class Matrix:
    def __init__(self, listy: List[List[int]]):
        self.listy = listy

    def transpose(self) -> List[List[int]]:
        tmp: List[List[int]] = []
        for kol in len(self.listy[0]):
            tmp.append([])

        for row in enumerate(self.listy):
            tmp.

    def size(self) -> str:
        return 'a'

    def set_value(self, pozycja, wartosc):
        pass

    def get_value(self, pozycja) -> int:
        return 1

    def is_identity(self) -> bool:
        return True





"""
kwadrat: Square = Square(3)
trojkat: Triangle = Triangle(4,5)

print(f"Pole: {kwadrat.area()}, Obwod: {kwadrat.perimeter()}")
print(f"Pole: {trojkat.area()}, Obwod: {trojkat.perimeter()}")

lista: List[Any] = []
for i in range(0,11):
    lista.append(Square(i+11))

#Zadanie 3
print("Kwadraty:")
for count ,el in enumerate(lista):
    print(f"{count}|Bok={count+11} Pole={el.area()}, Obwod={el.perimeter()}")

#Zadanie 4
list_tree: List[Any] = []
for i in range(0, 5):
    list_tree.append(Tree(3+i,4+i,5+i))
    print(f"Tree({i}) ", end='')
    list_tree[i].show()

list_tree[1].grow_up(5)
list_tree[3].grow_wide(3)
list_tree[3].grow_up(2)
print("*Zmiana*")
for i in range(0, 5):
    print(f"Tree({i}) ", end='')
    list_tree[i].show()
    """
#Zadanie 5
