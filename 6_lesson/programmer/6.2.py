# 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

# *Пример:*

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

li = [1, 2, 3, 5, 1, 5, 3, 10]
print(li)
my_set = list(set(li))
print(my_set)