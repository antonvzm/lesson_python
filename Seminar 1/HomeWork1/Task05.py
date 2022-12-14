# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. 
# https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/

print('Введите координаты первой точки')
x_a, y_a= int(input()), int(input())
print('Введите координаты второй точки')
x_b, y_b = int(input()), int(input())
import math
range_coordinate = round(math.sqrt((x_b - x_a) ** 2 + (y_b - y_a) ** 2), 3)
print(range_coordinate)