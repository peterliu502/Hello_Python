#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('布尔值测试')
print("and（与运算）:")  # 两边同时为True，运算结果才为True；
print("True and True =", True and True)
print("1 < 2 and 3 < 4 =", 1 < 2 and 3 < 4)
print('True and False =', True and False)
print("1 < 2 and 3 > 4 =", 1 < 2 and 3 > 4)
print("False and False =", False and False)
print("1 > 2 and 3 > 4 =", 1 > 2 and 3 > 4)
print("or（或运算）:")  # 有一边为True，则运算结果为True；
print("True or True =", True or True)
print("1 < 2 or 3 < 4 =", 1 < 2 or 3 < 4)
print("True or False =", True or False)
print("1 < 2 or 3 > 4 =", 1 < 2 or 3 > 4)
print("False or False =", False or False)
print("1 > 2 or 3 > 4 =", 1 > 2 or 3 > 4)
print("not（非运算）:")  # True运算结果是False，False运算结果为True；
print("not True =", not True)
print("not 1 < 2 =", not 1 < 2)
print("not False =", not False)
print("not 1 > 2 =", not 1 > 2)
print('整数输出测试')
print(int('0x12', 16))
print(int('12', 16))
print(hex(12))
print('除法测试')
print(9 / 3)
print(9.0 / 3.0)
print(9 // 3)
print(9.0 // 3.0)
print(10 / 3)
print(10.0 / 3.0)
print(10 // 3)
print(10.0 // 3.0)
print('作业')
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n, f, s1, s2, s3, s4, sep='\n')  # sep='\n'，通过使用换行符间隔各个变量，从而实现分行输出变量的效果。
print(1, 2, 3, sep='')  # ，通过使用sep=''，从而实现","分割变量显示时不会出现空格。
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# objects -- 复数，表示可以一次输出多个对象。输出多个对象时，需要用 , 分隔。
# sep -- 用来间隔多个对象，默认值是一个空格。
# end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符串。
# file -- 要写入的文件对象。
# flush -- 输出是否被缓存通常决定于 file，但如果 flush 关键字参数为 True，流会被强制刷新。
