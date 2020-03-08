#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 返回函数
def return_func(*args):
    def return_func1():
        def my_list():
            return list(args)
        return my_list
    return return_func1


result = return_func(1, 2, 3, 4)
result = return_func(1, 2, 3, 4, result)
print(result)
print(result())
print(result()())
print(result()()[4]())
print(result()()[4]()())


# 闭包结构结构陷阱：赋值时(a = f)不执行，调用时(a())才执行
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


# 闭包结构中使用循环变量的方法
def count_ex():
    fs = []

    def i_accept(j):  # 接收循环变量，通过传参将形参指向当前i变量指向的对象，之后就和i不再有关联了
        def f():
            return j * j  # 进行数据处理，引用的是i_accept的局部变量j，而非count_ex的局部变量i
        return f  # 返回闭包结构
    for i in range(1, 4):
        fs.append(i_accept(i))
    return fs


f1, f2, f3 = count_ex()
print(f1(), f2(), f3())


# 作业：计数器
# 生成器写法
def createCounter1():
    def my_iterator():
        i = 0
        while True:
            i = i + 1
            print(
                'my_iterator():'
                '\nglobals():', globals(),
                '\nlocals()', locals())
            yield i
            print('my_iterator():'
                  '\nglobals():', globals(),
                  '\nlocals()', locals())

    generator = my_iterator()  # 必须用一个变量接收下来，不然调用完会回收内存，下次调用会从头开始迭代

    def counter():
        print('counter():'
              '\nglobals():', globals(),
              '\nlocals()', locals())
        return next(generator)
    print('createCounter1():'
          '\nglobals():', globals(),
          '\nlocals()', locals())
    return counter


Counter1 = createCounter1()
print(Counter1(), Counter1(), Counter1())


# list写法
def createCounter2():
    n = [0]

    def counter():
        n[0] = n[0] + 1
        return n[0]
    return counter


Counter = createCounter2()
print(Counter(), Counter(), Counter())


# int写法
def createCounter3():
    n = 0

    def counter():
        nonlocal n
        n = n + 1
        return n
    return counter


Counter = createCounter3()
print(Counter(), Counter(), Counter())