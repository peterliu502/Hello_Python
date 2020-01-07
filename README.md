# Hello_Python
***
## Description  
***
This repository is used to record my personal Python learning process.  
***
## List
### 1. [20200107_01_hello_world.py](https://github.com/peterliu502/Hello_Python/blob/master/20200107_01_hello_world.py)  
* __time__  
2020-01-07
* __content__  
    * 输出 __“hello，world！”__  
    * 了解 [__“#!/usr/bin/env python3”__](https://www.jianshu.com/p/400c612381dd) 作用   
        * 含义
            * 注释是为了告诉 Linux / OS X 系统，这是一个 python3 可执行程序，这在电脑上同时安装了 python2 和 python3 的时候尤其重要，因为 python3 不向下兼容。而 Windows 系统会忽略这个注释；  
        * env的作用
            * #!/usr/bin/env python3 表示从 "PATH 环境变量"中查找 python3 解释器的位置, 路径没有被写死, 而是在"环境变量"中寻找 python3 解释器的安装路径, 再调用该路径下的解释器来执行脚本。显然, 采用 #!/usr/bin/env python3 的写法更灵活更具有通用性, 推荐使用这种写法。  
            * #!/usr/bin/python3 表示 python3 解释器所处的绝对路径就是 /usr/bin/python3, 路径被写死了, 类似于编程中的"硬编码"。之所以有这种写法, 是因为在类 Unix 系统中, python 解释器一般情况下都位于这个路径。不过, 如果碰到 python 解释器不在该路径下的话, 脚本就无法执行了。  
    * 了解 [__“## -\*- coding: utf-8 -\*-”__](https://blog.csdn.net/zhongbeida_xue/article/details/81736671) 作用  
        * 含义
            * 如果没有此文件编码类型的声明，则 python 默认以ASCII编码去处理；如果你没声明编码，但是文件中又包含非ASCII编码的字符的话，python解析器去解析的 python 文件，自然就会报错了。
            * 必须放在python文件的第一行或第二行。 
            * 声明格式要符合[正则表达式 "__coding[:=]\s*([-\w.]+)__"](https://blog.csdn.net/xld_19920728/article/details/80534146)
### 2. 20200107_02_print().py
* __time__  
2020-01-07
* __content__