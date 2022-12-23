# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

number = int(input('in\n'))
binary_numbers = ''
while number != 0:
    binary_numbers = str(number % 2) + binary_numbers
    number //= 2
print('out\n',binary_numbers)