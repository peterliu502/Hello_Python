#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("hello,world!")
print("100", "+", "200", "+", "300", "=", 100 + 200 + 300)
print("1024 * 768 =", 1024 * 768)
print("Good", "morning!")
print("")
name = input("请输入您的名字：")
print("尊敬的" + name + "您好！")
a = int(input("请输入您母亲的年龄："))
b = int(input("请输入您的年龄："))
c = int(a - b)
d = a - b
e = 1
f = 1.0
g = e + f
print()
print(type(d))  # 赋值的传递性，定义为a和b的数据类型
print(type(name))  # input返回值为str类型
print(type(e))  # 赋值的传递性，随1定义为int
print(type(f))  # 赋值的传递性，随1.1定义为float
print(type(g))  # int与float运算，结果为float
print(g)  #int与float运算，结果为float
print()
print("您母亲是在", int(a) - int(b), "岁时生的您。")  # int与str混用，只能用，相连
print("您母亲是在", a - b, "岁时生的您。")  # int与str混用，只能用，相连
print("您母亲是在", c, "岁时生的您。")  # int与str混用，只能用，相连
print("您母亲是在", int(a - b), "岁时生的您。")  # int与str混用，只能用，相连
print("您母亲是在", str(a - b), "岁时生的您。")  # 三个str，可以用,和+相连
print("您母亲是在", str(c), "岁时生的您。")  # 三个str，可以用,和+相连
print("您母亲是在" + str(a - b) + "岁时生的您。")  # 三个str，可以用,和+相连
print("您母亲是在" + str(c) + "岁时生的您。")  # 三个str，可以用,和+相连
