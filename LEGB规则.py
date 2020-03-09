#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# LG规则
# Example 1.1
# scope(L)找不到就翻上层去scope(G)找
print('example 1.1')
a_var = 'global variable'


def a_func():
    print(a_var, '[ a_var inside a_func() ]')


a_func()
print(a_var, '[ a_var outside a_func() ]')
# global value [ a_var inside a_func() ]
# global value [ a_var outside a_func() ]

# Example 1.2
print('\nexample 1.2')
a_var = 'global value'


def a_func():
    a_var = 'local value'
    print(a_var, '[ a_var inside a_func() ]')


a_func()
# local value [ a_var inside a_func() ]
print(a_var, '[ a_var outside a_func() ]')
# global value [ a_var outside a_func() ]

# Example 1.3
print('\nexample 1.3')
a_var = 'global value'


def a_func():
    global a_var  # 通过global关键字将a_var标识为scope(G)的那个同名a_var变量
    a_var = 'local value'
    print(a_var, '[ a_var inside a_func() ]')


print(a_var, '[ a_var outside a_func() ]')
# global value [ a_var outside a_func() ]
a_func()  # 注意a_var的值是在调用过a_func之后才改变的
# local value [ a_var inside a_func() ]
print(a_var, '[ a_var outside a_func() ]')
# local value [ a_var outside a_func() ]

