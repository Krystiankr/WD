import math
from typing import List


def task_lista(list1: List) -> (int, int):
    number_p: int = 0
    number_n: int = 0
    for el in list1:
        if el >= 0:
            number_p += 1
        else:
            number_n += 1
    return number_p, number_n


def task_amount(list2: List) -> List[int]:
    list_copy = []
    for el in list2:
        n1 = 0
        for e1 in list2:
            if el == e1:
                n1 += 1
        list_copy.append(n1)
    return list_copy


def square(a1: int, n1: int) -> List[int]:
    list_new = []
    for el in range(n1-a1+1):
        list_new.append((el+int(a1)) ** 2)
    return list_new


print("Zadanie 1")
wynik1: float = ((math.sqrt(5)-1)/4) ** 2+((math.sqrt(10+2*math.sqrt(5)))/4) ** 2

wynik2: float = (math.sin(65) + (4/5)**2) ** (1/4)

print(f'Wyrazenie_1: {wynik1:.2f}, Wyrazenie_2: {wynik2:.2f}')
print("Zadanie 2")
f = open("req.txt", "r")

task0 = f.readlines()
task2 = task0[0][31:51]


print("Zadanie 2a")
count1 = 0
task1 = task0[0][15:35]
for i in task1:
    if i.islower():
        count1 += 1

print(f"The number of lowercase characters is: {count1}")

print("Zadanie 2a")
count2 = 0
search_letter = 'b'
for i in task2:
    if i == search_letter:
        count2 += 1
if count2 > 0:
    print(f"The number of {search_letter} is: {count2}")
else:
    print(f"There is no {search_letter}")

print(task2)

print("Zadanie 3")
result = task_lista([3, 4, 9, -3, -1])
print(f"Number positive: {result[0]}, number negative: {result[1]}")

print("Zadanie 4")
org = [2, 5, 7, 2, 1, 3, 3]

result1 = task_amount(org)
print(result1)
print("Zadanie 5")

zm = True
result2 = 0
while zm:
    a = input("a: ")
    n = input("n: ")
    if not(n.isnumeric() and a.isnumeric()):
        print("Input correct data only numbers!")
        continue
    if n > a:
        zm = False
        result2 = square(int(a), int(n))
        break
    else:
        print("a must be higher than a")

print(result2)
