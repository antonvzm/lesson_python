# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# in
# 54

# out
# [2, 3, 3, 3]

print("Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.")

number = int(input('in\n'))
i = 2 
list_numbers = []
old = number
while i <= number:
    if number % i == 0:
        list_numbers.append(i)
        number //= i
        i = 2
    else:
        i += 1
print('out\n', list_numbers)