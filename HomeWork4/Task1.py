#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
#повторениями). Выдать без повторений в порядке возрастания все те числа, которые
#встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
#элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random

length_list_1 = int(input("Введите длину первого списка: "))
length_list_2 = int(input("Введите длину второго списка: "))

list_1 = []
list_2 = []

for i in range(length_list_1):
    list_1.append(random.randint(0, 10))

for i in range(length_list_2):
    list_2.append(random.randint(0, 10))

list_3 = list(set(list_1) & set(list_2))

print(list_1)
print(list_2)
print(list_3)