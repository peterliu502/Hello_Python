#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import copy

list1 = [1, '2', [3], [4, [5]], [6, [7, [8]]]]
print([id(list1), id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3][1]), id(list1[4][1][1])])
list2 = list1
print([id(list2), id(list2[0]), id(list2[1]), id(list2[2]), id(list2[3][1]), id(list2[4][1][1])])
# list2直接使用list1的引用来赋值，其自身、元素和更高维的元素都是list1的引用
list3 = copy.copy(list1)
print([id(list3), id(list3[0]), id(list3[1]), id(list3[2]), id(list3[3][1]), id(list3[4][1][1])])
# list3是对list1的浅拷贝，其自身使用新的内存地址，而其一维元素和更高维的元素仍是list1的引用
list4 = copy.deepcopy(list1)
print([id(list4), id(list4[0]), id(list4[1]), id(list4[2]), id(list4[3][1]), id(list4[4][1][1])])
# list4是对list1的深拷贝，其自身、一维元素和更高维的元素都采用新的内存地址，成为新的对象，不再是list1的引用

print([id(1), id('2')])
# int str等不可变类型对值相同的对象会共用内存地址以节省空间，所以拷贝等同与引用赋值
# 不可变类型对象也无法通过引用关系被改变，所以不生成新地址对于被引用对象也没有危险

list5 = [1, 2]
list5.append(list5)
print(list5, id(list5), id(list5[2]))
list6 = copy.deepcopy(list5)
print(list6, id(list6), id(list6[2]))
# 遇到类似m = [n, m]这种某级元素是其对象自身的引用时，list对象时不会进行彻底的递归运算
# 遇到m[1]这种已经处理的过的元素并不会分配新的内存地址，而是直接使用已经处理过的相同元素的引用
# 所以id(m) = id(m[1])

a = [3, 4]
m = [1, 2, a, [5, a]]
n = copy.deepcopy(m)
n[3][1][0] = -1
print(n)  # n = [1, 2, [-1, 4], [5, [-1, 4]]]
print(m)  # m = [1, 2, [3, 4], [5, [3, 4]]]
print(a)  # a = [3, 4]

# m中的a只是起到引用同一个list对象[3, 4]的作用，可以理解为a只是这个list对象的别名，他俩是绑定关系
# deepcopy()对各层元素都会建立副本，所以m[2]和m[3][1]指向的都是list对象[3, 4]的副本，而非本体
# 所以m[2]和m[3][1]和原本的list对象[3, 4]以及a都没有关系了
