# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

from decimal import Decimal, ROUND_HALF_EVEN

number = Decimal(input("Введите число: "))
number_decimal = input("Введите требуемую точность: ")

print(number.quantize(Decimal(number_decimal), ROUND_HALF_EVEN))