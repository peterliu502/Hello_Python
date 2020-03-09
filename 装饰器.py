#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import functools


# 写一个装饰器
# 功能：在调用函数前返回函数返回值的类型
def log(my_func):  # 用于接收函数对象
    def wrapper(*args, **kwargs):  # 用于返回的闭包
        print(type(my_func()))
        return my_func(*args, **kwargs)

    return wrapper


# 装饰器的使用
@log  # 等价于my_func = log(my_func)，记住赋值符右侧先执行
def my_func(*args):
    return list(args)


my_var = my_func(1, 2, 3, 4, 5, 6, 7, 8, 9)
print('func name is:', my_func.__name__)  # my_func的__name__属性已经被log装饰器修改为wrapper了


# 装饰器本身需要输入参数的情况
# 三层函数嵌套
def log2(text):  # 接收装饰器参数
    def decorator(my_func):  # 用于接收函数对象
        def wrapper(*args, **kwargs):  # 用于返回的闭包
            print('{:s} call this function:\n'
                  '{:s}:'.format(text, my_func.__name__))
            return my_func(*args, **kwargs)

        return wrapper

    return decorator


@log2('Peter')
# log2函数的参数在log语句处输入，而不是在赋值处输入
# 等价于my_func1 = log2('Peter')(my_func1)，记住赋值符右侧先执行
def my_func1(*args):
    return {i: j for i, j in zip(range(len(args)), args)}


my_var1 = my_func1
print(my_var1(1, 2, 3, 4, 5, 6, 7, 8, 9))
print('func name is:', my_func1.__name__)  # my_func1的__name__属性已经被log装饰器修改为wrapper了


# 修正被绑定装饰器函数的__name__属性
# 不然后续调用函数名是会出现错误
def log3(text):  # 接收装饰器参数
    def decorator(my_func):  # 用于接收函数对象
        @functools.wraps(my_func)  # 注意@functools.wraps()需写接收函数对象的那层函数作用域内
        def wrapper(*args, **kwargs):  # 用于返回的闭包
            print('{:s} call this function:\n'
                  '{:s}:'.format(text, my_func.__name__))
            return my_func(*args, **kwargs)

        return wrapper

    return decorator


@log3('LZY')
def my_func2(*args):
    return {i: j for i, j in zip(range(len(args)), args)}


my_var2 = my_func2
print(my_func2('1', 2, False, (1, 3), 'ai', {1: '234'}))
print('func name is:', my_func2.__name__)


# 作业：设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
def metric(fn):  # 接收函数对象
    @functools.wraps(fn)  # 修正函数__name__属性
    def decorator(*args, **kwargs):  # 接收原函数的参数
        print('%s executed in %s ms' % (fn.__name__, 10.24))  # 装饰器操作
        return fn(*args, **kwargs)  # 返回原函数的值

    return decorator  # 返回闭包


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


# 作业：在函数调用的前后打印出'begin call'和'end call'的日志
def log4(text):  # 用于接收函数对象
    if isinstance(text, str):  # 也可以改为if isinstance(text, function)，然后对调if和else的分支
        def decorator(my_func):
            @functools.wraps(my_func)  # 修正函数__name__属性
            def wrapper(*args, **kwargs):  # 用于返回的闭包
                start_time = time.time()
                print('begin call {:s} at {:f}'.format(my_func.__name__, start_time))
                my_var = my_func(*args, **kwargs)
                end_time = time.time()
                print('end call {:s} at {:f}'.format(my_func.__name__, end_time))
                print('{:s} the func in {:e}ms'.format(text, 1000 * (end_time - start_time)))
                return my_var

            return wrapper

        return decorator
    else:
        def wrapper(*args, **kwargs):  # 用于返回的闭包
            start_time = time.time()
            print('begin call {:s} at {:f}'.format(text.__name__, start_time))
            my_var = text(*args, **kwargs)
            end_time = time.time()
            print('end call {:s} at {:f}'.format(text.__name__, end_time))
            return my_var

        return wrapper


def log5(text):  # 用于接收函数对象
    if callable(text):  # 也可以改为if isinstance(text, function)，然后对调if和else的分支
        def wrapper(*args, **kwargs):  # 用于返回的闭包
            start_time = time.time()
            print('begin call {:s} at {:f}'.format(text.__name__, start_time))
            my_var = text(*args, **kwargs)
            end_time = time.time()
            print('end call {:s} at {:f}'.format(text.__name__, end_time))
            return my_var

        return wrapper
    else:
        def decorator(my_func):
            @functools.wraps(my_func)  # 修正函数__name__属性
            def wrapper(*args, **kwargs):  # 用于返回的闭包
                start_time = time.time()
                print('begin call {:s} at {:f}'.format(my_func.__name__, start_time))
                my_var = my_func(*args, **kwargs)
                end_time = time.time()
                print('end call {:s} at {:f}'.format(my_func.__name__, end_time))
                print('{:s} the func in {:e}ms'.format(text, 1000 * (end_time - start_time)))
                return my_var

            return wrapper

        return decorator


@log5('execute')
def my_abs(num):
    print('the result is:', abs(num))
    return abs(num)


print(type(my_abs))
my_var3 = my_abs
my_var3(-99)
