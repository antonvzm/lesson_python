# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# ниже изначальный вариант
# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# num3 = int(input('Введите третье число: '))
# num4 = int(input('Введите четвертое число: '))
# num5 = int(input('Введите пятое число: '))

# my_max = num1

# if num2 > my_max:
#     my_max = num2
# if num3 > my_max:
#     my_max = num3
# if num4 > my_max:
#     my_max = num4
# if num5 > my_max:
#     my_max = num5
# print (f'{num1}, {num2}, {num3}, {num4}, {num5} -> {my_max}')

def el_li(num):
    return True if num == max_num else False
li_num = list(map(int, input("Введите 5 цифр через пробел: ").split()))
max_num = max(li_num)
print(f'{li_num} => ',int(list(filter(el_li,[i for i in li_num]))[0]))

