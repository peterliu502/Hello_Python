#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 必选参数（位置或关键词参数）:是函数形参的默认形式，可以通过位置匹配或关键词匹配两种方式赋值
def student(name, id_num):
    return {'name': name, 'id': '{:04d}'.format(id_num)}


# 位置参数：作为位置函数的实参是通过位置次序与定义函数时的位置形参进行匹配
print(student('Peter', 1))  # 实参'Peter'和1通过位置关系分别与形参name和id_num进行匹配
# 关键词函数：作为关键词函数的实参通过关键词与同名关键词的形参进行匹配，无需遵循位置匹配规则
print(student(id_num=1, name='Peter'))  # 实参通过关键词参数的方式赋值，不需要遵循按位置对应的规则
# 必选参数部分如果实参混用位置参数与关键词参数，必须先写位置实参，且后面的关键词实参对应的形参不可以与位置实参冲突
print(student('Peter', id_num=1))


# 默认参数：在调用时没有对应实参进行赋值时会自动赋为默认值的参数，可降低函数的调用难度
# 默认参数不可以赋为可变类型对象
def worker(name, region='UK'):
    return {'name': name, 'region': region}


print(worker('John'))  # 未指定id_num则取默认值'UK'
print(worker('Ross', 'US'))  # 指定了默认参数的值则以指定值为准


# 可变参数：分为可变位置参数与可变关键词参数
# 可变位置参数:可以接收任意数量的实参，所有参数会依次打包成一个元组
def employer(name, department, *projects):
    return {'name': name, 'department': department, 'projects': projects}


print(employer('John', 'BD', 'BD-012', 'BD-020', 'DM-003'))  # 第三个参数开始会全部打包为一个tuple对象
print(employer('Amy', 'RD', *['BD-020', 'RD-002', 'PDD-012']))  # 通过解包序列类型对象的方式给可变参数赋值


# 可变关键词参数：可以接收任意数量的关键词形式的实参（key=value），所有参数会依次打包成一个字典
def add_elm(**my_dict):
    my_dict.popitem()
    return my_dict


print(add_elm(elm1=1, elm2=2, elm3=3, elm4=4, elm5=5))  # 通过关键词的方式给关键词参数赋值，全部打包为一个字典对象
my_dict_test = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
print(add_elm(**my_dict_test))  # 通过解包dict对象的方式给关键词参数赋值，传递的是深拷贝，函数内部修改并不会影响dict对象
print(my_dict_test)


# 限定参数：限制了形参赋值方式的参数，分为仅限位置参数与仅限关键词参数
# 仅限位置参数：对应实参只能通过位置关系传参，通过插入一个/分隔符来将符号之前的形参设为仅限位置参数
def my_class(teacher, stu_num, /, rank):
    return teacher, stu_num, rank


print(my_class('jack', 40, rank=1))  # teacher和stu_num都只能通过位置传参，而rank则可以通过位置和关键词两种方式传参


# 仅限关键词参数：对应实参只能通过关键词传参，通过插入一个*分隔符来将符号之前的形参设为仅限位置参数
def essay(topic, writer, *, word_num):
    return topic, writer, word_num


print(essay('data', 'Jacky', word_num=2000))  # word_num被限定了只能用关键词传参


# 如果仅限关键词参数前面有可变位置参数，则不需要在前面加*分隔符
# 因为如果不强制使用关键词会被识别为可变位置参数的一部分，导致异常
def book(name, editor, *writer, word_num):
    return name, editor, writer, word_num


print(book('data science', 'Joe', 'Lee', 'Tom', 'Cindy', word_num=200000))


# 混合使用：以上几种形参类型均可混合使用，但定义时必须必须遵循以下顺序：
# 仅限位置参数-必选参数-默认参数-可变位置参数-仅限关键词参数-可变关键词参数
# 其中前四种参数：仅限位置参数-必选参数-默认参数-可变位置参数都可以使用位置参数
# 而后两种：仅限关键词参数-可变关键词参数必须使用关键词参数
# 所以任何函数被调用时，无论函数是如何定义的都可以写成func(*arg, **kw)形式
# *arg实参和**kw实参分别给前四种形参和后两种形参赋值
# 虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差
def team(name, /, leader, ldr_tel, teacher='Amy', *mb_list, mb_num, **division):
    # mb_num前面有个*mb_list，所以不用加*分隔符
    # 默认参数后接可变位置参数，其默认值是无效的，因为若teacher省略则会把*mb_list的第一个元素识别为teacher
    # 必选参数如果后接可变位置参数，则不可以用关键词传参，因为违反了关键词参数必须在位置参数的后面的规则
    print(ldr_tel)
    print(teacher)
    print(mb_list)
    return name, leader, ldr_tel, teacher, mb_list, mb_num, division


print(team('data master', 'Peter', '13600000000', 'Tom',
           *['Patty', 'Carol', 'Jay', 'Fin', 'Steve'], mb_num=5,
           **{'Coco': 'driver', 'Patty': 'cook', 'Carol': 'guard',
              'Jay': 'Dr', 'Fin': 'engineer', 'Steve': 'engineer'}))


def product(*args):
    if not args:
        raise TypeError('bad operand number')
    s = 1
    for elm in args:
        if (type(elm) != int) & (type(elm) != float):
            raise TypeError('bad operand type')
        else:
            s *= elm
    return s


print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
