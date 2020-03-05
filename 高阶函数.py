#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce

# 变量引用函数
function_abs = abs  # 将函数赋值给变量，变量便引用函数了
print(function_abs(-1))  # 变量现在可以使用函数的功能了

# 函数名实质上也等同于指向函数的一个变量名
# 所以函数名也是可以被赋予其他值的（强烈不建议这么做），之后便不再能用该函数名调用函数了
# abs = 10  # 将abs函数名赋值为10
# 想在所有模块中都让某函数的指向改变，必须在使用import统一修改，格式为import 函数所在模块; 函数所在模块.函数 = 自定义值


# 接受函数为参数的函数，即为高阶函数
def add(num1, num2, my_func):
    return my_func(num1) + my_func(num2)


def tuple_zip(*iter_object):
    return tuple(zip(*iter_object))


print(add(-1, -1, function_abs))

# map()函数
print(list(map(abs, [-1, -10, 0, -11, -2, -5, 4])))  # func直接收一个参数的情况
print(list(map(add, [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [int, oct, bin, hex])))  # func若可以接多个参数则可以跟多个iterable


# reduce()函数
print(list(reduce(zip, [[1, 2, 3, 4], ['01', '02', '03', '04'],
                        ['one', 'two', 'three', 'four'], ['一', '二', '三', '四']])))
# 虽然zip()函数支持输入多个参数，但是reduce()只支持依次两两参数操作
print(list(reduce(zip, [[1, 2, 3, 4], ['01', '02', '03', '04'],
                        ['one', 'two', 'three', 'four']], ['一', '二', '三', '四'])))
# ['一', '二', '三', '四']做initialize参数，即reduce()接收的第一个默认参数


# 作业：首字母大写
def normalize(name):
    my_str = []
    if ord(name[0]) > 90:
        my_str[0:0] = [chr(ord(name[0]) - 32)]
    else:
        my_str[0:0] = [name[0]]
    my_str += [chr(ord(str_elm) + 32) if ord(str_elm) <= 90 else str_elm for str_elm in name[1::]]
    return ''.join(my_str)


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 作业：数列求积
def prod(L):
    def my_times(num_1, num_2):
        return num_1 * num_2
    return reduce(my_times, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 作业：字符串转浮点数
def str2float(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def char2num(my_str):
        return digits[my_str]

    def s_integer_char2num(num_1, num_2):
        return num_1 * 10 + num_2

    def s_decimal_char2num(num_1, num_2):
        return num_1 / 10 + num_2

    if '.' in s:
        point_index = s.index('.')
        return float(reduce(s_integer_char2num, map(char2num, s[0:point_index]))) + \
            float(reduce(s_decimal_char2num, map(char2num, s[len(s):point_index:-1]))) / 10
    else:
        return float(reduce(s_integer_char2num, map(char2num, s)))


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')