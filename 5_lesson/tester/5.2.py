# 2. Создайте список, в который попадают числа,
# описывающие возрастающую последовательность.
# Порядок элементов менять нельзя.

from random import choices

def create_list(num):
    return choices(range(1, num*2), k=num)

def seq(li):
    temp_li = []
    for i in range(len(li)):
        num = li[i]
        out_list = [num]
        for j in range(i+1, len(li)):
            if li[j] > num:
                num = li[j]
                out_list.append(num)
        temp_li.append(out_list)
    return temp_li

li = create_list(5)
print(li)
print(seq(li))