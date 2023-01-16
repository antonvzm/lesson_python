# 1. Создайте список из N натуральных чисел(0 до N),
# упорядоченных по возрастанию. Среди чисел не хватает
# одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.

from random import choices

def any_list(num):
    li = list(range(num+1))
    li.remove(choices(li))
    return li

def find(li):
    for i in range(len(li)):
        if li[i] - 1 != li[i-1]:
            return li[i] - 1
    return -1

data = any_list(int(input("Введите число: ")))
print(data)
number = find(data)
print(number)
