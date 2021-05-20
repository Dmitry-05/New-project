# 3 Написать функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью кортежа): периметр квадрата,
# площадь квадрата и диагональ квадрата.

import math


def square(sidelen):
    return sidelen*2, sidelen**2, sidelen*math.sqrt(2)


print(square(4))
