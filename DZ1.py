# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# day = int(input('Введите номер дня недели: '))
# if day > 7 or day < 1:
#     print('Повторите ввод')
# elif day == 6 or day == 7:
#     print("Это выходной!")
# else:
#     print("Это не выходной!")



# 1. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# 2. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# def inputNumbers(x):
#     xyz = ["X", "Y", "Z"]
#     a = []
#     for i in range(x):
#         a.append(input(f"Введите значение {xyz[i]}: "))
#     return a


# def checkPredicate(x):
#     left = not (x[0] or x[1] or x[2])
#     right = not x[0] and not x[1] and not x[2]
#     result = left == right
#     return result


# statement = inputNumbers(3)

# if checkPredicate(statement) == True:
#     print(f"Утверждение истинно")
# else:
#     print(f"Утверждение ложно")



# x = int(input('Введите x: '))
# y = int(input('Введите y: '))
# if x > 0 and y > 0:
#     print('1')
# if x < 0 and y > 0:
#     print('2')
# if x < 0 and y < 0:
#     print('3')
# if x > 0 and y < 0:
#     print('4')




# 1. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# n = int(input('Введите номер четверти: '))
# if n < 1 or n > 4:
#     print('Повторите ввод')
# elif n == 1:
#     print('x > 0 ; y > 0')
# elif n == 2:
#     print('x < 0 ; y > 0')
# elif n == 3:
#     print('x < 0 ; y < 0')
# elif n == 4:
#     print('x > 0 ; y < 0')


# print('Введите координаты точки А:')
# x_A = float(input('X: '))
# y_A = float(input('Y: '))
# print("введите координаты точки B:")
# x_B = float(input('X: '))
# y_B = float(input('Y: '))

# from math import sqrt
# print('Расстояние между точками A и B: ',round(sqrt((x_A - x_B)**2 + (y_A - y_B)**2), 2)) 