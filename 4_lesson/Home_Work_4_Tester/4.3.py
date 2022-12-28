# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

from random import randrange

list_number = []
size = int(input('in\n'))
if size < 0:
    print('Negative value of the number of numbers!')
else:
    for i in range(0, size):
        list_number.append(randrange(0, size))
    new_list = []
    for i in range(0, size):
        count = -1
        for j in range(0, size):
            if list_number[i] == list_number[j]:
                count = count + 1
        if count == 0:
            new_list.append(list_number[i])
    print('out\n', f'{list_number}\n', new_list)
