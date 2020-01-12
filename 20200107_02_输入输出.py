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
print()
print("1.\\n:\n换行符效果")
print("2.\\\\:\\")
print("3.\\t:\t制表符效果")
print('4.r"" or r\'\':' + r"\\\n\t")
# 当字符串中存在引号时，真正用于括字符串的引号要注意作区别，文本时单引号外侧就要用双引号，反之亦然。
# 举例："I'm Peter."，'他说"我是彼得。"'；
# 当字符串中同时存在""和''两种引号时，r''和r""都不太好用。
# 因为英文中的引号无前后之分，字符串中的引号必然会和真正的引号混在一起，使字符串异常。
# 举例："他说"我是彼得。""，这里程序会把"他说"识别成第一个字符串，而"我是彼得"则会识别异常；
print("""5.\"\"\"...\"\"\":
line2
line3""")
print('''5."""...""":
line2
line3''')
print("""12345678
a\tbcdefgh
ab\tcdefgh
abc\tdefgh
abcd\tefgh
abcde\tfgh
abcdef\tgh
abcdefg\th""")
