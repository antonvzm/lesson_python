# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

from random import sample

size_list = 5
list_number = sample(range(1, size_list * 2), size_list)
if size_list % 2 == 0:
    pairs_numbers = [(list_number[i] * list_number[size_list - 1 - i])
                 for i in range(0, round(size_list/2))]
elif size_list < 5:
    pairs_numbers = [(list_number[i] * list_number[size_list - 1 - i])
                 for i in range(0, round(size_list/2)-1)]
    if size_list % 2 ==1:
        pairs_numbers.append(list_number[round((size_list-1)/2)])
else:
    pairs_numbers = [(list_number[i] * list_number[size_list - 1 - i])
                 for i in range(0, round(size_list/2-1))]
    if size_list % 2 ==1:
        pairs_numbers.append(list_number[round((size_list-1)/2)])
print(list_number, '=>', pairs_numbers)
print(round(size_list%2))