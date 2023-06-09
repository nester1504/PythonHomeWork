#Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
#круглой грядке, причем кусты высажены только по окружности. Таким образом, у
#каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
#Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
#выросло различное число ягод – на i-ом кусте выросло ai
# ягод.
#В этом фермерском хозяйстве внедрена система автоматического сбора черники.
#Эта система состоит из управляющего модуля и нескольких собирающих модулей.
#Собирающий модуль за один заход, находясь непосредственно перед некоторым
#кустом, собирает ягоды с этого куста и с двух соседних с ним.
#Напишите программу для нахождения максимального числа ягод, которое может
#собрать за один заход собирающий модуль, находясь перед некоторым кустом
#заданной во входном файле грядки.

import random

length_list = int(input("Введите количество кустов: "))

list = []
max_harvest = 0

for i in range(length_list):
    list.append(random.randint(0, 10))

print(list)

for i in range(len(list) -1):
    if max_harvest < list[i - 1] + list[i] + list[i + 1]:
        max_harvest = list[i - 1] + list[i] + list[i + 1]

if max_harvest < list[-2] + list[-1] + list[0]:
        max_harvest = list[-2] + list[-1] + list[0]

print(max_harvest)