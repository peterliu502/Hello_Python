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
### 2. [20200107_02_输入输出.py](https://github.com/peterliu502/Hello_Python/blob/develop/20200107_02_%E8%BE%93%E5%85%A5%E8%BE%93%E5%87%BA.py)
* __time__  
2020-01-07
* __content__
    * print()函数
        * 显示单个字符串，需使用""或''引住文字
        * 显示多个字符串
            * 使用","符号，显示时","会被显示成空格，除了连接多个字符串，","还可以连接多个算式或者是连接字符串与算式；
            * 使用"+"符号，显示时字符串之间不会有空格。"+"只可以连接字符串。或者连接多个数字或者算式作运算符使用，不可以连接字符串与数字或算式；
        * 转义符
            * \:\\
            * "or':\"or\'
            * 换行符\n:\\n
            * 制表符\t:\\t，作用是将字符串的字数补齐成8的倍数，一般是输出表格的时候自动将各列对齐时使用的。举例来说"abc\t"，就是在"abc"后面补上5个空格，凑齐8个字符。而"abcdefghijk\t"一共11个字符，已经超过了8个字符，但是不满足16个字符，所以\t的作用就是补上7个空格，补齐16个字符。在某些编译器中\t不是默认占8位，可能是4位，但是一般可以手动调整。
            * r'' or r""，在字符串引号前加上r，可以让字符串强制不转义。当字符串中存在引号时，真正用于括字符串的引号要注意作区别，文本时单引号外侧就要用双引号，反之亦然。举例："I'm Peter."，'他说"我是彼得。"',当字符串中同时存在""和''两种引号时，r''和r""都不太好用。因为英文中的引号无前后之分，字符串中的引号必然会和真正的引号混在一起，使字符串异常。举例："他说"我是彼得。""，这里程序会把"他说"识别成第一个字符串，而"我是彼得"则会识别异常；
            * """..."""，作用是字符串直接使用回车键换行，不需要在行末加\n。
        * 显示数字或算式，print()函数可以接收一个变量或算式，直接显示变量的值或者是算式的结果；
    * input()函数
        * input()函数中可以输入一个提示语，作为显示界面中提示用户输入的引导语；  
        * input()函数输出的是字符串类型。
### 3. [20200109_01_数据类型与变量.py]()
* __time__  
2020-01-09
* __content__
    * 
