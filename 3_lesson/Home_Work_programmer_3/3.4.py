# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


number = 45
binary_numbers = ''
print(number, '->', end=' ')
while number != 0:
    binary_numbers = str(number % 2) + binary_numbers
    number //= 2
print(binary_numbers)
