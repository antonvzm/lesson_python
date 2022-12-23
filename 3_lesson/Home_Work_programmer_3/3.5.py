# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


number = 8
fibonachi_number = [1] * (2 * number + 1)
fibonachi_number[number] = 0
for i in range(number + 2, len(fibonachi_number)):
    fibonachi_number[i] = fibonachi_number[i - 1] + fibonachi_number[i - 2]
    fibonachi_number[len(fibonachi_number) - i -
                     1] = fibonachi_number[i] * (-1) ** (i + 1)
print('для k =', number, 'список будет выглядеть так:', fibonachi_number)
