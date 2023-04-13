#Задача 10: На столе лежат n монеток. 
#Некоторые из них лежат вверх решкой, 
#а некоторые – гербом. Определите минимальное число монеток, 
#которые нужно перевернуть, чтобы все монетки были 
#повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть
import random

coin = int(input("Введите количество монет "))
count_heads = 0
count_tails = 0
for i in range(coin):
    heads_and_tails = random.randint(0,1)
    if heads_and_tails != 1:
        count_heads = count_heads + 1
    else:
        count_tails = count_tails + 1
if count_heads >= count_tails:
    print(f"Минимальное количество монет, которые нужно перевернуть {count_tails}")
else:
    print(f"Минимальное количество монет, которые нужно перевернуть {count_heads}")
    
    
