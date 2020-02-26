#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# if语句作业
height = float(input('请输入身高(m):'))  # 输入身高（m）
weight = float(input('请输入体重(kg):'))  # 输入体重（kg）
BMI_index = weight / (height**2)  # 计算BMI指数
print('BMI_index:', BMI_index)  # 打印BMI指数
if BMI_index < 18.5:
    print('过轻')
elif BMI_index < 25:
    print('正常')
elif BMI_index < 28:
    print('超重')
elif BMI_index < 32:
    print('肥胖')
else:
    print('严重肥胖')

# for in/continue/break
print()
mylist1 = [-1, -2, -3, -4, -5, 5.5, 6, 7, 8, 9, 0]
max_elm = None
for elm in mylist1:
    if type(elm) != int:
        print('type wrong!')
        break
    elif elm % 2 == 0:
        if max_elm is None:
            max_elm = elm
        else:
            if elm > max_elm:
                max_elm = elm
            else:
                pass
    else:
        continue
print('max_elm:', max_elm)
print()

# while
my_sum = 0
i = 1
while my_sum < 1000:
    my_sum += i
    i += 1
print('sum:', my_sum)
print('i:', i)

# 循环语句作业
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello, {:s}!'.format(name))
