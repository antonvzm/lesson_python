# 35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

with open('5_lesson\\programer\\text.txt', 'w') as f:
    f.write('1 2 3 4 6 7 8 9 10')

path = '5_lesson\\programer\\text.txt'
data = open(path, 'r')
for line in data:
    print(line)
    li = list(map(int, line.split()))
data.close()
print(li)

for i in range(1,len(li)):
        if li[i] - 1 != li[i-1]:
            print (li[i] - 1)