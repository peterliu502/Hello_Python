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
    * 输出 __"hello，world!"__
        ```python
        print("hello，world!")
        ```
    * 了解 [__"#!/usr/bin/env python3"__](https://www.jianshu.com/p/400c612381dd) 作用   
        * 含义  
            注释是为了告诉 Linux / OS X 系统，这是一个 python3 可执行程序，这在电脑上同时安装了 python2 和 python3 的时候尤其重要，因为 python3 不向下兼容。而 Windows 系统会忽略这个注释；  
        * env的作用  
            ```python
            #!/usr/bin/env python3 
            ```
            该代码表示从 "PATH 环境变量"中查找 python3 解释器的位置, 路径没有被写死, 而是在"环境变量"中寻找 python3 解释器的安装路径, 再调用该路径下的解释器来执行脚本。  
           ```python
            #!/usr/bin/python3
            ```
            该代码表示 python3 解释器所处的绝对路径就是 /usr/bin/python3, 路径被写死了, 类似于编程中的"硬编码"。之所以有这种写法, 是因为在类 Unix 系统中, python 解释器一般情况下都位于这个路径。不过, 如果碰到 python 解释器不在该路径下的话, 脚本就无法执行了。  
            
            显然, 采用第一种写法更灵活更具有通用性, 推荐使用这种写法。  
    * 了解 [__"## -\*- coding: utf-8 -\*-"__](https://blog.csdn.net/zhongbeida_xue/article/details/81736671) 作用  
        * 含义  
            如果没有此文件编码类型的声明，则 python 默认以ASCII编码去处理；如果你没声明编码，但是文件中又包含非ASCII编码的字符的话，python解析器去解析的 python 文件，自然就会报错了。  
            必须放在python文件的第一行或第二行。   
            声明格式要符合[__正则表达式__](https://blog.csdn.net/xld_19920728/article/details/80534146)  
            ```python
            "__coding[:=]\s*([-\w.]+)__"
            ```
### 2. [20200107_02_输入输出.py](https://github.com/peterliu502/Hello_Python/blob/develop/20200107_02_%E8%BE%93%E5%85%A5%E8%BE%93%E5%87%BA.py)
* __time__  
2020-01-07
* __content__
    * print()函数
        * 参数：
            * 参数定义：    
                ```python
                print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)  
                ```
            * objects  
                复数，表示可以一次输出多个对象。输出多个对象时，需要用 , 分隔。  
            * sep  
                用来间隔多个对象，默认值是一个空格。  
                可以通过修改成
                ```python
                print(sep='')
                ```
                实现取消 , 分隔对象产生的空格；  
                可以通过修改成
                ```python
                print(sep='\n')
                ```
                实现逐行输出变量。  
            * end  
                用来设定以什么结尾。默认值是换行符 \n。  
                可以通过修改成
                ```python
                print(end='')
                ```
                实现输出显示不自动换行。  
            * file  
                要写入的文件对象。  
            * flush  
                输出是否被缓存通常决定于 file，但如果 flush 关键字参数为 True，流会被强制刷新。  
        * 显示单个字符串  
            需使用" "或' '引住文字
        * 显示多个字符串  
            使用","符号，默认状态下显示时","会被显示成空格，但可以通过修改print()函数的sep参数进行修改。除了连接多个字符串，","还可以连接多个算式或者是连接字符串与算式；  
            使用"+"符号，显示时字符串之间不会有空格。"+"只可以连接字符串，或者在多个数字或者算式之间作运算符使用，即数学意义上的加号。但不可以连接字符串与数字或算式；  
        * 转义符
            * \\:
                * 写法：  
                    ```python
                    \\
                    ```
            * "or':
                * 写法：
                    ```python
                    \"
                    \'
                    ```
            * 换行符\n:
                * 写法：
                    ```python
                    \\n
                    ```
            * 制表符\t:
                * 写法： 
                    ```python
                    \\t
                    ```
                * 作用：  
                    制表符作用是将字符串的字数补齐成8的倍数，一般是输出表格的时候自动将各列对齐时使用的。  
                    举例来说"abc\t"，就是在"abc"后面补上5个空格，凑齐8个字符。而"abcdefghijk\t"一共11个字符，已经超过了8个字符，但是不满足16个字符，所以\t的作用就是补上7个空格，补齐16个字符。  
                    在某些编译器中\t不是默认占8位，可能是4位，但是一般可以手动调整。  
            * r'_文本_' or r"_文本_"：
                * 作用：  
                    在字符串引号前加上r，可以让字符串强制不转义。当字符串中存在引号时，真正用于括字符串的引号要注意作区别，文本中存在单引号外侧就要用双引号，反之亦然。  
                    举例：
                    ```python
                    print("I'm Peter.")
                    # 文本含单引号，外扩双引号
                    print('他说："我是彼得。"')
                    # 文本含双引号，外扩单引号
                    ```
                    当字符串中同时存在""和''两种引号时，r''和r""都不太好用，建议单独转义。因为英文中的引号无前后之分，字符串中的引号必然会和真正的引号混在一起，使字符串异常。  
                    举例：
                    ```python
                    print(r"I'm Peter,'他说："我是彼得。"")
                    # 程序会把"I'm Peter,'他说："识别成第一个字符串，而"我是彼得。""则会识别异常；
                    print(r'I'm Peter,'他说："我是彼得。"')
                    # 程序会把"I"识别成第一个字符串，而"'m Peter,'他说："我是彼得。""则会识别异常；
                    ```
            * """_文本_""":
                * 作用:  
                    字符串直接使用回车键换行，不需要在行末加\n。
        * 显示数字或算式  
            print()函数可以接收一个变量或算式，直接显示变量的值或者是算式的结果；  
    * input()函数  
        input()函数中可以输入一个提示语，作为显示界面中提示用户输入的引导语；  
        input()函数输出的是字符串类型。    
### 3. [20200109_01_数据类型与变量.py](https://github.com/peterliu502/Hello_Python/blob/master/20200109_01_%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B%E4%B8%8E%E5%8F%98%E9%87%8F.py)
* __time__  
2020-01-09
* __content__
    * 数据类型
        * 分类
            * 整数（int）：  
                即整型。不仅指十进制的整数，python也可以处理其他进制的整数  
                python的整数没有大小限制  
            * 浮点数（float）：  
                即小数  
                python的浮点数没有大小限制，但超过一定范围就直接表示为inf（无限大）   
            * 字符串（str）：  
                需要用" "或' '将字符串文本内容括起来；  
            * 布尔值（bool）：  
                * 分类：  
                只有True和False两种，首字母必须大写；  
                * 运算：
                    * and（与运算）：  
                        只有所有都为True，and运算结果才是True  
                    * or（或运算）  
                        只要其中有一个为True，or运算结果就是True  
                    * not（非运算）  
                        它是一个单目运算符，把True变成False，False变成True  
            * 空值（None）  
                空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值，可以理解为没有任何东西。  
    * 变量
        * 变量名的表示方法：  
            变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头；  
        * 赋值：  
            等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量  
            请不要把赋值语句的等号等同于数学的等号。比如下面的代码：  
            ```python
            x = 10  
            x = x + 2
            ```
            如果从数学上理解x = x + 2那无论如何是不成立的，在程序中，赋值语句先计算右侧的表达式x + 2，得到结果12，再赋给变量x。由于x之前的值是10，重新赋值后，x的值变成12。  
        * 动态语言：  
            这种变量本身类型不固定的语言称之为动态语言，主要动态语言：Object-C、C#、JavaScript、PHP、Python、Erlang  
            与之对应的是静态语言，静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。主要静态语言：Java、C、C++  
        * 变量在内存中的表示方法  
            当我们写：
            ```python
            a = 'ABC'
            ```
            时，Python解释器干了两件事情：  
            1. 在内存中创建了一个'ABC'的字符串；  
            2. 在内存中创建了一个名为a的变量，并把它指向'ABC'。   
            也可以把一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指向的数据，例如下面的代码：
            ```python
            a = 'ABC'
            b = a
            a = 'XYZ'
            print(b)
            ```
            程序执行过程如下：  
            1.执行
            ```python
            a = 'ABC'
            ```
            解释器创建了字符串'ABC'和变量a，并把a指向'ABC'：  
            ![avatar](https://static.liaoxuefeng.com/files/attachments/923791878255456/0)  
            2.执行
            ```python
            b = a
            ```
            解释器创建了变量b，并把b指向a指向的字符串'ABC'：  
            ![avatar](https://static.liaoxuefeng.com/files/attachments/923792058613440/0)  
            3.执行
            ```python
            a = 'XYZ'
            ```
            解释器创建了字符串'XYZ'，并把a的指向改为'XYZ'，但b并没有更改：  
            ![avatar](https://static.liaoxuefeng.com/files/attachments/923792191637760/0)  
            4.所以，最后打印变量b的结果自然是'ABC'了  
    * 常量  
        所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在python中，通常用全部大写的变量名表示常量：
        ```python
        PI = 3.14159265359
        ```
        但事实上PI仍然是一个变量，python根本没有任何机制保证PI不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果一定要改变变量PI的值，并不会报错
    * 除法
        * /除法  
            /除法计算结果是浮点数，即使是两个数恰好整除，结果也是浮点数。可参考以下代码：
            ```python
            print(9/3)
            print(10/3)
            print(9.0/3.0)
            print(10.0/3.0)
            ```
            python浮点数运算遵循IEEE 754的浮点运算标准，往往存在误差，或者叫做有限精度。  
            参考以下算式：
            ```python
            print(0.1+0.2)
            print(0.1+0.1+0.1-0.3)
            ```  
        * //除法  
            //除法称为地板除，两个数的地板除结果是商取整，即使除不尽。具体参考以下代码：
            ```python
            print(9//3)
            print(10//3)  
            print(9.0//3.0)
            print(10.0//3.0)
            ```
            因为//除法只取结果的整数部分，所以Python还提供一个余数运算，可以得到两个整数相除的余数：
            ```python
            print(9%3)
            print(10%3)
            ```
            

