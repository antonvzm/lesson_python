# 2. Создать список, длины n, значения формируются по формуле 3k + 1,
# где k принимает значения от 1 до n включительно.

import os
clear = lambda: os.system('csl')
clear()

num_list = []
n = int(input("Введите число: "))
for i in range(1, n+1):
    num_list.append(3*i+1)
print(num_list)