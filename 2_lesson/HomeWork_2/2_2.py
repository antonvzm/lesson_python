# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]

number = int(input("Введите число: "))
list_numbers = []
for i in range(1, number + 1):
    temp = 1
    for j in range(1, i + 1):
        temp = temp * j
    list_numbers.append(temp)
print(list_numbers)
