# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def Sum_number(number_one: int , number_two: int):
    if number_two == 0:
        return number_one
    return Sum_number(number_one + 1, number_two - 1)

def Is_number(text: str) -> int: 
    flag = False    
    while(flag == False):
        number_text = int(input(text))
        if number_text > 0:
            flag = True
            return number_text
        else:
            print("Число должно быть положительным")
           
text_1 = "Введите первое число "
text_2 = "Введите второе число "
number_1 = Is_number(text_1)
number_2 = Is_number(text_2)

print(f"{number_1} + {number_2} = {Sum_number(number_1, number_2)}")