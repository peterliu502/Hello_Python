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

print('集合类型：')
print('构造器函数:')
my_set = set([1, 2, 3, 4])  # set()构造器函数
my_set1 = {1, 2, 3, 4}
my_frozenset = frozenset([1, 2, 3, 4])  # frozenset()构造器函数
print(my_frozenset, '\'s type is', type(my_frozenset))
print(my_set, '\'s type is', type(my_set))

print('集合类型通用操作:')
my_set.isdisjoint(my_set1)  # 验证A集合和B可迭代对象是否没有交集
print('是否无交集:', my_set)
my_set.issubset(my_set1)  # 验证A集合是否是B可迭代对象的子集，等价于set1 <= set2
print('子集:', my_set)
print('子集:', my_set <= my_set1)  # 验证A集合是否是B集合的子集，等价于set1.issubset(set2)
print('真子集:', my_set < my_set1)  # 验证A集合是否是B集合的真子集，即set <= other and set != other
my_set.issuperset(my_set1)  # 验证A集合是否是B可迭代对象的超集，等价于set1 >= set2
print('超集:', my_set)
print('超集:', my_set >= my_set1)  # 验证A集合是否是B集合的超集，等价于set1.issuperset(set2)
print('真超集:', my_set > my_set1)  # 验证A集合是否是B集合的真超集，即set >= other and set != other
my_set1 = my_set1.union([4, 5], [5, 6])  # 返回集合对象A和可迭代对象B1-Bn的并集
print('并集:', my_set1)
my_set = my_set | my_frozenset | {4, 5} | {5, 6}  # 返回A和B1-Bn的并集,只能set与frozenset之间运算
my_frozenset1 = my_frozenset | my_set
print('并集:my_frozenset | my_set', my_frozenset1, type(my_frozenset1))  # set和frozenset取并集的结果是取第一个对象的类型
print('并集:my_set | my_frozenset', my_set, type(my_set))  # set和frozenset取并集的结果是取第一个对象的类型
my_set = my_set.intersection([2, 3, 4, 5], (1, 2, 3, 4))  # 返回集合对象A和可迭代对象B1-Bn的交集
print('交集:', my_set)
my_set1 = my_set1 & {2, 3, 4, 5} & {1, 2, 3, 4}  # 返回集合对象A和B1-Bn的交集,只能set与frozenset之间运算
print('交集:', my_set1, type(my_set))
my_set = my_set.difference([2], (4, ))  # 返回集合对象A与可迭代对象B1-Bn的差集
print('差集:', my_set)
my_set1 = my_set1 - {2} - {4}  # 返回集合对象A与B1-Bn的差集
print('差集:', my_set1)
my_set = my_set.symmetric_difference([1, 2, 3, 4, 5])  # 集合对象A和可迭代对象B的并集减去交集
print('对称差集:', my_set)
my_set1 = my_set1 ^ {1, 2, 3, 4, 5}  # 集合对象A和B的并集减去交集
print('对称差集:', my_set)
my_set2 = my_set1.copy()  # 创建浅拷贝
print('id(my_set1):', id(my_set1), 'id(my_set2):', id(my_set2))

print('set类型通用操作:')
my_set2 = {1, 2, 3, 4}
my_set3 = {1, 2, 3, 4}
my_set2.update([4, 5], [5, 6])  # set类型版的set.union()，可直接对原对象进行修改
print('并集:', my_set2)
my_set3 |= my_frozenset | {4, 5} | {5, 6}  # set类型版的set1 | set2 | …… | setn，可直接对原对象进行修改
print('并集:', my_set3, type(my_set3))
my_set2.intersection_update([2, 3, 4, 5], (1, 2, 3, 4))  # set类型版的set.intersection()，可直接对原对象进行修改
print('交集:', my_set2)
my_set3 &= {2, 3, 4, 5} & {1, 2, 3, 4}  # set类型版的set1 & set2 & …… & setn，可直接对原对象进行修改
print('交集:', my_set3, type(my_set3))
my_set2.difference_update([2], (4, ))   # set类型版的set.difference()，可直接对原对象进行修改
print('差集:', my_set2)
my_set3 -= {2} - {4}  # set类型版的set1 - set2 - …… - setn，可直接对原对象进行修改
print('差集:', my_set3)
my_set2.symmetric_difference_update([1, 2, 3, 4, 5])   # set类型版的set.symmetric_difference()，可直接对原对象进行修改
print('对称差集:', my_set2)
my_set2 ^= {1, 2, 3, 4, 5}  # set类型版的set1 ^ set2，可直接对原对象进行修改
print('对称差集:', my_set2)
my_set2.add(4)  # 在set对象的末尾插入x元素
print('插入元素:', my_set2)
my_set2.remove(3)  # set对象中存在x元素则消除，不存在则报错
print('删除元素(remove):', my_set2)
elm = {1}
my_set2.discard(elm)  # 相当于不会报错版的set.remove()
print('删除元素(discard):', my_set2)
my_set3.pop()  # 消除set对象中的一个元素（打印出来的最后一个元素）
print('删除元素(pop):', my_set3)
my_set3.clear()  # 清除set对象中所有的元素
