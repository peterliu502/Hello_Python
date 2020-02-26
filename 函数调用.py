#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from 函数定义与参数检查 import my_abs
from 函数定义与参数检查 import quadratic

print(my_abs(1, 1))  # int类型
print(my_abs(1.0, 1))  # float类型
# print(my_abs(''))  # str类型，异常

print(quadratic(1, 3, 1))
print(quadratic(1, 2, 1))
# print(quadratic(1, 3, []))  # 参数非数字，异常
# print(quadratic(1, 1, 1))  # 无实根，异常

print('作业：')
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')