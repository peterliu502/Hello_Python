#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fact(n):
    if type(n) != int:
        raise TypeError("'bad operand type'")
    elif n == 0:
        return 0
    elif n == 1:
        return n
    else:
        return n * fact(n - 1)


print(fact(1))
print(fact(3))
print(fact(10))


# 尾递归：在函数返回的时候，调用自身本身。并且，return语句不能包含表达式
# 尾递归可以解决递归层数太多导致栈溢出的异常，而且与循环是等价的
# 关键在于在调用递归前要处理完变量
# 示例1是在调用递归函数定义形参时完成了对变量的处理
def fact_iter(num, product=1):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact_iter(1))
print(fact_iter(3))
print(fact_iter(10))


# 示例2是在调用者的函数体中完成了对参数的处理，然后才调用递归函数
def fact_iter(num, product=1):
    if num == 1:
        return product
    product *= num
    num -= 1
    return fact_iter(num, product)


print(fact_iter(1))
print(fact_iter(3))
print(fact_iter(10))


# 训练
# 汉诺塔
def tower(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        tower(n - 1, a, c, b)
        print(a, '-->', c)
        tower(n - 1, b, a, c)


tower(2, 'A', 'B', 'C')


# 序列求和
def sum_list(my_list: list, my_sum=0):
    if len(my_list) == 1:
        my_sum += my_list.pop()
        return my_sum
    else:
        my_sum += my_list.pop()
        return sum_list(my_list, my_sum)


print(sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# 买汽水：
# 1块钱可以买一瓶汽水,2个空瓶可以换一瓶,3个瓶盖可以换一瓶,问:20块钱最终能得到多少瓶?
def buy_cola(money, bottle=0, cap=0, num=0):
    if (money < 1) & (bottle < 2) & (cap < 3):
        return num
    else:
        cola = 0
        cola += money  # 钱换可乐
        money = money % 1  # 结算钱
        cola += (bottle // 2)  # 瓶子换可乐
        bottle = bottle % 2  # 结算瓶子
        cola += (cap // 3)  # 盖子换可乐
        cap = cap % 3  # 结算盖子
        num += cola  # 统计可乐
        bottle += cola  # 产生瓶子
        cap += cola  # 产生盖子
        return buy_cola(money, bottle, cap, num)


print(buy_cola(2))


# 买汽水重构1：合并步骤
def buy_cola1(money, bottle=0, cap=0, num=0):
    if (money < 1) & (bottle < 2) & (cap < 3):
        return num
    else:
        cola = money + (bottle // 2) + (cap // 3)  # 换可乐(钱换可乐+盖子换可乐+瓶子换可乐)
        num += cola  # 统计可乐
        money = money % 1  # 结算钱
        bottle = bottle % 2 + cola  # 结算瓶子(-换可乐的+新可乐生成的)
        cap = cap % 3 + cola  # 结算盖子(-换可乐的+新可乐生成的)
        return buy_cola1(money, bottle, cap, num)


print(buy_cola1(2))


# 买汽水重构2：去掉money参数，改为给bottle和cap一个初始值
def buy_cola2(bottle, cap, num):
    if (bottle < 2) & (cap < 3):
        return num
    else:
        my_sum = (bottle // 2) + (cap // 3)
        num += my_sum  # 换可乐(盖子换可乐+瓶子换可乐)
        bottle = bottle % 2 + my_sum  # 结算瓶子(-换可乐剩的的+新可乐生成的)
        cap = cap % 3 + my_sum  # 结算盖子(-换可乐剩的的+新可乐生成的)
        return buy_cola2(bottle, cap, num)


print(buy_cola2(2, 2, 2))
