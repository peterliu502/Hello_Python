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

# LEG规则
# Example 2.1
print('\nexample 2.1')
a_var = 'global value'


def outer():
    a_var = 'enclosed value'
    # a_var未申明Global变量
    # 且在outer()的scope(L)中有赋值
    # 因此赋值为'enclosed value'

    def inner():
        a_var = 'local value'
        # a_var未申明nonlocal变量
        # 且在inner()的scope(L)中有赋值
        # 因此赋值为'local value'
        print(a_var,'scope(L)')
        # a_var值取scope(L)中的赋值，和scope(E)或scope(G)无关
    print(a_var, 'scope(E)')
    inner()


print(a_var, 'scope(G)')
# global value scope(G)
outer()
# enclosed value scope(E)
# local value scope(L)
# scope(L)/scope(E)/scope(G)分别对同名变量赋值，三个变量独立取值

a_var = 'global value'


# Example 2.2
print('\nexample 2.2')
def outer():
    a_var = 'local value'
    print('outer before:', a_var)
    # outer before: local value

    def inner():
        nonlocal a_var
        # nonlocal关键词将此变量标记为outer()中的同名变量
        a_var = 'inner value'
        # 因为scope(L)和scope(E)中的a_var是同一个变量
        # 所以这里的再赋值会同时影响scope(L)和scope(E)中的a_var
        print('in inner():', a_var)
        # in inner(): inner value
    inner()
    print("outer after:", a_var)
    # outer after: inner value


outer()
print('global:', a_var)
# global: global value
# 因为outer()中的a_var没加global关键字，所以值的变化不会影响到scope(G)

# LEGB规则
# Example 3.1
print('\nexample 3.1')
a_var = 'global variable'


def len(in_var):
    print('called my len() function')
    l = 0
    for i in in_var:
        l += 1
    return l


def a_func(in_var):
    len_in_var = len(in_var)
    print('Input variable is of length', len_in_var)


a_func('Hello, World!')
