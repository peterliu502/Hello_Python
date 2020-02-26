#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
# 空两行


def my_abs(num, condition=0):
    if type(num) != int and type(num) != float:
        raise TypeError('bad operand type')
    else:
        if condition == 0:
            if num < 0:
                return -num
            else:
                return num
        elif condition == 1:
            return num, -num
        else:
            raise TypeError('bad operand type')


# 空两行
def quadratic(a, b, c):
    if (not isinstance(a, (int, float)))\
        or (not isinstance(b, (int, float)))\
            or (not isinstance(c, (int, float))):
        raise TypeError('bad operand type')
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        raise TypeError('方程{:f}x^2 + {:f}x + {:f} = 0 没有实数解'.format(a, b, c))
    result1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    result2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    if delta == 0:
        print('方程{:g}x^2 + {:g}x + {:g} = 0 有一个实数解{:g}'.format(a, b, c, result1))
        return result1, result2
    else:
        print('方程{:g}x^2 + {:g}x + {:g} = 0 有两个实数解{:g}、{:g}'.format(a, b, c, result1, result2))
        return result1, result2

