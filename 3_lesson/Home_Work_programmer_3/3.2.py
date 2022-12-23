# 2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


list_numbers = '2 3 4 5 6'.split()
list_numbers = list(map(int, list_numbers))
pairs_numbers = [(list_numbers[i] * list_numbers[len(list_numbers) - i-1])
                 for i in range(0, len(list_numbers)//2+1)]
print(list_numbers, '=>', pairs_numbers)
