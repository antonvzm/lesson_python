# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# *Пример:*

# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти

print('Введите номер четверти: ')
number = int(input())
if number == 1:
    print('1 -> x > 0, y > 0')
if number == 2:
    print('2 -> x < 0, y > 0')
if number == 3:
    print('3 -> x < 0, y < 0')
if number == 4:
    print('4 -> x > 0, y < 0')
if number < 1 or number > 4:
    print('Нет такой четверти')