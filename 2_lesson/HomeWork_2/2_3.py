# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6

# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

number = int(input("Введите количество чисел: "))
list_numbers = []
for i in range(1, number+1):
    round_number = round(((1+1/i)**i), 3)
    list_numbers.append(round_number)

sum = 0
for i in list_numbers:
    sum += i
print("in ", list_numbers)
print("out ", sum)