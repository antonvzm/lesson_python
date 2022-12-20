# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

number = input('Введите число: ')
print(number, end = " -> ")
size = len(number)
number = float(number)
number = number * 10 ** (size - 2)

if number < 0:
    number = number * -1
summ = 0
while number > 0:
    lastnum = number % 10
    summ = int(summ + lastnum)
    number = number // 10
print(summ)