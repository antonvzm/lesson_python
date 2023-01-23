# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

import random

li_num = [random.randint(0, 10) for i in range(10)]
print(li_num)
li_new = [li_num[i+1] for i in range(0, 9) if li_num[i] < li_num[i+1]]
print(li_new)