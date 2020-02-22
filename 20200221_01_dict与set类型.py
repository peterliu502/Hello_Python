#!/usr/bin/env python3
# -*- coding: utf-8 -*-

my_dict = {0: '语文', 1: '数学', 2: '英语', 3: '地理'}
print('dict对象基本操作：')
print(list(my_dict))  # 将dict对象输入list构造器可以输出一个以dict的键为元素的list
print(len(my_dict))  # 返回dict对象中项的个数
print(my_dict.keys())  # 返回以dict对象的键为元素的list对象
print(my_dict.values())  # 返回以dict对象的值为元素的list对象
print(my_dict.items())  # 返回以dict对象的键-值对元组为元素的list对象
my_dict1 = my_dict.copy()  # 创建dict对象的浅拷贝
my_dict.clear()  # 清除list中的所有元素
print(my_dict, my_dict1)
my_dict = my_dict.fromkeys(reversed(my_dict1), 1)
# 返回一个以dict的键为元素逆序排列的可迭代对象
print(my_dict)
my_dict = my_dict.fromkeys(iter(my_dict1), 1)
# iter(dict)返回一个以dict的键为元素的可迭代对象
# 类方法dict.fromkeys(seq[, value])返回一个以iterable的seq参数为键，value参数为值的dict对象
print(my_dict)
print(my_dict.get(0, '有'), my_dict.get(5, '没有'))  # dict中有key元素则返回key的值，没有则返回default，不会报错
print(my_dict.pop(0))
# 去除键为x的项，并返回该项的值
print(my_dict)
print(my_dict.popitem())
# 按照LIFO（先进后出）的顺序删去最后一项，并返回该键值对元组
print(my_dict)
my_dict.setdefault(3, 1)
my_dict.setdefault(1, 2)
# 如果存在键为x的对象则返回键的值，不存在则建立该键并赋值为default
print(my_dict)
my_dict.update([(3, 3), (4, 4), (5, 5)])  # 使用update()的参数来更新dict，已存在的键会更新，不存在的键会直接建立
print(my_dict)
print(0 in my_dict)
print(0 not in my_dict)

print('字典推导式：')
animal = ['beer', 'tiger', 'lion', 'monkey']
visitor = ['Peter', 'Loe', 'Alice', 'Jack']
number = [2, 4, 2, 10]
my_dict1 = {key: value for key, value in zip(animal, visitor)}
my_dict2 = {key: float(number - 2) for key, number in zip(animal, number) if number > 2}
print(my_dict1)
print(my_dict2)
