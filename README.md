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
    * 了解 ["#!/usr/bin/env python3"](https://www.jianshu.com/p/400c612381dd) 作用   
        * 含义  
            注释是为了告诉 `Linux` / `OS X` 系统，这是一个 `python3` 可执行程序，这在电脑上同时安装了 `python2` 和 `python3` 的时候尤其重要，因为 `python3` 不向下兼容。而 `Windows` 系统会忽略这个注释；  
        * env的作用  
            ```python
            #!/usr/bin/env python3 
            ```
            该代码表示从`PATH 环境变量`中查找 `python3` 解释器的位置, 路径没有被写死, 而是在`环境变量`中寻找 `python3` 解释器的安装路径, 再调用该路径下的解释器来执行脚本。  
           ```python
            #!/usr/bin/python3
            ```
            该代码表示 `python3` 解释器所处的绝对路径就是 `/usr/bin/python3`, 路径被写死了, 类似于编程中的`硬编码`。之所以有这种写法, 是因为在`类 Unix` 系统中, python 解释器一般情况下都位于这个路径。不过, 如果碰到 python 解释器不在该路径下的话, 脚本就无法执行了。  
            
            显然, 采用第一种写法更灵活更具有通用性, 推荐使用这种写法。  
    * 了解 <a id = '编码声明'>["## -\*- coding: utf-8 -\*-"](https://blog.csdn.net/zhongbeida_xue/article/details/81736671)</a> 作用  
        * 含义  
            如果没有此文件编码类型的声明，则 python2 默认以`ASCII`编码去处理；如果你没声明编码，但是文件中又包含非`ASCII`编码的字符的话，python解析器去解析的 python 文件，自然就会报错了。  
            必须放在python文件的第一行或第二行。   
            声明格式要符合[正则表达式](https://blog.csdn.net/xld_19920728/article/details/80534146)  
            ```python
            "__coding[:=]\s*([-\w.]+)__"
            ```
### 2. [20200107_02_输入输出.py](https://github.com/peterliu502/Hello_Python/blob/develop/20200107_02_%E8%BE%93%E5%85%A5%E8%BE%93%E5%87%BA.py)
* __time__  
2020-01-07
* __content__
    * [print()函数](https://docs.python.org/zh-cn/3.8/library/functions.html#print)
        * 函数定义：    
                ```python
                print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)  
                ```
        * 参数：
            * `objects`  
                复数，表示可以一次输出多个对象。输出多个对象时，需要用`,`分隔。  
            * `sep`  
                用来间隔多个对象，默认值是一个空格。  
                可以通过修改成
                ```python
                print(sep='')
                ```
                实现取消`,`分隔对象产生的空格；  
                可以通过修改成
                ```python
                print(sep='\n')
                ```
                实现逐行输出变量。  
            * `end`  
                用来设定以什么结尾。默认值是换行符`\n`。  
                可以通过修改成
                ```python
                print(end='')
                ```
                实现输出显示不自动换行。  
            * `file`  
                要写入的文件对象。  
            * `flush`  
                输出是否被缓存通常决定于 file，但如果`flush`关键字参数为True，流会被强制刷新。  
        * 显示单个字符串  
            需使用`" "`或`' '`引住文字
        * 显示多个字符串  
            使用`,`符号，默认状态下显示时`,`会被显示成空格，但可以通过修改`print()`函数的`sep`参数进行修改。除了连接多个字符串，`,`还可以连接多个算式或者是连接字符串与算式；  
            使用`+`符号，显示时字符串之间不会有空格。`+`只可以连接字符串，或者在多个数字或者算式之间作运算符使用，即数学意义上的加号。但不可以连接字符串与数字或算式；  
        * 转义符
            * `\`:
                * 写法：  
                    ```python
                    \\
                    ```
            * `"`or`'`:
                * 写法：
                    ```python
                    \"
                    \'
                    ```
            * 换行符`\n`:
                * 写法：
                    ```python
                    \\n
                    ```
            * 制表符`\t`:
                * 写法： 
                    ```python
                    \\t
                    ```
                * 作用：  
                    制表符\t作用是将字符串的字数补齐成8的倍数，一般是输出表格的时候自动将各列对齐时使用的。  
                    举例来说"abc\t"，就是在"abc"后面补上5个空格，凑齐8个字符。而"abcdefghijk\t"一共11个字符，已经超过了8个字符，但是不满足16个字符，所以\t的作用就是补上7个空格，补齐16个字符。  
                    在某些编译器中\t不是默认占8位，可能是4位，但是一般可以手动调整。  
            * `r'文本'` or `r"文本"`：
                * 作用：  
                    在字符串引号前加上`r`，可以让字符串强制不转义。当字符串中存在引号时，真正用于括字符串的引号要注意作区别，文本中存在单引号外侧就要用双引号，反之亦然。  
                    举例：
                    ```python
                    print("I'm Peter.")
                    # 文本含单引号，外扩双引号
                    print('他说："我是彼得。"')
                    # 文本含双引号，外扩单引号
                    ```
                    当字符串中同时存在`""`和`''`两种引号时，`r''`和`r""`都不太好用，建议单独转义。因为英文中的引号无前后之分，字符串中的引号必然会和真正的引号混在一起，使字符串异常。  
                    举例：
                    ```python
                    print(r"I'm Peter,'他说："我是彼得。"")
                    # 程序会把"I'm Peter,'他说："识别成第一个字符串，而"我是彼得。""则会识别异常；
                    print(r'I'm Peter,'他说："我是彼得。"')
                    # 程序会把"I"识别成第一个字符串，而"'m Peter,'他说："我是彼得。""则会识别异常；
                    ```
            * `"""文本"""`:
                * 作用:  
                    字符串直接使用回车键换行，不需要在行末加`\n`。
        * 显示数字或算式  
            `print()`函数可以接收一个变量或算式，直接显示变量的值或者是算式的结果；  
    * [input()函数](https://docs.python.org/zh-cn/3.8/library/functions.html#input)  
        * 函数定义  
            input(prompt)
        * 参数
            * prompt  
                `input()`函数中可以输入一个`提示语`(`prompt`)，作为显示界面中提示用户输入的引导语；  
        * 返回值  
            `input()`函数输出的是字符串类型。    
### 3. [20200109_01_数据类型与变量.py](https://github.com/peterliu502/Hello_Python/blob/master/20200109_01_%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B%E4%B8%8E%E5%8F%98%E9%87%8F.py)
* __time__  
2020-01-09
* __content__
    * 数据类型
        * 分类
            * [`整数`（`int`）](https://docs.python.org/zh-cn/3.8/library/functions.html#int)：  
                即整型。不仅指十进制的整数，python也可以处理其他进制的整数  
                python的整数没有大小限制  
            * [`浮点数`（`float`）](https://docs.python.org/zh-cn/3.8/library/functions.html#float)：  
                即小数  
                `python`的浮点数没有大小限制，但超过一定范围就直接表示为`inf`（`无限大`）   
            * [`字符串`（`str`）](https://docs.python.org/zh-cn/3/library/stdtypes.html#str)：  
                * 类定义：
                    * str(object='')  
                        如果`encoding`或`errors`均未给出，则直接返回内容为`object`的字符串，`object`实参需要用`''`或`""`括起      
                    * str(object=b'', encoding='utf-8', errors='strict')  
                        如果`object`是一个`bytes-like object`(例如`bytes`或`bytearray`)，`encoding`或`errors`至少给出其中之一，否则会把`object`当`str`类型  
                        str(bytes, encoding, errors) 等价于<a href = '#decode()'>bytes.decode(encoding, errors)</a>  
            * [`布尔值`（`bool`）](https://docs.python.org/zh-cn/3.8/library/functions.html#bool)：  
                * 分类：  
                只有`True`和`False`两种，首字母必须大写；  
                * 运算：
                    * `and`（`与运算`）：  
                        只有所有都为`True`，`and`运算结果才是`True`  
                    * `or`（`或运算`）  
                        只要其中有一个为`True`，`or`运算结果就是`True`  
                    * `not`（`非运算`）  
                        它是一个`单目运算符`，把`True`变成`False`，`False`变成`True`  
            * [`空值`（`None`）](https://docs.python.org/zh-cn/3.8/library/constants.html#None):  
                空值是Python里一个特殊的值，用`None`表示。`None`不能理解为0，因为0是有意义的，而`None`是一个特殊的空值，可以理解为没有任何东西。  
    * 变量
        * 变量名的表示方法：  
            变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和下划线的组合，且不能用数字开头；  
        * 赋值：  
            等号`=`是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量  
            请不要把赋值语句的等号等同于数学的等号。比如下面的代码：  
            ```python
            x = 10  
            x = x + 2
            ```
            如果从数学上理解x = x + 2那无论如何是不成立的，在程序中，赋值语句先计算右侧的表达式x + 2，得到结果12，再赋给变量x。由于x之前的值是10，重新赋值后，x的值变成12。  
        * 动态语言：  
            这种变量本身类型不固定的语言称之为`动态语言`，主要动态语言：`Object-C`、`C#`、`JavaScript`、`PHP`、`Python`、`Erlang`  
            与之对应的是`静态语言`，静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。主要静态语言：`Java`、`C`、`C++`  
        * 变量在内存中的表示方法  
            当我们写：a = 'ABC'时，Python解释器干了两件事情：  
            1.在内存中创建了一个'ABC'的字符串；  
            2.在内存中创建了一个名为a的变量，并把它指向'ABC'。   
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
        所谓常量就是不能变的变量，比如常用的数学常数`π`就是一个常量。在`python`中，通常用全部大写的变量名表示常量：
        ```python
        PI = 3.14159265359
        ```
        但事实上`PI`仍然是一个变量，`python`根本没有任何机制保证`PI`不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果一定要改变变量PI的值，并不会报错
    * 除法
        * /除法  
            /除法计算结果是浮点数，即使是两个数恰好整除，结果也是浮点数。可参考以下代码：
            ```python
            print(9/3)
            print(10/3)
            print(9.0/3.0)
            print(10.0/3.0)
            ```
            python浮点数运算遵循`IEEE 754`的浮点运算标准，往往存在误差，或者叫做有限精度。  
            参考以下算式：
            ```python
            print(0.1+0.2)
            print(0.1+0.1+0.1-0.3)
            ```  
        * //除法  
            //除法称为`地板除`，两个数的地板除结果是商取整，即使除不尽。具体参考以下代码：
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
 ### 4. [20200201_01_字符串与编码.py](https://github.com/peterliu502/Hello_Python/blob/master/20200201_01_%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%8E%E7%BC%96%E7%A0%81.py)
* __time__  
2020-02-01
* __content__           
    * 字符编码
        * 字节  
            由于计算机只能处理二进制数字，所以所有的文本都必须转为数字才可以交由计算机处理。因此通常由8`比特`（`bit`）构成1个`字节`（`byte`），也可以理解为为每1个字符都可以对应一个8位的二进制数字。  
            1个字节8比特可以表示`2^8`个数字（`0`-`255`），2个字节16比特可以表示`2^16`个数字（`0`-`65535`），4个字节32比特可以表示`2^32`个数字（`0`-`4294967295`）
        * 几种常用编码
            * ASCII  
                全称`美国信息交换标准代码`。计算机最早由美国人发明，所以一开始设计编码时只考虑到了26个英文字母大小写、数字以及一些基本符号，合计127个字符。这个字符编码表就被称为`ASCII编码表`。  
                由于字符数没有超出8比特的表示范围（`256`），所以`ASCII`码用1个字节表示1个字符。而实际上，`ASCII`的字符数根本不需要8位数字，7位即可。所以首位数字一般默认为0，只有在一些`ASCII`码的变形编码上会将首位标为1，使之与原版`ASCII`码作区别。
            * Unicode  
                由于`ASCII`码没有包含非英语字符，所以后续又出现了许多包含非英语字符的编码，这些编码大多与`ASCII`码兼容  
                比如中文的`GB2312`编码，与`ASCII`码不同的是由于中文字符数量远大于英文字符，1个字节的范围不够表示所有字符，所以`GB2312`编码采用2字节构成1个字符。诸如此类的编码还有很多，比如日文的`Shift_JIS`编码，韩文的`Euc-kr`编码等等  
                但如果同时存在两种或以上语言的字符，采用任何一种编码都会出现乱码。针对这种情况，出现了将各种编码整合到一起的`Unicode`编码，该编码大多使用2字节构成一个字符，少部分字符需要4字节。目前大部分操作系统和编程语言都可以很好的支持`Unicode`。  
                无论是`Unicode`还是`UTF-16`，都是2字节起步，所以`ASCII`码需要补1个字节，即在前面补上`00000000`，凑齐16比特。  
            * UTF-8  
                由于`Unicode`中1个字符的字节数至少是`ASCII`码的2倍，这意味着`Unicode`所需的存储空间也至少是`ASCII`码的2倍。这使得文本基本以英文为主时，使用`Unicode`在存贮和传输上非常浪费。  
                而`UTF-8`码则解决了这个问题，`UTF-8`码是一种`可变长编码`。1个字符对应的字节数由1个到6个不等。`ASCII`码中的字符采用1个字节，与`ASCII`保持一致，大部分汉字采用3个字节，部分生僻字符采用4-6个字节。在以英文字符为主时可以节省大量空间。
        * 几种常用编码对比  
        
            |  字符  |  ASCII  |      Unicode       |           UTF-8            |
            |  :-:  |    :-:   |        :-:         |            :-:             |
            |   A   | 01000001 | 00000000 01000001  |          01000001          |
            |   中  |     X    | 01001110 00101101  | 11100100 10111000 10101101 |  
             
            可以看出`ASCII`码中的字符在`UTF-8`中的编码并没有变化，这意味着一些只支持`ASCII`编码的软件与系统可以在`UTF-8`中较好的运行。  
            在计算机内存中默认使用`Unicode`编码，而数据传输和储存时考虑到存储体积更偏向于使用`UTF-8`编码，因此在日常计算机操作中经常涉及到几种字符编码的转换，具体可以参看以下2个例子：  
            1.编辑`UTF-8`编码的TXT格式文档  
            ![avatar](https://static.liaoxuefeng.com/files/attachments/923923787018816/0)  
            2.浏览网页中的文本  
            ![avatar](https://static.liaoxuefeng.com/files/attachments/923923759189600/0)  
            很多网页的源码上会有类似`<meta charset="UTF-8" />`的信息，表示该网页正是用的`UTF-8`编码。  
        * python中的默认编码  
            `python2`中默认编码是`ASCII`，所以在程序开头必须带上<a href = '#编码声明'>`## -*- coding: utf-8 -*-`</a>，以保证`utf-8`编码的字符可以正常显示。  
            `python3`则默认采用`Unicode`编码，具体来说就是默认用`utf-8`编码去读源代码文件，而`python`内存中运行中的`str`是`Unicode`编码  
            然而通过`getsizeof()`方法插看`str`内存大小发现，`str`中`ASCII`字符为1字节，非`ASCII`字符为2字节，这与`Unicode`编码中所有字符都为2字节的设计有所差别。推测是因为出于节约空间的考虑，并非完全默认使用`Unicode`编码，而是将`ASCII`字符都按`ASCII`编码进行储存，非`ASCII`字符前`2^16`个字符每个2字节，往后每个4字节   
            检测方法：  
            ```python
            import sys
            for i in range(1, 200):
              s1 = ''.join(chr(n) for n in range(i))
              s2 = ''.join(chr(n) for n in range(i + 1))
              print('getsizeof{}={:d}'.format(i, sys.getsizeof(s2) - sys.getsizeof(s1)))
            # ASCII字符1字节
            for i in range(2**16 - 10, 2**16 + 10):
              s1 = ''.join(chr(n) for n in range(i))
              s2 = ''.join(chr(n) for n in range(i + 1))
              print('getsizeof{}={:d}'.format(i, sys.getsizeof(s2) - sys.getsizeof(s1)))
            # 非ASCII字符中，第2^16个字符之前每个字符2字节，往后每个字符4字节
            ```  
            测试结果中，第`127`/`255`/`2^16`个字符比较异常，原因是这几个字节正好是编码中首位数字由0变1的字符，所以结构体所占的内存也会有变化  
    * 字符串  
        * <a id = 'ord()'>[ord()函数](https://docs.python.org/zh-cn/3/library/functions.html#ord)</a>  
            * 函数定义  
                ord(c)  
            * 参数
                * c  
                对表示单个`Unicode`字符的字符串c，返回代表它`Unicode码点`的`int对象`。  
            * 返回值
                `int`  
            * 逆函数  
                <a href = '#chr()'>`chr()`</a>  
            * 备注
                `ord()`只能接收`str`，所以注意`str`类型的'1'和`int`类型的1之间的区别
        * <a id = 'chr()'>[chr()函数](https://docs.python.org/zh-cn/3/library/functions.html#chr)</a>  
            * 函数定义  
                chr(i)
            * 参数
                * i  
                    返回`Unicode`码位为`int`对象`i`的`str`格式字符  
                    `i`的取值范围为`0`到 `1,114,111`（`16进制`表示是`0x10FFFF`）。如果`i`超过这个范围，会触发`ValueError`异常。  
            * 返回值  
                `str`对象
            * 逆函数  
                <a href = '#ord()'>`ord()`</a>  
            * 备注  
                >1.`int`类型的四种进制整数对`chr()`来说没有区别，或者说这四种进制数对程序来说一般也没有区别。  
                2.`python`可以直接支持`Unicode`编码，所以直接在`str`对象中输入`\u`+四位`Unicode`编码即可打印出字符  
        * <a id = 'encode()'>[encode()方法](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.encode)</a>  
            * 作用  
                `str`类型的特殊方法，返回原字符串编码为字节串对象的版本。
            * 方法定义
                str.encode(encoding="utf-8", errors="strict")  
            * 参数  
                * encoding  
                    设定`encode()`返回的字节串编码方式，参数值缺省则默认为`utf-8`，也可以设定为其他[可用编码](https://docs.python.org/zh-cn/3/library/codecs.html#standard-encodings)  
                * errors  
                    设定`encode()`无法对字符串全部或部分进行解码时的处理方法，参数值缺省则默认方法是`strict`，即会引发`UnicodeError`错误，其他方法还包括`ignore`,`replace`,`xmlcharrefreplace`,`backslashreplace`，具体参见[错误处理方案](https://docs.python.org/zh-cn/3/library/codecs.html#error-handlers)  
                    * `ignore`  
                        对无法解码的部分进行忽略  
                    * `replace`  
                        无法解码的部分用`？`字符代替  
                    * `xmlcharrefreplace`  
                        对无法解码的部分用`XML`字符引用代替  
                    * `backslashreplace`  
                        无法解码的部分使用带`\`的转义序列进行替换  
                    * `namereplace`  
                        对无法解码的部分用`\N{...}` 转义序列进行替换  
            * 返回值  
                `byte`对象  
            * 逆方法  
                <a href = '#decode()'>`decode()`</a>
            * 备注  
                `byte`对象的形式为`b'编码'`，具体写法由所用的字符编码决定  
            | 字符  |   ASCII  |        gbk         |     UTF-8     |     UTF-16     |
            |  :-:  |    :-:   |        :-:         |      :-:      |       :-:      |
            |   A   |   b'A'   |        b'A'        |      b'A'     |b'\xff\xfeA\x00'|
            |   中  |   null   |    b'\xd6\xd0'     |b'\xe4\xb8\xad'|  b'\xff\xfe-N' |  
        * <a id = 'decode()'>[decode()方法](https://docs.python.org/zh-cn/3/library/stdtypes.html#bytes.decode)</a>  
            * 作用  
                `bytes`和`bytearray`对象的附加方法，返回从给定`bytes`解码出来的`str`。  
            * 方法定义  
                bytes.decode(encoding="utf-8", errors="strict")  
                bytearray.decode(encoding="utf-8", errors="strict")  
            * 参数  
                * encoding  
                    指定`byte`对象的编码方式，参数缺省则默认为`utf-8`，也可以指定其他[可用编码](https://docs.python.org/zh-cn/3/library/codecs.html#standard-encodings)  
                * errors  
                    设定`encode()`无法对字节串全部或部分进行编码时的处理方法，参数值缺省则默认方法是`strict`，即会引发`UnicodeError`错误。其他方法具体参见[错误处理方案](https://docs.python.org/zh-cn/3/library/codecs.html#error-handlers)  
            * 返回值  
                `str`  
            * 逆方法  
                <a href = '#encode()'>`encode()`</a>  
    * 占位符  
        * %  
            * 格式  
                '%[[-][+][0][width][.precision]type]' % (obj)  
                只有一处占位符时可以`obj`可以不加括号  
            * 参数  
                * \-  
                    左对齐，默认是右对齐  
                * \+  
                    正数默认显示`+`符号  
                * 0  
                    左侧空白位置补0  
                * width  
                    整个数据输出的位数，含小数点  
                * .precision  
                    对浮点数的作用是保留小数点后多少位  
                    对字符串的作用是最大字符大小，即最多显示多少位字符串的内容    
                * type  
                    用于指定占位符最后输出的字符类型  
                    * %s  
                        `%s`可以接受任何类型的对象，然后转为`str`，但`%-0a.bf`只能识别为`%-af`，即补0与`.precision`会失效  
                    * %d  
                        `%d`可以接受任何类型的数字对象，然后输出为十进制数字`str`，`float`对象会向`-inf`取整  
                    * %b  
                        `%b`可以接受任何类型的数字对象，然后输出为二进制数字`str`，`float`对象会向`-inf`取整再转二进制，结果不带进制前缀     
                    * %o  
                        `%o`可以接受任何类型的数字对象，然后输出为八进制数字`str`，`float`对象会向`-inf`取整再转八进制，结果不带进制前缀  
                    * %x  
                        `%x`可以接受任何类型的数字对象，然后输出为十六进制数字`str`，`float`对象会向`-inf`取整再转二进制，结果不带进制前缀  
                    * %f  
                        `%b`可以接受任何类型的数字对象，然后输出为浮点型数字`str`，不设置`.precision`参数则默认6位小数  
            * 备注  
                1.对`%`转义的方式为`%%`  
        * [format()方式](https://docs.python.org/zh-cn/3/library/string.html#format-string-syntax)  
            * 格式  
                '{[field_name][!conversion]:[:format_spec]}'.format()  
            * 参数  
                * field_name
                    * 作用  
                        将占位符指向一个参数  
                    * 格式  
                        arg_name("."attribute_name|"["element_index"]")*  
                    * 备注  
                        >1.`field_name`本身以一个数字或关键字`arg_name`打头。如果为数字，则它指向一个位置参数，而如果为关键字，则它指向一个命名关键字参数。  
                        2.如果格式字符串中的数字`arg_names`为0,1,2,... 的序列，它们可以全部省略（而非部分省略）。数字 0, 1, 2, ... 将会按顺序自动插入。  
                        3.由于`arg_name`不使用引号分隔，因此无法在格式字符串中指定任意的字典键 (例如字符串`'10'`或`':-]'`)。  
                        4.`arg_name`之后可以带上任意数量的`arg_name.attribute_name`索引或`arg_name[element_index]`属性表达式。    
                * conversion  
                    * 作用  
                        在`format()`方式对参数格式化之前对其转为字符串  
                    * 格式
                        !conversion
                    * 转换旗标类型  
                        * a  
                            调用`ascii()`转为`ASCII`字符  
                        * s  
                            调用`str()`转为`Unicode`编码的`str`字符串  
                        * r  
                            调用`repr()`  
                    * 备注  
                        `conversion`只对`type`为`s`的有效  
                * [format_spec](https://docs.python.org/zh-cn/3/library/string.html#formatspec)  
                    * 作用  
                    `format_spec`字段用于指定`format()`返回值呈现的规格  
                    * 格式  
                    :[[fill]align][sign][#][0][width][grouping_option][.precision][type]  
                    * 参数  
                        * fill  
                            * 作用  
                                `fill`参数用于接收一个字符作补位字符，不指定字符则默认是空格  
                            * 备注  
                                >1.仅当输出的字符串宽度小于`width`时才会进行补位  
                                2.仅当`align`是有效值时`fill`参数才会有效  
                                3.当指定了`fill`参数，则`width`前的`0`无效    
                        * align  
                            * 作用  
                                `align`参数用于指定对齐方式，考虑到`=`的情况，更精确的说法是指定`fill`和`0`参数的补位方式  
                            * 分类  
                                * <  
                                    强制字段在可用空间内左对齐，即在右侧补位  
                                    * 备注  
                                        这是大多数对象的默认值  
                                * \>  
                                    强制字段在可用空间内右对齐，即在左侧补位  
                                    * 备注  
                                        这是数字对象的默认值  
                                * =  
                                    强制将`fill`和`0`参数指定的补位字符填充在有效的`sign`参数和进制前缀之后但在数字之前  
                                    * 备注  
                                        >1.该方式仅对数字类型有效  
                                        2.当`0`参数有效时，它成为默认值  
                                * ^  
                                    强制字段在可用空间内居中对齐，即在两侧补位  
                        * sign  
                            * 作用  
                                `sign`参数用于指定数字对象前的符号，不指定参数值则默认是`-`  
                                * 分类  
                                    * \+  
                                        表示正数和负数前要加上`+`和`-`符号  
                                    * \-  
                                        表示只在负数前要加上`-`符号  
                                    * 空格  
                                        表示应在正数前使用前加空格，在负数上使用`-`  
                                        
                        * \#  
                            * 作用  
                                >1.对非十进制整数强制显示进制前缀  
                                2.对浮点数、复数、十进制整数强制显示小数点符号  
                            * 备注  
                                仅对数字对象有效  
                        * 0  
                            * 作用  
                                使用`0`来进行补位  
                            * 备注  
                                >1.仅当输出的字符串宽度小于`width`时才会进行补位  
                                2.当有`fill`参数，则`0`无效  
                                3.当指定了有效的`0`参数后，`align`的默认值为`=`，{:0d}等于{:0=d}  
                                4.由于当`type`为`s`类型时，不支持`=`类型的对齐方式，指定`0`参数后，必须手动把`align`改为其他值  
                        * width  
                            * 作用  
                                接收一个十进制整数，用于指定输出字符串的最小宽度，若没有指定则字段宽度将由`obj`确定  
                        * precision  
                            * 格式  
                                .precision  
                            * 作用  
                                接收一个十进制数字，然后根据对象的`type`差异作不同处理：  
                                >1.对于以`f`和`F`格式化的浮点数值要在小数点后显示多少个数位  
                                2.对于以`g`或`G`格式化的浮点数值要在小数点前后共显示多少个数位  
                                3.对于非数字类型，该字段表示最大字段大小，即要使用多少个来自字段内容的字符  
                            * 备注  
                                对于整数对象不允许使用precision  
                        * grouping_option  
                            * 作用  
                                对数字对象的每3位进行一次分割  
                            * 分类  
                                * ,  
                                * _  
                                    >1.对浮点表示类型和整数表示类型`d`使用下划线作为千位分隔符  
                                    2.对于整数表示类型`b`,`o`,`x`和`X`，将为每4个数位插入一个`_`  
                            * 备注  
                                对于其他表示类型指定千位分隔符则将导致错误  
                        * type  
                            * 作用  
                                确定数据应如何呈现  
                            * 分类  
                                具体参见[格式规格迷你语言](https://docs.python.org/zh-cn/3/library/string.html#format-specification-mini-language)的`type`参数部分  
                                  
                              
                                                                 