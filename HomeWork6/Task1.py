# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: 
# an= a1+ (n-1) * d.

# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

one_number_list = int(input("Введите первое число списка "))
step_list = int(input("Введите шаг между числами в списке "))
length_list = int(input("Введите количество чисел в списке "))

list_1 = []

def Creating_a_list(begin: int, step: int, size: int, list_creat: list):
    for i in range(begin , begin + step * size, step):
        list_creat.append(i)       
    return list_creat

print(Creating_a_list(one_number_list, step_list, length_list, list_1))