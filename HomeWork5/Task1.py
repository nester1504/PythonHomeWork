# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
power_result = 1

def Exponentiation(numb: int , power: int):
    if power == 0:
        return power_result
    else:       
        return numb * Exponentiation(numb, power - 1)

number = int(input("Введите число "))
number_in_power = int(input("Введите степень числа "))

print(f"Число {number} в степени {number_in_power} = {Exponentiation(number, number_in_power)}")