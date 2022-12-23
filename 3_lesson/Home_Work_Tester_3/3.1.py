# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

from random import sample

size_list = int(input('in\n '))
list_number = sample(range(1, size_list * 2), size_list)
sum_number = 0
for i in range(0, len(list_number), 2):
    sum_number += list_number[i]
print('out\n', list_number, '\n', sum_number)
