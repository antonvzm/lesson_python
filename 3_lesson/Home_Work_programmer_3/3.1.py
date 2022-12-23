# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list_numbers = '2 3 5 9 3'.split()
list_numbers = list(map(int, list_numbers))
odd_index = [(list_numbers[i])
             for i in range(0, len(list_numbers)) if i % 2 != 0]
print(list_numbers, ' -> на нечётной позиции элементы',
      odd_index, ', ответ: ', sum(odd_index))
