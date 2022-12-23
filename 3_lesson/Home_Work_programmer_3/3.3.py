# 3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list_numbers = '1.1 1.2 3.1 5 10.01'.split()
list_numbers = list(map(float, list_numbers))
fractional_numbers = [round((list_numbers[i] - int(list_numbers[i])), 5)
                     for i in range(0, len(list_numbers))]
min = fractional_numbers[0]
max = fractional_numbers[0]
for i in range(1, len(fractional_numbers)):
    if max < fractional_numbers[i]:
        max = fractional_numbers[i]
    if min > fractional_numbers[i] and fractional_numbers[i] != 0.0:
        min = fractional_numbers[i]
print(list_numbers, '=>', max - min)
