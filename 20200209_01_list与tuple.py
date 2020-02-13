#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import copy

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
print('list4:', list4, end='\n\n')

# 通过 list * n 方法生成的多维list元素之间存在关联性
print('通过 list * n 方法生成的多维list元素之间存在关联性')
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
print('list1:', list1, end='\n\n')
# 执行list5[0].append(0)时就会同步再次对list1[0]插入一个0，此时list1为[[0, 0]]

# 可变类型元素操作对引用关系的影响
print('可变类型元素操作对引用关系的影响:')
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
print('list7:', list7, end='\n\n')
# list7[0] = [2]与上面两个操作不同，并非是对list7[0]所引用的list对象值进行修改
# 而是直接对list7[0]所引用的对象进行修改，改为引用新list对象[1]
# 使原来list7[0]对list6[0]的引用关系被替换了，list7[2] list7[4]还保留着对list6[0]的引用关系
# 所以list7[0]不再与list7[2]、list7[4]联动

# 通过列表推导式可以生成元素之间不关联的多级list
print('通过列表推导式可以生成元素之间不关联的多级list:')
list8 = [[] for i in range(3)]
for i in range(0, 3):
    list8[i].append(i)
print('list8:', list8, end='\n\n')

# 构造一个用于拼接的二维list，list元素作为拼接对象，方便使用for循环批量拼接
list_lens = 500  # 设定list的数量
# 选择list9构造方式，需要与方法3的for循环同步修改
list9 = [list(range(i + 1)) for i in range(list_lens)]  # 二级list的元素数由0到list_lens递增
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
print('计算四种拼接方法的运行时间:')
# +>>>append()>extend()>+=
start1 = time.process_time()
for i in range(list_lens):
    list9_1.extend(list9[i])
end1 = time.process_time()
# print('list9_1:', list9_1)  # 查看list9_1
print('Running time1: %.10f Seconds' % (end1 - start1))

start2 = time.process_time()
for i in range(list_lens):
    list9_2 += list9[i]
end2 = time.process_time()
# print('list9_2:', list9_2)  # 查看list9_2
print('Running time2: %.10f Seconds' % (end2 - start2))

start3 = time.process_time()
for i in range(list_lens):
    list9_3 = list9_3 + list9[i]
end3 = time.process_time()
# print('list9_3:', list9_3)  # 查看list9_3
print('Running time3: %.10f Seconds' % (end3 - start3))

start4 = time.process_time()
for i in range(list_lens):
    for j in range(i + 1):
        # 选择循环体执行代码，需要与list9的构造方式同步修改
        list9_4.append(list9[i][j])  # 二级list的元素数由0到list_lens递增
#    list9_4.append(list9[i][0])  # 所有二级list都只有一个元素i
end4 = time.process_time()
# print('list9_4:', list9_4)  # 查看list9_4
print('Running time4: %.10f Seconds' % (end4 - start4), end='\n\n')

# 检验四种方法生成的数组是否具有一致性
print('拼接方法产生的结果是否具有一致性')
print(list9_1 == list9_2)
print(list9_1 == list9_3)
print(list9_1 == list9_4)
print(list9_2 == list9_3)
print(list9_2 == list9_4)
print(list9_3 == list9_4, end='\n\n')

# 运行时间差异的关键：过程中是否生成了新的对象/内存地址
print('拼接方法是否生成了新对象：')
list10 = [1]
print(id(list10))

list10 = list10 + list10
# 将list10 + list10这个新list对象赋值给list10，赋值对象改变，list10的内存地址也改变了
print(id(list10))

list10 += list10
# +=是调用了__iadd__（）方法，并没有生成新的对象，也就不会分配新的内存地址
print(id(list10))

list10.extend(list10)
# list.extend()方法只是对list对象的内部元素进行操作，不涉及对list的重新赋值
# 对于可变类型对象来说只有将整个对象替换掉才算重新赋值，只是对象内部操作并不算赋值
print(id(list10))

list10.append(list10[0])
# list.append()方法只是对list对象的内部元素进行操作，不涉及对list的重新赋值
# 对于可变类型对象来说只有将整个对象替换掉才算重新赋值，只是对象内部操作并不算赋值
print(id(list10), end='\n\n')

print('list运算:')
print('in 与 not in:')
print([1] in list8, [] in list8)  # 使用in来确认list中是否有某元素
print([1] not in list8, [] not in list8)  # 使用not in来确认list中是否没有某元素
print('min(list) 与 max(list):')
print(max([1000, True, 6]))  # 取最大值的元素，True=1，False=0
print(min([1000, True, 6]))  # 取最大值的元素，True=1，False=0

list11 = [[j] for i in range(1000) for j in range(i + 1)]  # 构造测试函数
print(list11[0:len(list11):2].count([0]))  # 统计元素出现次数
print(list11[0:len(list11):2].index([1]))  # 查找特定元素首次出现的序数
print(list11[0:len(list11):2].index([1], len(list11) // 200))  # 加入范围限制查找特定元素首次出现的序数
print(list11[int(list11[0:len(list11):2].index([1], len(list11) // 200) * 2)], end='\n\n')  # 验证返回的序数项是否是指定的元素

# list = list * n等价于list *= n
print('list = list * n与list *= n等价测试:')
list12_1 = [1]
list12_2 = [1]
list12_2 *= 5
print(list12_1 * 5 == list12_2, end='\n\n')  # True

# copy.copy(list) = list[:]
print('copy.copy()/copy.deepcopy()/list.copy()/list[:]/list()对比:')
list13 = [[1], [2]]
list13_1 = copy.copy(list13)
list13_1s = copy.copy(list13[0:1])
list13_2 = copy.deepcopy(list13)
list13_2s = copy.deepcopy(list13[0:1])
list13_3 = list13[:]
list13_3s = list13[0:1]
list13_4 = list13.copy()
list13_4s = list13[0:1].copy()
list13_5 = list(list13)
list13_5s = list(list13[0:1])
# copy.copy() = list.copy() = list[:] = list()
print('copy.copy():', list13_1 is list13, list13_1[0] is list13[0])  # False True
print('copy.deepcopy():', list13_2 is list13, list13_2[0] is list13[0])  # False False
print('list.copy():', list13_3 is list13, list13_3[0] is list13[0])  # False True
print('list[:]:', list13_4 is list13, list13_4[0] is list13[0])  # False True
print('list():', list13_5 is list13, list13_5[0] is list13[0])  # False True
# copy.copy()/copy.deepcopy()/list.copy()/list[:]/list()都支持切片操作
print('copy.copy():', list13_1s, list13_1s[0] is list13[0])  # True
print('copy.deepcopy():', list13_2s, list13_2s[0] is list13[0])  # False
print('list.copy():', list13_3s, list13_3s[0] is list13[0])  # True
print('list[:]:', list13_4s, list13_4s[0] is list13[0])  # True
print('list():', list13_5s, list13_5s[0] is list13[0], end='\n\n')  # True

print('原始list(list7):', list7, sep='\n')
list7_1 = copy.deepcopy(list7)
list7_2 = copy.deepcopy(list7)
list7_3 = copy.deepcopy(list7)
list7_4 = copy.deepcopy(list7)
list7_5 = copy.deepcopy(list7)
list7_6 = copy.deepcopy(list7)
list7_7 = copy.deepcopy(list7)
list7_8 = copy.deepcopy(list7)
list7_9 = copy.deepcopy(list7)

list7_1[2:4] = list1[0:1]
# s[j:k] = t[m:n]中len(s[i:j])不必与len(t[m:n])相同
print('s[j:k] = t[m:n]:', list7_1, sep='\n', end='\n\n')

list7_2[3:4] = []
del list7_3[3:4]
# s[m:m] = []等价于del s[m:n]
print('两种切片删除方法是否相等:', list7_2 == list7_3, list7_3 == list7_8,
      'list7:', list7, 'list7_2:', list7_2, 'list7_3:', list7_3, 'list7_8:',
      list7_8, sep='\n', end='\n\n')  # True

list7_4[None:None:2] = [[1, 2]] * 3
# s[i:j:k] = t[m:n:l]中len(s[i:j:k])必须与len(t[m:n:l])相同
print('s[i:j:k] = t[m:n:l]:', list7_4, sep='\n')

del list7_5[None:None:2]
# 对于有步长的切片不能使用s[i:j:k] = []这种语法，只能使用del s[i:j:k]
print('del s[i:j:k]:', list7_5, sep='\n', end='\n\n')

# list.clear()
print('list.clear():')
print('list7_8:', list7_8)
list7_8[:].clear()
# list.clear不支持切片，建议改用del list[i:j]或list[i:j] = []
print('list7_8[:].clear():', list7_8)
list7_8 = [list7_8[0:1].clear()]
# list.clear()方法没有返回值
print('list7_8 = [list7_8[0:1].clear()]:', list7_8)
list7_8.clear()
# list.clear()等价于del list
print('list7_8.clear():', list7_8, end='\n\n')

# list.insert()
print('list.insert():')
list7_9.insert(1, [1])
print(list7_9, end='\n\n')

# list.pop(i)
print('list.pop():')
list7_9.pop(1)
# 删除i位置上的元素
print(list7_9)
list7_9.pop()
# 参数缺省则删除最后一个元素
print(list7_9)
list7_9[1:3].pop()
# list.pop(i)不支持切片，建议改用del list[i:j]或list[i:j] = []
print(list7_9, end='\n\n')

# list.remove(x)
print('list.remove(x):')
list7_9.remove([1])
print(list7_9)
# 删除list对象中第一个等于x的项目
list7_9[2:len(list7_9)].remove(1)
print(list7_9, end='\n\n')
# list.remove()不支持切片

# list.reverse()
print('list.reverse():')
list7_9.reverse()
# 在原list中将列表中的元素逆序
print(list7_9)
list7_9[0:3].reverse()
# list.reverse()不支持切片
print(list7_9, end='\n\n')

# list.sort()
# list().sort()
print('list.sort()&list().sort():')
list7_10 = [[1, 2], [1, 3], [2, 4], [2, 3, 4], [1.5]]
list7_10.sort()
print(list7_10)
list7_10 = ['123', 'abc', '1中文', 'abc123']
list7_10.sort()
print(list7_10)
# list.sort()默认对list元素不做处理，以升序排列
list7_10.sort(reverse=True)
print(list7_10)
# reverse参数默认为False，即以升序排列，手动改为True即以降序排列
list7_11 = [5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 8, 9]
list7_10 = [5, 5, 5, 6, 6, 6, 7, 8, 8, 8, 8, 9]
list7_10.sort(key=list7_11.count)
print(list7_10)
# key参数可以指定list元素的处理方式，对处理结果再进行排序
list7_10.sort(key=copy.deepcopy(list7_10).count)
print(list7_10)
# list对象自身不可以作key参数，但可以用深浅拷贝来做参数
# key参数可以接收一个函数，该函数必须可以接收一个参数并返回一个值
# list对象中的元素会依次输入该函数，并将返回值作为排序对象
# 在list7_10.sort(key=copy.deepcopy(list7_10).count)中
# list7_10[0]和list7_10[5]的返回值都是1，所以根据处理的先后顺序
# 将先处理的9排在7前面
