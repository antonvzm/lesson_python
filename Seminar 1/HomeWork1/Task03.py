# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
print('x = ')
x = int(input())
print('y = ')
y = int(input())
if x == 0:
    print('x не может быть равен 0, введите другое число')
    x = int(input())
if y == 0:
    print('y не может быть равен 0, введите другое число')
    y = int(input())
if x > 0 and y > 0:
    print(f'{x}, {y} -> 1')
if x < 0 and y > 0:
    print(f'{x}, {y} -> 2')
if x < 0 and y < 0:
    print(f'{x}, {y} -> 3')
elif x > 0 and y < 0:
    print(f'x = {x}, y = {y} -> 4')