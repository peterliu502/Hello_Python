#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 匿名函数（lambda函数）
# 函数赋值
my_lambda = map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(my_lambda))  # [1, 4, 9, 16, 25, 36, 49, 64, 81]


# 等价函数对比
def my_sqr(x):
    return x * x


my_func = map(my_sqr, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(my_func))  # [1, 4, 9, 16, 25, 36, 49, 64, 81]


# 返回lambda函数
def rtn_lmd(x):
    return lambda: x * 2
    # 注意这里lambda没有定义形参，因为可以直接用rtn_lmd的形参
    # 如果lambda定义了形参的话,对rtn_lmd和lambda的调用都要传参


my_func2 = rtn_lmd
print(my_func2(10)())


# 返回lambda函数的值
def rtn_lmd1(x):
    return (lambda: x * 2)()  # 返回lambda函数的返回值


print(rtn_lmd(2))  # 返回lambda函数
print(rtn_lmd1(2))  # 返回lambda函数值


# 作业
L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)
