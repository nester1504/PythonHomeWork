"""Задача 8: Требуется определить, 
можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no """

length = int(input("Введите длину шоколадки "))
width = int(input("Введите ширину шоколадки "))
slice = int(input("Введите количество долек которые нужно отломить от шоколадки "))

if (length * width - slice) % 2 == 0 and (length * width) > slice and (length * width - slice) > 1:
    print("Шоколадку можно разломить на два прямоугольника")
else:
    print("Шоколадку НЕЛЬЗЯ разломить на два прямоугольника")