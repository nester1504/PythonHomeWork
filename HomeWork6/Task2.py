# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
import random

length_list_1 = int(input("Введите длину списка: "))

list_1 = []

for i in range(length_list_1):
    list_1.append(random.randint(-10, 10))

star_number = int(input("Введите начало отрезка: "))
end_number = int(input("Введите конец отрезка: "))

print(list_1)
result = [i for i, x in enumerate(list_1) if star_number <= x <= end_number]
print(result)
