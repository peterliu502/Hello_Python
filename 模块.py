#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import mymodule.school  # import package[.subpackage]
from mymodule.book import *  # from package[.subpackage] import *
import mymodule.hello  # import package[.subpackage].module
from mymodule.math import myadd  # from package[.subpackage] import module
from mymodule.math.mytimes import mytimes  # from package[.subpackage].module import attribute


mymodule.hello.hello()
# 对于使用import package[.subpackage].module方式引入的module
# 调用时必须按照package[.subpackage].module.attribute的格式完整写出module与attribute的名字
print(myadd.myadd(1, 2, 3, 4, 5, 6, 7, 8, 9))
# 对于使用from package[.subpackage] import module方式引入module
# 调用时只需写module.attribute即可，但这种方式遇到来自不同package的同名module时会触发命名空间冲突
print(mytimes(1, 2, 3, 4, 5))
# 对于使用from package[.subpackage].module import attribute方式引入module
# 调用时可以直接用attribute调用，但是当来自不同module的attribute同名时也会触发命名空间冲突
print(ID.book_id('My birthday is today'))
# 可以将package/subpackage中的所有模块赋值给__init__.py中的__all__属性
# 然后使用from package[.subpackage] import *方式一次性引入module
print(mymodule.school.teacher.teacher('Bob'))
# 当package/subpackage中的所有模块已经预先在__init__.py中被引入后
# 只需引入__init__模块就可以将__init__.py内提前引入的模块批量引入
