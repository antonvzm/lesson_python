# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

path_first = '5_lesson\\programer\\home_work\\text.txt'
data = open(path_first, 'r')

for line in data:
    print(line)
new_line = ''
line_temp = 0
i = 0
temp = 0
while line_temp < int(len(line)):
    if line[i] == line[line_temp]:
        line_temp += 1
        temp += 1
    else:
        new_line = new_line + f"{temp}{line[i]}"
        i = line_temp
        temp = 0
data.close()
print(new_line)