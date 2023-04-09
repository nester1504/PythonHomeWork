"""Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) """


import random

number = random.randint(100, 999)
sum = number // 100 + (number % 100) // 10 + number % 10

input(f'Сумму цифр числа {number} =  {sum}')