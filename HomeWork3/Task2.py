#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
#*Пример:*
#
#   5
#   1 2 3 4 5
#    6
#    -> 5

import random

list = []

n = int(input("Введите длину списка "))

for i in range(n):
    list.append(random.randint(1, 100))

print(list)

number = list[0]
number2 = 0

x = int(input("Введите число "))
 
element = list[0]  

for i in list:
    if abs(i - x) < abs(element - x):
        element = i

print(f"Самый близкий по величине элемент к числу X: {element}")