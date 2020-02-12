#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

# list2 = list1 * n，意味着list2中的元素都是对list1中元素的引用
# 由于对list2中引用的可变类型元素(如list与dict)的值进行修改不会改变该元素的内存地址
# 所以会导致同步修改list1中的被引用元素以及list2中其他引用同一对象的元素
# 这个问题多见于使用list * n的方法来生成多维list时
print('list * n:')
list1 = [[]]
list2 = [[], [], []]
list3 = [[]] * 3
list4 = list1 * 3
list5 = list1 * 3
print('list1:', list1)
print('list2:', list2)
print('list3:', list3)
print('list4:', list4)

# 通过 list * n 方法生成的多维list元素之间存在关联性
list2[0].append(0)
print('list2:', list2)
# list2[0] list2[1] list[2]是三个独立的对象，
# 单独对某一元素赋值其他元素不受影响
list3[0].append(0)
print('list3:', list3)
# list3[0] list3[1] list3[2]都是对[[]]的引用，都属于可变类型list类型对象
# 所以list3[0].append(0)会同步对[[]]插入元素
list4[0].append(0)
print('list4:', list4)
# list4[0] list4[1] list4[2]都是对list1[0]的引用
# 所以list4[0].append(0)会同步对list1[0]插入元素
print('list1:', list1)
# 执行list4[0].append(0)时就会同步对list1[0]插入一个0，此时list1为[[0]]
list5[0].append(0)
print('list5:', list5)
# list5[0] list5[1] list5[2]都是对list1[0]的引用
# 所以list5[0].append(0)会同步对list1[0]插入元素
print('list1:', list1)
# 执行list5[0].append(0)时就会同步再次对list1[0]插入一个0，此时list1为[[0, 0]]

# 可变类型元素操作对引用关系的影响
list6 = [[], 1]
list7 = list6 * 3
list7[0].append(2)
print('list7:', list7)
# list7[0] list7[2] list7[4]都是引用list6[0]，这4个list元素保持关联
# list7[0].append(2)会同步在list7[2] list7[4]和list6[0]中插值
list7[0][0] = 1
print('list7:', list7)
# list7[0] list7[2] list7[4]都是引用list6[0]，这4个list元素保持关联
# list7[0][0] = 1会同步对list7[2] list7[4]和list6[0]的首位元素赋值为1
list7[0] = [2]
print('list7:', list7)
# list7[0] = [2]与上面两个操作不同，并非是对list7[0]所引用的list对象值进行修改
# 而是直接对list7[0]所引用的对象进行修改，改为引用新list对象[1]
# 使原来list7[0]对list6[0]的引用关系被替换了，list7[2] list7[4]还保留着对list6[0]的引用关系
# 所以list7[0]不再与list7[2]、list7[4]联动

# 通过列表推导式可以生成元素之间不关联的多级list
list8 = [[] for i in range(3)]
for i in range(0, 3):
    list8[i].append(i)
print('list8:', list8)

# 构造一个用于拼接的二维list，list元素作为拼接对象，方便使用for循环批量拼接
list_lens = 500  # 设定list的数量
# 选择list9构造方式，需要与方法3的for循环同步修改
list9 = [list(range(i+1)) for i in range(list_lens)]  # 二级list的元素数由0到list_lens递增
# list9 = [[i] for i in range(list_lens)]  # 所有二级list都只有一个元素i

# 构造用于接收拼接结果的空list，由于list是可变类型对象
# 不要使用list9_1 = list9_2 = list9_3 = list9_4 = []
# 否则前面变量的接收完拼接结果后会直接传给后面的变量
# 使得后面方法测试开始时的接收list初始值不是[]
list9_1 = []
list9_2 = []
list9_3 = []
list9_4 = []
# print('list9:', list9)  # 查看list9

# 计算四种拼接方法的运行时间
# +>>>append()>extend()>+=
start1 = time.process_time()
for i in range(list_lens):
    list9_1.extend(list9[i])
end1 = time.process_time()
# print('list9_1:', list9_1)  # 查看list9_1
print('Running time1: %.10f Seconds' % (end1-start1))

start2 = time.process_time()
for i in range(list_lens):
    list9_2 += list9[i]
end2 = time.process_time()
# print('list9_2:', list9_2)  # 查看list9_2
print('Running time2: %.10f Seconds' % (end2-start2))

start3 = time.process_time()
for i in range(list_lens):
    list9_3 = list9_3 + list9[i]
end3 = time.process_time()
# print('list9_3:', list9_3)  # 查看list9_3
print('Running time3: %.10f Seconds' % (end3-start3))

start4 = time.process_time()
for i in range(list_lens):
    for j in range(i + 1):
        # 选择循环体执行代码，需要与list9的构造方式同步修改
        list9_4.append(list9[i][j])  # 二级list的元素数由0到list_lens递增
#    list9_4.append(list9[i][0])  # 所有二级list都只有一个元素i
end4 = time.process_time()
# print('list9_4:', list9_4)  # 查看list9_4
print('Running time4: %.10f Seconds' % (end4-start4))

# 检验四种方法生成的数组是否具有一致性
print(list9_1 == list9_2)
print(list9_1 == list9_3)
print(list9_1 == list9_4)
print(list9_2 == list9_3)
print(list9_2 == list9_4)
print(list9_3 == list9_4)

# 运行时间差异的关键：过程中是否生成了新的内存地址
list10 = [1]
print(id(list10))
list10 = list10 + list10
print(id(list10))
list10 += list10
print(id(list10))
list10.extend(list10)
print(id(list10))
list10.append(list10[0])
print(id(list10))

print([1] in list8, [] in list8)  # 使用in来确认list中是否有某元素
print([1] not in list8, [] not in list8)  # 使用not in来确认list中是否没有某元素
print(max([1000, True, 6]))  # 取最大值的元素，True=1，False=0
print(min([1000, True, 6]))  # 取最大值的元素，True=1，False=0

list11 = [[j]for i in range(1000) for j in range(i+1)]  # 构造测试函数
print(list11[0:len(list11):2].count([0]))  # 统计元素出现次数
print(list11[0:len(list11):2].index([1]))  # 查找特定元素首次出现的序数
print(list11[0:len(list11):2].index([1], len(list11)//200))  # 加入范围限制查找特定元素首次出现的序数
print(list11[int(list11[0:len(list11):2].index([1], len(list11)//200) * 2)])  # 验证返回的序数项是否是指定的元素

# list = list * n等价于list *= n
list12_1 = [1]
list12_2 = [1]
list12_2 *= 5
print(list12_1 * 5 == list12_2)

# 