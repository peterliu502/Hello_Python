# Hello_Python
***
## Description  
***
This repository is used to record my personal Python learning process.  
***
## List
### [![avatar](https://img.shields.io/badge/主题-hello%20world-red)](https://github.com/peterliu502/Hello_Python/blob/master/hello_world.py)  
***
#### __time__  
2020-01-07
#### __content__  
* 输出 __"hello，world!"__
    ```python
    print("hello，world!")
    ```
* 了解 ["#!/usr/bin/env python3"](https://www.jianshu.com/p/400c612381dd) 作用   
    * 含义  
        注释是为了告诉 `Linux` / `OS X` 系统，这是一个 `python3` 可执行程序，这在电脑上同时安装了 `python2` 和 `python3` 的时候尤其重要，
        因为 `python3` 不向下兼容。而 `Windows` 系统会忽略这个注释；  
    * env的作用  
        ```python
        #!/usr/bin/env python3 
        ```
        该代码表示从`PATH 环境变量`中查找 `python3` 解释器的位置, 路径没有被写死, 而是在`环境变量`中寻找 `python3` 解释器的安装路径, 
        再调用该路径下的解释器来执行脚本。  
       ```python
        #!/usr/bin/python3
        ```
        该代码表示 `python3` 解释器所处的绝对路径就是 `/usr/bin/python3`, 路径被写死了, 类似于编程中的`硬编码`。之所以有这种写法,
        是因为在`类 Unix` 系统中, python 解释器一般情况下都位于这个路径。不过, 如果碰到 python 解释器不在该路径下的话, 脚本就无法执行了。  
        
        显然, 采用第一种写法更灵活更具有通用性, 推荐使用这种写法。  
* 了解 <a id = '编码声明'>["## -\*- coding: utf-8 -\*-"](https://blog.csdn.net/zhongbeida_xue/article/details/81736671)</a> 作用  
    * 含义  
        如果没有此文件编码类型的声明，则 python2 默认以`ASCII`编码去处理；如果你没声明编码，但是文件中又包含非`ASCII`编码的字符的话，
        python解析器去解析的 python 文件，自然就会报错了。  
        必须放在python文件的第一行或第二行。   
        声明格式要符合[正则表达式](https://blog.csdn.net/xld_19920728/article/details/80534146)  
        ```python
        "__coding[:=]\s*([-\w.]+)__"
        ```
### [![avatar](https://img.shields.io/badge/主题-输入输出-red)](https://github.com/peterliu502/Hello_Python/blob/develop/输入输出.py)  
***
#### __time__  
2020-01-07
#### __content__
##### [![avatar](https://img.shields.io/badge/函数-print()-orange)](https://docs.python.org/zh-cn/3.8/library/functions.html#print)  
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
##### ![avatar](https://img.shields.io/badge/关键概念-转义符-yellowgreen)
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
        举例来说"abc\t"，就是在"abc"后面补上5个空格，凑齐8个字符。而"abcdefghijk\t"一共11个字符，已经超过了8个字符，
        但是不满足16个字符，所以\t的作用就是补上7个空格，补齐16个字符。  
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
        当字符串中同时存在`""`和`''`两种引号时，`r''`和`r""`都不太好用，建议单独转义。因为英文中的引号无前后之分，
        字符串中的引号必然会和真正的引号混在一起，使字符串异常。  
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
##### [![avatar](https://img.shields.io/badge/函数-input()-orange)](https://docs.python.org/zh-cn/3.8/library/functions.html#input)  
* 函数定义  
    input(prompt) 
* 参数
    * prompt  
        `input()`函数中可以输入一个`提示语`(`prompt`)，作为显示界面中提示用户输入的引导语；  
* 返回值  
    `input()`函数输出的是字符串类型。    
### [![avatar](https://img.shields.io/badge/主题-数据类型与变量-red)](https://github.com/peterliu502/Hello_Python/blob/master/数据类型与变量.py)
***
#### __time__  
2020-01-09
#### __content__
##### ![avatar](https://img.shields.io/badge/关键概念-数据类型-yellowgreen)
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
                `str(bytes, encoding, errors)` 等价于<a href = '#decode()'>`bytes.decode(encoding, errors)`</a>  
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
##### ![avatar](https://img.shields.io/badge/关键概念-变量-yellowgreen)
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
    1. 执行
    ```python
    a = 'ABC'
    ```
    解释器创建了字符串'ABC'和变量a，并把a指向'ABC'：  
    ![avatar](https://raw.githubusercontent.com/peterliu502/Hello_Python/master/resource/20200109_01/变量在内存中的表示方法1.png)  
    2. 执行
    ```python
    b = a
    ```
    解释器创建了变量b，并把b指向a指向的字符串'ABC'：  
    ![avatar](https://raw.githubusercontent.com/peterliu502/Hello_Python/master/resource/20200109_01/变量在内存中的表示方法2.png)  
    3. 执行
    ```python
    a = 'XYZ'
    ```
    解释器创建了字符串'XYZ'，并把a的指向改为'XYZ'，但b并没有更改：  
    ![avatar](https://raw.githubusercontent.com/peterliu502/Hello_Python/master/resource/20200109_01/变量在内存中的表示方法3.png)  
    4. 所以，最后打印变量b的结果自然是'ABC'了  
##### ![avatar](https://img.shields.io/badge/关键概念-常量-yellowgreen)  
所谓常量就是不能变的变量，比如常用的数学常数`π`就是一个常量。在`python`中，通常用全部大写的变量名表示常量：
```python
PI = 3. 14159265359
```
但事实上`PI`仍然是一个变量，`python`根本没有任何机制保证`PI`不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果一定要改变变量PI的值，并不会报错
##### ![avatar](https://img.shields.io/badge/关键概念-除法-yellowgreen)
* /除法  
    /除法计算结果是浮点数，即使是两个数恰好整除，结果也是浮点数。可参考以下代码：
    ```python
    print(9/3)
    print(10/3)
    print(9.0/3. 0)
    print(10.0/3. 0)
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
    print(9.0//3. 0)
    print(10.0//3. 0)
    ```
    因为//除法只取结果的整数部分，所以Python还提供一个余数运算，可以得到两个整数相除的余数：
    ```python
    print(9%3)
    print(10%3)
    ```
### [![avatar](https://img.shields.io/badge/主题-字符串与编码-red)](https://github.com/peterliu502/Hello_Python/blob/master/字符串与编码.py)
***
#### __time__  
2020-02-01
#### __content__           
##### ![avatar](https://img.shields.io/badge/关键概念-字符编码-yellowgreen)
* 字节  
    由于计算机只能处理二进制数字，所以所有的文本都必须转为数字才可以交由计算机处理。因此通常由8`比特`（`bit`）构成1个`字节`（`bytes`）
    ，也可以理解为为每1个字符都可以对应一个8位的二进制数字。  
    1个字节8比特可以表示`2^8`个数字（`0`-`255`），2个字节16比特可以表示`2^16`个数字（`0`-`65535`），4个字节32比特可以表示`2^32`个数字（`0`-`4294967295`）
* 几种常用编码
    * ASCII  
        全称`美国信息交换标准代码`。计算机最早由美国人发明，所以一开始设计编码时只考虑到了26个英文字母大小写、数字以及一些基本符号，
        合计127个字符。这个字符编码表就被称为`ASCII编码表`。  
        由于字符数没有超出8比特的表示范围（`256`），所以`ASCII`码用1个字节表示1个字符。而实际上，`ASCII`的字符数根本不需要8位数字，
        7位即可。所以首位数字一般默认为0，只有在一些`ASCII`码的变形编码上会将首位标为1，使之与原版`ASCII`码作区别。
    * Unicode  
        由于`ASCII`码没有包含非英语字符，所以后续又出现了许多包含非英语字符的编码，这些编码大多与`ASCII`码兼容  
        比如中文的`GB2312`编码，与`ASCII`码不同的是由于中文字符数量远大于英文字符，1个字节的范围不够表示所有字符，
        所以`GB2312`编码采用2字节构成1个字符。诸如此类的编码还有很多，比如日文的`Shift_JIS`编码，韩文的`Euc-kr`编码等等  
        但如果同时存在两种或以上语言的字符，采用任何一种编码都会出现乱码。针对这种情况，出现了将各种编码整合到一起的`Unicode`编码，
        该编码大多使用2字节构成一个字符，少部分字符需要4字节。目前大部分操作系统和编程语言都可以很好的支持`Unicode`。  
        无论是`Unicode`还是`UTF-16`，都是2字节起步，所以`ASCII`码需要补1个字节，即在前面补上`00000000`，凑齐16比特。  
    * UTF-8  
        由于`Unicode`中1个字符的字节数至少是`ASCII`码的2倍，这意味着`Unicode`所需的存储空间也至少是`ASCII`码的2倍。
        这使得文本基本以英文为主时，使用`Unicode`在存贮和传输上非常浪费。  
        而`UTF-8`码则解决了这个问题，`UTF-8`码是一种`可变长编码`。1个字符对应的字节数由1个到6个不等。`ASCII`码中的字符采用1个字节，
        与`ASCII`保持一致，大部分汉字采用3个字节，部分生僻字符采用4-6个字节。在以英文字符为主时可以节省大量空间。
* 几种常用编码对比  

    |  字符  |  ASCII  |      Unicode       |           UTF-8            |
    |  :-:  |    :-:   |        :-:         |            :-:             |
    |   A   | 01000001 | 00000000 01000001  |          01000001          |
    |   中  |     X    | 01001110 00101101  | 11100100 10111000 10101101 |  
     
    可以看出`ASCII`码中的字符在`UTF-8`中的编码并没有变化，这意味着一些只支持`ASCII`编码的软件与系统可以在`UTF-8`中较好的运行。  
    在计算机内存中默认使用`Unicode`编码，而数据传输和储存时考虑到存储体积更偏向于使用`UTF-8`编码，因此在日常计算机操作中经常涉及到几种字符编码的转换，具体可以参看以下2个例子：  
    1. 编辑`UTF-8`编码的TXT格式文档  
    ![avatar](https://raw.githubusercontent.com/peterliu502/Hello_Python/master/resource/20200201_01/浏览网页中的文本.png)  
    2. 浏览网页中的文本  
    ![avatar](https://raw.githubusercontent.com/peterliu502/Hello_Python/master/resource/20200201_01/编辑UTF-8编码的TXT格式文档.png)  
    很多网页的源码上会有类似`<meta charset="UTF-8" />`的信息，表示该网页正是用的`UTF-8`编码。  
* python中的默认编码  
    `python2`中默认编码是`ASCII`，所以在程序开头必须带上<a href = '#编码声明'>`## -*- coding: utf-8 -*-`</a>，以保证`utf-8`编码的字符可以正常显示。  
    `python3`则默认采用`Unicode`编码，具体来说就是默认用`utf-8`编码去读源代码文件，而`python`内存中运行中的`str`是`Unicode`编码  
    然而通过`getsizeof()`方法插看`str`内存大小发现，`str`中`ASCII`字符为1字节，非`ASCII`字符为2字节，
    这与`Unicode`编码中所有字符都为2字节的设计有所差别。推测是因为出于节约空间的考虑，并非完全默认使用`Unicode`编码，
    而是将`ASCII`字符都按`ASCII`编码进行储存，非`ASCII`字符前`2^16`个字符每个2字节，往后每个4字节   
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
##### 字符串  
* <a id = 'ord()'>[![avatar](https://img.shields.io/badge/函数-ord()-orange)](https://docs.python.org/zh-cn/3/library/functions.html#ord)</a>  
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
        >`ord()`只能接收`str`，所以注意`str`类型的'1'和`int`类型的1之间的区别
* <a id = 'chr()'>[![avatar](https://img.shields.io/badge/函数-chr()-orange)](https://docs.python.org/zh-cn/3/library/functions.html#chr)</a>  
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
        >1. `int`类型的四种进制整数对`chr()`来说没有区别，或者说这四种进制数对程序来说一般也没有区别。  
        >2. `python`可以直接支持`Unicode`编码，所以直接在`str`对象中输入`\u`+四位`Unicode`编码即可打印出字符  
* <a id = 'encode()'>[![avatar](https://img.shields.io/badge/方法-str.encode()-orange)](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.encode)</a>  
    * 作用  
        `str`类型的特殊方法，返回原字符串编码为字节串对象的版本。
    * 方法定义
        str.encode(encoding="utf-8", errors="strict")  
    * 参数  
        * encoding  
            设定`encode()`返回的字节串编码方式，参数值缺省则默认为`utf-8`，也可以设定为其他[可用编码](https://docs.python.org/zh-cn/3/library/codecs.html#standard-encodings)  
        * errors  
            设定`encode()`无法对字符串全部或部分进行解码时的处理方法，参数值缺省则默认方法是`strict`，即会引发`UnicodeError`错误，
            其他方法还包括`ignore`,`replace`,`xmlcharrefreplace`,`backslashreplace`，具体参见[错误处理方案](https://docs.python.org/zh-cn/3/library/codecs.html#error-handlers)  
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
        `bytes`对象  
    * 逆方法  
        <a href = '#decode()'>`decode()`</a>
    * 备注  
        >`bytes`对象的形式为`b'编码'`，具体写法由所用的字符编码决定  
        >| 字符  |   ASCII  |        gbk         |     UTF-8     |     UTF-16     |
        >|  :-:  |    :-:   |        :-:         |      :-:      |       :-:      |
        >|   A   |   b'A'   |        b'A'        |      b'A'     |b'\xff\xfeA\x00'|
        >|   中  |   null   |    b'\xd6\xd0'     |b'\xe4\xb8\xad'|  b'\xff\xfe-N' |  
* <a id = 'decode()'>[![avatar](https://img.shields.io/badge/方法-bytes.decode()-orange)](https://docs.python.org/zh-cn/3/library/stdtypes.html#bytes.decode)</a>  
    * 作用  
        `bytes`和`bytearray`对象的附加方法，返回从给定`bytes`解码出来的`str`。  
    * 方法定义  
        bytes.decode(encoding="utf-8", errors="strict")  
        bytearray.decode(encoding="utf-8", errors="strict")  
    * 参数  
        * encoding  
            指定`bytes`对象的编码方式，参数缺省则默认为`utf-8`，也可以指定其他[可用编码](https://docs.python.org/zh-cn/3/library/codecs.html#standard-encodings)  
        * errors  
            设定`encode()`无法对字节串全部或部分进行编码时的处理方法，参数值缺省则默认方法是`strict`，即会引发`UnicodeError`错误。
            其他方法具体参见[错误处理方案](https://docs.python.org/zh-cn/3/library/codecs.html#error-handlers)  
    * 返回值  
        `str`  
    * 逆方法  
        <a href = '#encode()'>`encode()`</a>  
* ![avatar](https://img.shields.io/badge/关键概念-占位符-yellowgreen)  
    * [printf风格的字符串格式化](https://docs.python.org/zh-cn/3/library/stdtypes.html#printf-style-string-formatting)  
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
                用于指定占位符最后输出的字符类型，更多类型参见`python`手册  
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
            >1. 对`%`转义的方式为`%%`  
    * [![avatar](https://img.shields.io/badge/方法-str.format()-orange)](https://docs.python.org/zh-cn/3/library/string.html#format-string-syntax)  
        * 格式  
            '{[field_name][!conversion]:[:format_spec]}'.format()  
        * 参数  
            * field_name
                * 作用  
                    将占位符指向一个参数  
                * 格式  
                    arg_name("."attribute_name|"["element_index"]")*  
                * 备注  
                    >1. `field_name`本身以一个数字或关键字`arg_name`打头。如果为数字，则它指向一个位置参数，而如果为关键字，则它指向一个命名关键字参数。  
                    >2. 如果格式字符串中的数字`arg_names`为0,1,2,... 的序列，它们可以全部省略（而非部分省略）。数字 0, 1, 2, ... 将会按顺序自动插入。  
                    >3. 由于`arg_name`不使用引号分隔，因此无法在格式字符串中指定任意的字典键 (例如字符串`'10'`或`':-]'`)。  
                    >4. `arg_name`之后可以带上任意数量的`arg_name.attribute_name`索引或`arg_name[element_index]`属性表达式。    
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
                    >`conversion`只对`type`为`s`的有效  
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
                            >1. 仅当输出的字符串宽度小于`width`时才会进行补位  
                            >2. 仅当`align`是有效值时`fill`参数才会有效  
                            >3. 当指定了`fill`参数，则`width`前的`0`无效    
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
                                    >1. 该方式仅对数字类型有效  
                                    >2. 当`0`参数有效时，它成为默认值  
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
                            >1. 对非十进制整数强制显示进制前缀  
                            >2. 对浮点数、复数、十进制整数强制显示小数点符号  
                        * 备注  
                            >仅对数字对象有效  
                    * 0  
                        * 作用  
                            使用`0`来进行补位  
                        * 备注  
                            >1. 仅当输出的字符串宽度小于`width`时才会进行补位  
                            >2. 当有`fill`参数，则`0`无效  
                            >3. 当指定了有效的`0`参数后，`align`的默认值为`=`，{:0d}等于{:0=d}  
                            >4. 由于当`type`为`s`类型时，不支持`=`类型的对齐方式，指定`0`参数后，必须手动把`align`改为其他值  
                    * width  
                        * 作用  
                            接收一个十进制整数，用于指定输出字符串的最小宽度，若没有指定则字段宽度将由`obj`确定  
                    * precision  
                        * 格式  
                            .precision  
                        * 作用  
                            接收一个十进制数字，然后根据对象的`type`差异作不同处理：  
                            >1. 对于以`f`和`F`格式化的浮点数值要在小数点后显示多少个数位  
                            >2. 对于以`g`或`G`格式化的浮点数值要在小数点前后共显示多少个数位  
                            >3. 对于非数字类型，该字段表示最大字段大小，即要使用多少个来自字段内容的字符  
                        * 备注  
                            >对于整数对象不允许使用precision  
                    * grouping_option  
                        * 作用  
                            对数字对象的每3位进行一次分割  
                        * 分类  
                            * ,  
                            * _  
                                >1. 对浮点表示类型和整数表示类型`d`使用下划线作为千位分隔符  
                                >2. 对于整数表示类型`b`,`o`,`x`和`X`，将为每4个数位插入一个`_`  
                        * 备注  
                            >对于其他表示类型指定千位分隔符则将导致错误  
                    * type  
                        * 作用  
                            确定数据应如何呈现  
                        * 分类  
                            具体参见[格式规格迷你语言](https://docs.python.org/zh-cn/3/library/string.html#format-specification-mini-language)的`type`参数部分  
### [![avatar](https://img.shields.io/badge/主题-list与tuple-red)](https://github.com/peterliu502/Hello_Python/blob/master/序列类型.py)                              
***
#### __time__  
2020-02-09
#### __content__           
##### [![avatar](https://img.shields.io/badge/关键概念-序列类型-yellowgreen)](https://docs.python.org/zh-cn/3/library/stdtypes.html#sequence-types-list-tuple-range)  
* 分类  
    * 可变序列类型  
        * [list(列表)](https://docs.python.org/zh-cn/3/library/stdtypes.html#lists)  
            * 定义  
                `list`(列表)是可变序列，通常用于存放同类项目的集合，但也支持存放不同类型的对象到一个`list`(列表)中  
            * 函数  
                * [![avatar](https://img.shields.io/badge/函数-list()-orange)](https://docs.python.org/zh-cn/3/library/stdtypes.html#list)  
                    * 格式  
                        list([iterable])  
                    * 参数  
                        * iterable  
                            其中的项与`iterable`中的项具有相同的的值与顺序。`iterable`可以`list`、支持迭代的容器或其它可迭代对象。  
                            如果`iterable`已经是一个`list`对象，将创建并返回其副本，类似于`iterable[:]`(即浅拷贝)。  
                            如果`iterable`没有给出参数，构造器将创建一个空列表`[]`。  
            * 方法  
                * [![avatar](https://img.shields.io/badge/方法-list.sort()-orange)](https://docs.python.org/zh-cn/3/library/stdtypes.html#list.sort)  
                    * 格式  
                        sort(*, key=None, reverse=False)  
                    * 参数  
                        * key  
                            `key`参数可以接收一个函数，该函数必须可以接收一个参数并返回一个值，`list`对象中的元素会依次输入该函数，并将返回值作为排序对象  
                            `list`对象自身不可以作`key`参数，但可以用深浅拷贝来做参数  
                            默认值`None`表示直接对列表项排序而不计算每一个单独的键  
                        * reverse  
                            `reverse`为一个布尔值。如果设为`True`，则每个列表元素将按反向顺序比较进行排序。默认为`False`  
                    * 备注  
                        >1. 此方法会原地修改序列以保证空间经济性.此操作是通过间接影响进行的，它并不会返回排序后的序列  
                        >2. 如需要返回一个已排序列表对象，请使用<a href = '#sorted()'>`sorted()`</a>显示地请求一个新的已排序列表  
                        >3. `sort()`方法确保是稳定的。如果一个排序确保不会改变比较结果相等的元素的相对顺序就称其为稳定的，这有利于进行多重排序。  
            * [![avatar](https://img.shields.io/badge/关键概念-列表推导式-yellowgreen)](https://docs.python.org/zh-cn/3/faq/programming.html#how-do-i-create-a-multidimensional-list)  
                * 格式  
                    result = [obj.method() if …… else obj.method() for obj in mylist if ……]
                * 备注  
                    >1. `for in`前面也可以接一个`if else`表达式，按情况输出不同的`obj.method()` 
                    >2. `for in`后面接了`if`条件句，用于筛选可迭代对象中的元素    
    * 不可变序列类型      
        * [tuple(元组)](https://docs.python.org/zh-cn/3/library/stdtypes.html#tuples)  
            * 定义  
                `tuple`(元组)是不可变序列，通常用于储存异构数据的多项集（例如由`enumerate()`内置函数所产生的二元组）。  
                `tuple`也被用于需要同构数据的不可变序列的情况（例如允许存储到`set`或`dict`的实例）。  
            * 函数  
                *  [![avatar](https://img.shields.io/badge/函数-tuple()-orange)](https://docs.python.org/zh-cn/3/library/stdtypes.html#tuple)  
                    * 格式  
                        tuple([iterable])  
                    * 参数  
                        * iterable  
                            函数将构造一个元组，其中的项与`iterable`中的项具有相同的值与顺序。`iterable`可以是序列、支持迭代的容器或其他可迭代对象  
                            如果`iterable`已经是一个元组，会不加改变地将其返回。如果没有给出参数，构造器将创建一个空元组`()`。  
            * 备注  
                >1. 决定生成元组的其实是逗号而不是圆括号。圆括号只是可选的，生成空元组或需要避免语法歧义的情况除外  
                >2. 单元素元组的表示方法是`a,`或`(a,)`，而非`a`和`(a)`   
        * [range](https://docs.python.org/zh-cn/3/library/stdtypes.html#range)  
            * 定义  
                `range`类型表示不可变的数字序列，通常用于在`for`循环中循环指定的次数。  
            * 函数  
                * [![avatar](https://img.shields.io/badge/函数-range()-orange)](https://docs.python.org/zh-cn/3/library/stdtypes.html#ranges)  
                    * 格式  
                        [start = 0,] stop[, step = 1]  
                        * 参数  
                            * start  
                                设定`range`对象的起始值，参数缺省则默认从0开始  
                            * stop  
                                `range`对象值的上限，且不可以达到这个值  
                            * step  
                                `range`对象的步长，参数缺省则默认为1，如果`step`为0则会引发`ValueError`  
                        * 备注  
                            >1. 如果`step`为正值，确定`range`对象r内容的公式为`r[i] = start + step *i `其中`i >= 0`且`r[i] < stop`  
                            >2. 如果`step`为负值，确定`range`对象r内容的公式仍然为`r[i] = start + step * i`，但限制条件改为`i >= 0`且`r[i] > stop`  
                            >3. 如果`r[0]`不符合值的限制条件，则该`range`对象为空。  
                            >4. `range`对象虽然支持负索引，但是会将其解读为从正索引所确定的序列的末尾开始索引。  
                            >5. 元素绝对值大于`sys.maxsize`的`range`对象是被允许的，但某些特性(例如`len()`)可能引发`OverflowError`  
                            >6. 使用`==`和`!=`检测`range`对象是否相等是将其作为序列来比较。也就是说，如果两个`range`对象表示相同的值序列就认为它们是相等的。
                            （请注意比较结果相等的两个`range`对象可能会具有不同的`start`,`stop`和`step`属性
                            例如:
                            >```python
                            >range(0) == range(2, 1, 3)
                            >range(0, 3, 2) == range(0, 4, 2)
                            >```  
* 三种类型区别  
    >1. `list`对象为可变类型对象，`tuple`和`range`为不可变类型对象  
    >2. `range`比`tuple`占用更少的内存，因为`range`总是占用固定数量的内存，不论其所表示的范围有多大（因为它只保存了`start`,`stop`和`step`值，
        并会根据需要计算具体单项或子范围的值）  
* 操作  
    * [序列类型通用操作](https://docs.python.org/zh-cn/3/library/stdtypes.html#common-sequence-operations)  
        * x in s  
            * 结果  
                如果s中的某项等于x则结果为`True`，否则为`False`  
            * 备注  
                >1. 对其他序列类型也适用，如`str`、`bytes`、`btyearray`      
        * x not in s  
            * 结果  
                如果s中的某项等于x则结果为`False`，否则为`True`  
            * 备注  
                >1. 对其他序列类型也适用，如`str`、`bytes`、`btyearray`      
        * <a id = 's + t'>s + t</a>  
            * 结果  
                序列对象s与t拼接  
            * 备注  
                >1. s和t中有可变类型元素时会产生浅拷贝问题  
                >2. `range`不支持拼接操作  
                >3. s + t的拼接方式每次都会生成一个新对象，所以大批量处理时的效率比较低建议替换成别的方法  
                >>* 可变序列类型(list)  
                >>>* 替代方法    
                >>>>1. <a href = '#s.extend()'>s.extend()</a>  
                >>>>2. <a href = '#s += t'>s += t</a>  
                >>>>3. `for in`循环 + <a href = '#s.append()'>s.append()</a>
                >>>* 效率比较  
                >>>>`s = s + t` >>> `s.append()` > `s.extend()` = `s += t`        
                四种list拼接方法运行时间对比:  
                ![avatar](https://raw.githubusercontent.com/peterliu502/Hello_Python/master/resource/20200209_01/四种list拼接方法运行时间对比.png)  
                三种list拼接方法运行时间对比:  
                ![avatar](https://raw.githubusercontent.com/peterliu502/Hello_Python/master/resource/20200209_01/三种list拼接方法运行时间对比.png)  
                >>* 不可变序列类型  
                >>>* str                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                >>>>1. `str.join([str1, ...,strn])`  
                >>>>2. `io.StringIO`  
                >>>* bytes        
                >>>>1. `bytes.join([bytes1, ...,bytesn])`  
                >>>>2. `io.BytesIO`  
                >>>>3. 改用可变类型对象`bytearray`  
                >>>* tuple  
                >>>>1. 改用可变类型对象`list`
        * <a id = 's * n'>s * n</a>  
            * 结果  
                序列对象s的n次拼接  
            * 备注  
                >1. `range`对象不支持拼接操作  
                >2. `n <= 0`则识别为0，会返回一个和s同类型的空序列  
                >3. s中有可变类型元素时会产生浅拷贝问题  
        * s[i]  
            * 结果  
                s的i位置元素  
            * 备注  
                >1. i从0开始计算  
                >2. i为负数则索引顺序是相对于s的末尾。索引号会被替换为`len(s) + i`  
                >3. 但要注意不存在`s[len(s)]`，所以-0仍然为0  
        * s[i:j:k]  
            * 结果  
                s从i到j位置步长为k的切片，即所有满足`0 <= n < (j-i)/k`的索引号`x = i + n*k`的项(`x < j`)组成的序列  
            * 备注  
                >* 当k为正值时  
                >>1. 若i或j的值大于`len(s)`时，只能识别为`len(s)`  
                >>2. i与j须遵守`i <= j`, i或j为负数则索引顺序是相对于s的末尾，索引号需被替换为`len(s) + i`或`len(s) + j`进行判断大小，否则返回`[]`  
                >>3. `s.[i:i:1] = t`等价于<a id = 's.[i:i] = t'>`s.[i:i] = t`</a>（`0 <= i <= len(s)`）,表示在i位置插入序列t，
                     i为`len(s)`表示在序列最后插入  
                >>4. 当i或j的值缺省时，i默认为0，j默认为`len(s) - 1`  
                >* 当k为负值时    
                >>1. 若i或j的值大于`len(s) - 1`时，只能识别为`len(s) - 1`，所以k为负数时无法用`s.[len(s):len(s):k] = t`进行序列插入  
                >>2. i与j须遵守`i >= j`, i或j为负数则索引顺序是相对于s的末尾，索引号需被替换为`len(s) + i`或`len(s) + j`进行判断大小，否则返回`[]`  
                >>3. 当i或j的值缺省时，i默认为`len(s) - 1`，j默认为0   
                >* k不可为0，k值缺省或为None时默认为1  
        * len(s)  
            * 结果  
                s的长度  
        * max(s)  
            * 结果  
                s的最大项        
        * min(s)  
            * 结果  
                s的最小项  
        * s.index(x[, i[, j]])  
            * 结果  
                x在s中大于等于i且小于j的范围中首次出现的位置  
            * 备注  
                >1. 当x在s中找不到时`index`会引发`ValueError`  
                >2. 不是所有实现都支持传入额外参数i和j，但这两个参数允许高效地搜索序列的子序列，等价于`s[i:j].index(x)`  
                >3. 该操作不会复制任何数据，并且返回的索引是相对于序列的开头而非切片的开头                              
        * s.count(x)  
            * 结果  
                x在s中出现的总次数  
    * [可变序列类型操作](https://docs.python.org/zh-cn/3/library/stdtypes.html#mutable-sequence-types)  
        * s[i] = x  
            * 结果  
                s的第i项赋值为x  
        * s[i:j] = t
            * 结果  
                s从i到j位置的切片替换成可迭代对象t  
            * 备注      
                >1. <a id = 's[:] = []'>`s[:] = []`</a>表示清空s，等价于<a href = '#s.clear()'>`s.clear()`</a>和
                    <a href = '#del s[:]'>`del s[:]`</a>  
                >2. <a id = 's.[i:i] = t'>`s.[i:i] = t`</a>（`0 <= i <= len(s)`）,表示在i位置插入序列t，
                    i为`len(s)`表示在序列最后插入
        * del s[i:j]  
            * 结果  
                删除i到j位置的切片，等价于`s[i:j] = []`
            * 备注  
                >1. <a id = 'del s[:]'>`del s[:]`</a>表示清空s的元素，等价于<a href = '#s.clear()'>`s.clear()`</a>和
                    <a href = '#s.[:] = []'>`s.[:] = []`</a>  
                >2. `del s`表示删除整个s对象，要与`del s[:]`区别开来  
                >3. <a id = 'del s[i]'>`del s[i]`</a>表示删除i位置的元素    
        * s[i:j:k] = t  
            * 结果  
                所有满足`0 <= n < (j-i)/k`的索引号`x = i + n*k`的项(`x < j`)依次替换成t中的元素  
            * 备注  
                >1. 不同于`s[i:j] = t`的整段覆盖，`s[i:j:k] = t`中k绝对值不为1时，其元素是间隔排列的，所以不能直接整段替换成t，
                    必须严格遵循元素一一替换，因此要求`len(s[i:j:k]) == len(t)`  
        * s.append(x)  
            * 结果   
                在s末端插入x，等价于<a href = '#s[i:i] = t'>`s[len(s):len(s)] = [x]`</a>  
        * <a id = 's.clear()'>s.clear()</a>  
            * 结果   
                清除s中的所有项，等价于<a href = '#s[:] = []'>`s[:] = []`</a>和<a href = '#del s[:]'>`del s[:]`</a>  
            * 备注  
                >1. `s.clear()`是为了与不支持切片操作的可变容器(例如`dict`和`set`)的接口保持一致。 
        * s.copy()  
            * 结果  
                创建一个s的浅拷贝，等同于`copy.copy(s)`、`s[:]`和`list(s)`  
            * 备注  
                >1. `s.copy()`是为了与不支持切片操作的可变容器(例如`dict`和`set`)的接口保持一致。  
                >2. `copy()`不是`collections.abc.MutableSequence ABC`的一部分，但大多数具体的可变序列类都提供了它  
        * s.extend(t)或s += t  
            * 结果  
                s后面拼接上t，等价于<a href = '#s[i:i] = t'>`s[len(s):len(s)] = t`</a>  
            * 备注  
                >1. `s.extend(t)`和`s += t`的效率等同
                >2. 作用类似<a href = '#s + t'>`s + t`</a>，但区别是`s = s + t`会生成一个新对象而`s += t`不会，
                    所以在效率上`s += t`更优，关系类似`s = s * n`和`s *= n`    
                >3. `s = s + t`因为是生成新对象，所以可以应用于不可变类型序列，而`s += t`是对自身的修改，所以只有可变类型序列可以使用  
                >4. 要注意类似<a href = '#s + t'>`s + t`</a>，序列中的项不会被拷贝，它们会被多次引用。   
        * s *= n  
            * 结果  
                s的n次拼接
            * 备注  
                >1. 作用类似<a href = '#s * n'>`s * n`</a>，但区别是`s = s * n`会生成一个新对象而`s *= n`不会，
                    所以在效率上`s *= n`更优，关系类似`s = s + n`和`s += n`    
                >2. `s = s * n`因为是生成新对象，所以可以应用于不可变类型序列，而`s *= n`是对自身的修改，所以只有可变类型序列可以使用  
                >3. 要注意类似<a href = '#s * n'>`s * n`</a>，序列中的项不会被拷贝，它们会被多次引用。  
                >4. n值为一个整数，或是一个实现了`__index__()`的对象。n值为零或负数将清空序列     
        * s.insert(i, x)  
            * 结果  
                在s的i位置插入x元素  
            * 备注  
                >1. 等同于<a href = '#s[i:i] = t'>`s[i:i] = [x]`</a>  
        * s.pop(i)  
            * 结果  
                消除i位置的元素，并返回该元素的值  
            * 备注  
                >1. `s.pop(i)`的作用与<a href = '#del s[i]'>`del s[i]`</a>类似，但<a href = '#del s[i]'>`del s[i]`</a>没有返回值  
                >2. i缺省则默认为-1，即删除并返回最后一个元素  
        * s.remove(x)  
            * 结果  
                删除s中第一个值等于x的元素  
            * 备注  
                >1. 当在s中找不到x时`remove()`操作会引发`ValueError`                           
        * s.reverse()
            * 结果  
                就地将列表中的元素逆序  
            * 备注  
                >1. `s.reverse()`不是创建s的逆序副本，而是对s自身进行修改  
                >2. `s.reverse()`并不会返回反转后的序列  
### [![avatar](https://img.shields.io/badge/主题-浅拷贝与深拷贝-red)](https://github.com/peterliu502/Hello_Python/blob/master/浅拷贝与深拷贝.py)                        
***
#### __time__  
2020-02-12
#### __content__  
##### ![avatar](https://img.shields.io/badge/关键概念-赋值-yellowgreen)  
* 常用方法  
    `identifier = object`  
* 解释  
    使一个变量（官方称之为标识符（`identifier`））建立起与对象的引用  
* 备注  
    >1. 与`C`、`C++`等语言不同，变量（标识符）本身无类型，与之绑定的对象有类型  
    >2. `=`是赋值的关键，大部分情况下有无严格的`identifier =`可以区分操作是修改对象还是再赋值，
    比如`s = s + t`和`s += t`、`s = s * t`和`s *= t`、`s.expend(t)`和`s = s + t`  
    >>请看下面这个例子：  
    >>```python
    >>def func(m):
    >>    m[0] = 20
    >>    m = [4, 5, 6]
    >>    return m
    >>
    >>
    >>l = [1, 2, 3]
    >>func(l)
    >>print('l =', l)
    >>```
    >>l被赋值为`[1, 2, 3]`,所以在`func(l)`在传参时x也被赋值为`func(l)`，`m[0] = 20`将被引对象修改为`[20, 2, 3]`,
    l因为引用同一个对象所以也同步更新为`[20, 2, 3]`，而`m = [4, 5, 6]`则是对m的重新赋值，所以m和原list对象`[20, 2, 3]`脱离关系  
    因为l不受m的再次赋值的影响，所以最终的值为`[20, 2, 3]`  
    >3. 函数传参数就相当于对形参进行赋值，而非`C`、`C++`意义上的传值或传引用  
    >4. 赋值的过程如下面的代码与图片所示：  
    >```python
    >a = 1
    >print('a', a, id(a))
    >b = 2
    >print('b', b, id(b))
    >c = 1
    >print('c', c, id(c))
    ># 再次赋值
    >a = b
    >print('a', a, id(a))
    >```
    >```
    >输出结果：  
    >a 1 4301490544
    >b 2 4301490576
    >c 1 4301490544
    >a 2 4301490576
    >```  
    >![avatar](https://raw.githubusercontent.com/peterliu502/Hello_Python/master/resource/20200212_01/赋值.jpg)  
##### ![avatar](https://img.shields.io/badge/关键概念-浅拷贝-yellowgreen)  
* 常用方法  
    `import copy`  
    `copy.copy()`  
* 解释  
    浅拷贝生成的对象自身使用新的内存地址，而其一维元素和更高维的元素仍是被拷贝对象的引用  
* 备注  
    >1. 对于多维可变类型对象来说非常容易产生浅拷贝现象，比如拼接等操作  
    >2. 浅拷贝对象与被拷贝对象的关系示意图：  
    ![avatar](https://raw.githubusercontent.com/peterliu502/Hello_Python/master/resource/20200212_01/深浅拷贝1.jpg)  
##### ![avatar](https://img.shields.io/badge/关键概念-深拷贝-yellowgreen)  
* 常用方法  
    `import copy`  
    `copy.deepcopy()`  
* 解释  
    深拷贝生成的对象自身、一维元素和更高维的元素都使用新的内存地址  
* 备注  
    >* 当被引对象中存在多个项引用同一对象的情况，请参看下面的代码：  
    >>```python
    >>import deepcopy
    >>a = [3, 4]
    >>m = [1, 2, a, [5, a]]
    >>n = copy.deepcopy(m)
    >>n[3][1][0] = -1
    >>print(n)
    >>print(m)
    >>print(a)
    >>```
    >>```
    >>输出结果：
    >>[1, 2, [-1, 4], [5, [-1, 4]]]
    >>[1, 2, [3, 4], [5, [3, 4]]]
    >>[3, 4]
    >>```
    >>m中的a只是起到引用同一个`list`对象`[3, 4]`的作用，可以理解为a只是这个list对象的别名，他俩是绑定关系  
    `deepcopy()`对各层元素都会建立副本，所以`m[2]`和`m[3][1]`指向的都是list对象`[3, 4]`的副本，而非本体  
    所以`m[2]`和`m[3][1]`和原本的list对象`[3, 4]`以及a都没有关系了    
    >* 深拷贝对象与被拷贝对象的关系示意图：  
    ![avatar](https://raw.githubusercontent.com/peterliu502/Hello_Python/master/resource/20200212_01/深浅拷贝2.jpg)
### [![avatar](https://img.shields.io/badge/主题-if语句与循环语句-red)](https://github.com/peterliu502/Hello_Python/blob/master/if语句与循环语句.py)
***
#### __time__  
2020-02-20
#### __content__  
##### [![avatar](https://img.shields.io/badge/关键概念-条件判断语句-yellowgreen)](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#the-if-statement)
* 结构  
    ```python
    if a:
        do a1
    elif b:
        do b1
    else:
        do c1
    ```
* 说明  
    `if`语句通过对表达式逐个求值直至找到一个真值在子句体中选择唯一匹配的一个，然后执行该子句体的执行语句。而其他部分不会被执行或求值。
    如果所有表达式均为假值，且存在`else`子句体，就会执行`else`。 
* 备注  
    >1. if语句自上而下逐行运行，当判断语句为`True`时跳入当前分支的执行语句，后面的分支不再执行。因此各分支的判断范围必须彼此独立，
        或者范围逐渐扩大。
    >2. 判断语句必须以`:`结尾，执行语句必须缩进  
    >3. `elif`和`else`语句是可省略的  
    >4. 判断语句如果是非零数值、非空字符串、非空`list`等，就判断为`True`，否则为`False`  
##### ![avatar](https://img.shields.io/badge/关键概念-循环语句-yellowgreen)  
* 分类  
    * [for in循环](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#the-for-statement)  
        * 格式  
        ```python
        for i in s:
            do a
        else:
            do b    
        ```
        * 说明  
            将s中的元素依次赋值给i，每完成一次赋值循环一次。当完成s中元素的遍历后，如果存在else就执行else语句然后结束循环  
    * [while循环](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#the-while-statement)  
       * 格式  
        ```python
        while a:
            do a
        else:
            do b  
        ```
       * 说明  
           只要a为`True`就执行循环。当a判断为`False`时，如果存在else就执行else语句然后结束循环  
* 循环相关语法  
    * [break](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#break)  
        结束当前循环  
    * [continue](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#the-continue-statement)  
        跳过本次循环  
* 备注  
    >1. 循环语句的条件语句都要以`:`结尾，执行语句缩进  
    >2. `continue`和`break`一般都是配合`if`使用。但不可以滥用`break`和`continue`会造成代码执行逻辑分叉过多，容易出错。
         大多数循环并不需要用到`break`和`continue`语句，通常可以通过改写循环条件或者修改循环逻辑，去掉`break`和`continue`语句  
    >3. 出现死循环可以使用`ctrl + c`强制结束程序  
    >4. `else`语句可选  
### [![avatar](https://img.shields.io/badge/主题-dict与集合类型-red)](https://github.com/peterliu502/Hello_Python/blob/master/dict与集合类型.py)
***
#### __time__  
2020-02-21
#### __content__  
##### [dict(字典)](https://docs.python.org/zh-cn/3/library/stdtypes.html#mapping-types-dict)  
* 定义  
    字典是另一种采用`key-value`(键-值方法)储存可变容器模型，且可存储任意类型对象。  
    字典的每个键-值`key=>value`对用冒号`:`分割，每个键-值对之间用逗号`,`分割，整个字典包括在花括号`{}`中  
* 函数  
    [![avatar](https://img.shields.io/badge/函数-dict()-orange)](https://docs.python.org/zh-cn/3/library/stdtypes.html#mapping-types-dict)  
    * 格式  
        dict(**kwarg)  
        dict(mapping, **kwarg)  
        dict(iterable, **kwarg)  
    * 备注  
        >从函数的三种格式可知，`dict()`支持三种方式输入参数：
        >>1. 直接通过任意数量的关键词（`**kwarg`）参数传参，比如`dict(subject: Math, teacher: Jack, classroom: 401)`  
        >>2. 通过`map()`、`zip()`函数等可映射对象（`mapping`）传参，比如`dict(zip(list1, list2))`  
        >>3. 通过可迭代(`iterable`)对象传参，参数需要以可迭代的键-值对元组的形式输入，
             如`dict([(subject, Math), (teacher, Jack), (classroom, 401)])`  
        >>4. `mapping`传参可以和关键词传参方式混用，`iterable`传参也可以和关键词传参方式混用  
* 操作  
    * list(dict)  
        * 结果  
            将`dict`对象输入`list`构造器可以输出一个以`dict`的键为元素的`list`  
    * len(dict)  
        * 结果  
            返回`dict`对象中项的个数
    * dict[key]
        * 结果    
            返回`dict`中以`key`为键的项。 如果映射中不存在`key`则会引发`KeyError`  
    * dict[key] = value
        * 结果
            对键`key`的项，将其值设为`value`  
    * del dict  
        * 结果  
            删除`dict`对象  
    * del dict[key]  
        * 结果  
            删除`dict`对象键为`key`的项                          
    * dict.keys()  
        * 结果  
            返回以`dict`对象的键为元素的`list`对象  
    * dict.values()  
        * 结果  
            返回以`dict`对象的值为元素的`list`对象  
    * dict.items()  
        * 结果  
            返回以`dict`对象的键-值对元组为元素的`list`对象  
    * dict.copy()  
        * 结果  
            创建`dict`对象的浅拷贝  
    * dict.clear()  
        * 结果  
            清除`list`中的所有元素  
    * reversed(dict)  
        * 结果  
            返回一个以`dict`的键为元素逆序排列的`iterable`对象  
    * iter(dict)  
        * 结果  
            返回一个以`dict`的键为元素的`iterable`对象  
    * dict.fromkeys(seq[, value])
        * 结果  
            返回一个以`iterable`的`seq`参数为键，`value`参数为值的`dict`对象,所以与该方法绑定的`dict`对象没什么关系  
    * dict.get(key, default)  
        * 结果  
            `dict`中有`key`元素则返回`key`的值，没有则返回`default`，不会像`dict[key]`那样触发报错  
        * 备注  
            >1. `default`默认为`None`  
    * dict.pop(x)  
        * 结果  
            去除键为x的项，并返回该项的值  
    * dict.popitem()  
        * 结果  
            按照`LIFO`（先进后出）的顺序删去最后一项，并返回该键-值对元组  
    * dict.setdefault(x, default)  
        * 结果  
            如果存在键为x的对象则返回键的值，不存在则建立该键并赋值为`default`  
        * 备注  
            >1. `default`默认为`None`  
    * dict.update()  
        * 结果  
            使用`update()`的参数来更新`dict`，已存在的键会更新对应的值，不存在的键会直接建立并赋值  
        * 备注  
            >1. `dict`对象的常用拼接方法    
    * x (not) in dict  
        * 结果  
          （没）有键为x的项返回`True`，否则返回`False`  
* 字典推导式  
    * 格式  
        {key: value if …… else key: value for key, value in …… if ……}  
    * 备注  
        >1. `for in`后面要接一个元素为键-值对的可迭代对象，`value`和`key`分别对应键和值  
        >2. 也可以通过`zip()`函数缝合两个可迭代对象，在`for in`分别为`value`和`key`赋值
        >3. `for in`前面也可以接一个`if else`表达式，按情况输出不同的`value`和`key` 
        >4. `for in`后面接了`if`条件句，用于筛选可迭代对象中的元素  
        >5. `key: value`部分可以对键-值做一些运算，然后以运算结果作为最终的键-值  
* 备注  
    >1. `dict`对象的键几乎可以是任何值，除了非`hashable`的值，如列表、字典或其他可变类型的值。  
    >2. 数字类型用作键时遵循数字比较的一般规则：如果两个数值相等(例如1和1.0)则两者可以被用来索引同一字典条目（但是请注意，
        由于计算机对于浮点数存储的只是近似值，因此将其用作字典键是不明智的。）  
    >3. `dict`对象因为采用`key-value`(键-值方法)储存，查找和插入的速度极快，不会随着`key`的增加而变慢。但是需要占用大量的内存，
        内存浪费多  
    >4. 两个字典的比较当且仅当它们具有相同的键-值对时才会相等（不考虑顺序）。排序比较`<`,`<=`,`>=`,`>`会引发`TypeError`  
    >5. `dict`对会保留插入时的顺序。请注意对键的更新不会影响顺序。删除并再次添加的键将被插入到末尾  
##### [集合类型](https://docs.python.org/zh-cn/3/library/stdtypes.html#set-types-set-frozenset)  
* 定义  
    集合对象是由具有唯一性的`hashable`对象所组成的无序多项集  
    常见的用途包括成员检测、从序列中去除重复项以及数学中的集合类计算，例如交集、并集、差集与对称差集等  
* 分类  
    * set类型  
        * 定义  
            `set`类型是可变的,其内容可以使用`add()`和`remove()`这样的方法来改变。由于是可变类型，它是非`hashable`的，
            且不能被用作`dict`的`key`或其他集合对象的元素  
        * 函数  
            set([iterable])
            * 备注  
                >1. 想要创建一个空`set`对象必须借助其构造器函数，直接使用`{}`会被识别为`dict`对象  
                >2. 返回一个新的`set`对象，其元素来自于`iterable`。集合的元素必须为`hashable`  
                >3. 要表示由集合对象构成的`set`对象，所有的内层集合必须为`frozenset`对象。如果未指定`iterable`，则将返回一个新的空集合    
    * frozenset类型  
        * 定义  
            `frozenset`类型是不可变并且为`hashable`，其内容在被创建后不能再改变。因此它可以被用作`dict`的`key`或其他集合的元素  
        * 函数  
            frozenset([iterable])  
            * 备注  
                >1. 想要创建一个空`frozenset`对象必须借助其构造器函数，直接使用`{}`会被识别为`dict`对象  
                >2. 返回一个新的`frozenset`对象，其元素来自于`iterable`。集合的元素必须为`hashable`  
                >3. 要表示由集合对象构成的`frozenset`对象，所有的内层集合必须为`frozenset`对象。如果未指定`iterable`，
                    则将返回一个新的空集合    
* 操作  
    * 集合对象通用操作  
        * <a id = 'len(set)'>len(set)</a>  
            * 结果  
                返回集合对象中项的个数（即对象的基数）  
        * <a id = 'set.copy()'>set.copy()</a>  
            * 结果  
                返回集合对象的浅拷贝      
        * <a id = 'x in set'>x in set</a>  
            * 结果  
                如果集合对象中的某项等于`x`则结果为`True`，否则为`False`       
        * <a id = 'x not in set'>x not in set</a>  
            * 结果  
                如果集合对象中的某项等于`x`则结果为`False`，否则为`True`  
        * <a id = 'A.isdisjoint(B)'>A.isdisjoint(B)</a>  
            * 结果  
                验证`A`集合和`B`可迭代对象是否没有交集，没有则返回`True`，反之则`False`  
            * 备注  
                >1. `B`并不一定要集合对象，只要是可迭代对象即可，执行该方法的时候会将`B`隐性地转为集合对象进行比较    
        * <a id = 'A.issubset(B)'>A.issubset(B)</a>  
            * 结果  
                验证A集合是否是B可迭代对象的子集，等价于`set1 <= set2`  
            * 备注  
                >1. `B`并不一定要集合对象，只要是可迭代对象即可，执行该方法的时候会将`B`隐性地转为集合对象进行比较  
        * <a id = 'set1 <= set2'>set1 <= set2</a>  
            * 结果  
                验证集合`set1`是否是`set2`的子集，等价于`A.issubset(B)`  
            * 备注  
                >1. 受集合对象比较法则的约束，集合对象只可以和集合对象比较大小，`set`和`frozenset`可以互相比较，
                    这是与`A.issubset(B)`方法最大的区别  
        * <a id = 'set1 < set2'>set1 < set2</a>  
            * 结果  
                验证集合`set1`是否是`set2`的真子集，即`set <= other and set != other`  
            * 备注  
                >1. 受集合对象比较法则的约束，集合对象只可以和集合对象比较大小，`set`和`frozenset`可以互相比较          
        * A.issuperset(B)  
            * 结果  
                验证`A`集合是否是`B`可迭代对象的超集，等价于`set1 >= set2`  
            * 备注  
                >1. `B`并不一定要集合对象，只要是可迭代对象即可，执行该方法的时候会将`B`隐性地转为集合对象进行比较  
        * <a id = 'set1 >= set2'>set1 >= set2</a>  
            * 结果  
                验证集合`set1`是否是`set2`的超集，等价于`A.issuperset(B)`  
            * 备注  
                >1. 受集合对象比较法则的约束，集合对象只可以和集合对象比较大小，`set`和`frozenset`可以互相比较，
                    这是与`A.issuperset(B)`方法最大的区别  
        * <a id = 'set1 > set2'>set1 > set2</a>  
            * 结果  
                验证集合`set1`是否是`set2`的真超集，即`set >= other and set != other`  
            * 备注  
                >1. 受集合对象比较法则的约束，集合对象只可以和集合对象比较大小，`set`和`frozenset`可以互相比较     
        * <a id = 'A.union(B1, B2, ...,Bn)'>A.union(B1, B2, ...,Bn)</a>  
            * 结果  
                返回集合对象`A`和可迭代对象`B1-Bn`的并集  
            * 备注  
                >1. `B1-Bn`并不一定要集合对象，只要是可迭代对象即可，执行该方法的时候会将`B1-Bn`隐性地转为集合对象进行并集操作  
        * <a id = 'set1 | set2 | …… | setn'>set1 | set2 | …… | setn</a>  
            * 结果  
                返回集合对象`set1`到`setn`的并集  
            * 备注  
                >1. 受集合对象运算法则的约束，集合对象只可以和集合对象使用运算符运算，`set`和`frozenset`可以互相使用运算符运算，
                    这是与`A.union(B1, B2, ...,Bn)`方法最大的区别      
        * <a id = 'A.intersection(B1, B2, ...,Bn)'>A.intersection(B1, B2, ...,Bn)</a>  
            * 结果  
                返回集合对象`A`和可迭代对象`B1-Bn`的交集  
            * 备注  
                >1. `B1-Bn`并不一定要集合对象，只要是可迭代对象即可，执行该方法的时候会将`B1-Bn`隐性地转为集合对象进行交集操作  
        * <a id = 'set1 & set2 & …… & setn'>set1 & set2 & …… & setn</a>  
            * 结果  
                返回集合对象`set1`到`setn`的交集  
            * 备注  
                >1. 受集合对象运算法则的约束，集合对象只可以和集合对象使用运算符运算，`set`和`frozenset`可以互相使用运算符运算，
                    这是与`A.intersection(B1, B2, ...,Bn)`方法最大的区别  
        * <a id = 'A.difference(B1, B2, ...,Bn)'>A.difference(B1, B2, ...,Bn)</a>  
            * 结果  
                返回集合对象`A`和可迭代对象`B1-Bn`的差集  
            * 备注  
                >1. `B1-Bn`并不一定要集合对象，只要是可迭代对象即可，执行该方法的时候会将`B1-Bn`隐性地转为集合对象进行差集操作  
        * <a id = 'set1 - set2 - …… - setn'>set1 - set2 - …… - setn</a>  
            * 结果  
                返回集合对象`set1`到`setn`的差集  
            * 备注  
                >1. 受集合对象运算法则的约束，集合对象只可以和集合对象使用运算符运算，`set`和`frozenset`可以互相使用运算符运算，
                    这是与`A.difference(B1, B2, ...,Bn)`方法最大的区别  
        * <a id = 'A.symmetric_difference(B)'>A.symmetric_difference(B)</a>  
            * 结果  
                返回集合对象`A`和可迭代对象`B`的对称差集  
            * 备注  
                >1. `B`并不一定要集合对象，只要是可迭代对象即可，执行该方法的时候会将`B`隐性地转为集合对象进行对称差集操作  
        * <a id = 'set1 ^ set2 ^ …… ^ setn'>set1 ^ set2 ^ …… ^ setn</a>  
            * 结果  
                返回集合对象`set1`到`setn`的对称差集  
            * 备注  
                >1. 受集合对象运算法则的约束，集合对象只可以和集合对象使用运算符运算，`set`和`frozenset`可以互相使用运算符运算，
                    这是与`A.symmetric_difference(B1, B2, ...,Bn)`方法是不同的  
                >2. 该运算支持同时计算多个集合对象的对称差集，但是`A.symmetric_difference(B)`只支持两个对象求对称差集  
    * set类型操作  
        * A.add(x)  
            * 结果  
                在`set`对象A中插入x元素  
        * A.remove(x)  
            * 结果  
                `set`对象`A`中存在`x`元素则消除该元素，不存在则报错  
            * 备注  
                >1. `set.remove()`方法支持输入`set`对象，等同于同内容的`frozenset`对象  
        * A.discard(x)
            * 结果
                `set`对象`A`中存在`x`元素则消除该元素，不存在不会报错  
            * 备注  
                >1. `set.discard()`方法支持输入`set`对象，等同于同内容的`frozenset`对象  
        * A.pop()  
            * 结果  
                随机消除`set`对象中的一个元素（因为`set`对象中的元素没有顺序的概念） 
        * A.clear()  
            * 结果  
                清除`set`对象中所有的元素  
        * A.update(B1, B2, ...,Bn)  
            * 结果  
                `set`类型版的<a href = '#A.union(B1, B2, ...,Bn)'>`A.union(B1, B2, ...,Bn)`</a>，可直接对原对象进行修改  
            * 备注  
                >1. `B1-Bn`并不一定要集合对象，只要是可迭代对象即可，执行该方法的时候会将`B1-Bn`隐性地转为集合对象进行并集操作  
        * set1 |= set2 | …… | setn  
            * 结果  
                `set`类型版的<a href = '#set1 | set2 | …… | setn'>`set1 | set2 | …… | setn`</a>，可直接对原对象进行修改  
            * 备注  
                >1. 受集合对象运算法则的约束，集合对象只可以和集合对象使用运算符运算，`set`和`frozenset`可以互相使用运算符运算，
                    这是与`A.update(B1, B2, ...,Bn)`方法最大的区别      
        * A.intersection_update(B1, B2, ...,Bn)  
            * 结果  
                `set`类型版的<a href = '#A.intersection(B1, B2, ...,Bn)'>`A.intersection(B1, B2, ...,Bn)`</a>，可直接对原对象进行修改  
            * 备注  
                >1. `B1-Bn`并不一定要集合对象，只要是可迭代对象即可，执行该方法的时候会将`B1-Bn`隐性地转为集合对象进行交集操作  
        * set1 &= set2 & …… & setn  
            * 结果  
                `set`类型版的<a href = '#set1 & set2 & …… & setn'>`set1 & set2 & …… & setn`</a>，可直接对原对象进行修改  
            * 备注  
                >1. 受集合对象运算法则的约束，集合对象只可以和集合对象使用运算符运算，`set`和`frozenset`可以互相使用运算符运算，
                    这是与`A.intersection_update(B1, B2, ...,Bn)`方法最大的区别  
        * A.difference_update(B1, B2, ...,Bn)  
            * 结果  
                `set`类型版的<a href = '#A.difference(B1, B2, ...,Bn)'>`A.difference(B1, B2, ...,Bn)`</a>，可直接对原对象进行修改  
            * 备注  
                >1. `B1-Bn`并不一定要集合对象，只要是可迭代对象即可，执行该方法的时候会将`B1-Bn`隐性地转为集合对象进行差集操作  
        * set1 -= set2 | …… | setn  
            * 结果  
                `set`类型版的<a href = '#set1 - set2 - …… - setn'>`set1 - set2 - …… - setn`</a>，可直接对原对象进行修改  
            * 备注  
                >1. 受集合对象运算法则的约束，集合对象只可以和集合对象使用运算符运算，`set`和`frozenset`可以互相使用运算符运算，
                    这是与`A.difference_update(B1, B2, ...,Bn)`方法最大的区别  
                >2. 由于在运算符优先级中`-`高于`-=`,所以`set1 -= set2 - …… - setn`的写法是不行的，相当于`set1 -= (set2 - …… - setn)`，
                    所以要改为`set1 -= set2 | …… | setn`  
        * A.symmetric_difference_update(B)  
            * 结果  
                `set`类型版的<a href = '#A.symmetric_difference(B)'>`A.symmetric_difference(B)`</a>，可直接对原对象进行修改  
            * 备注  
                >1. `B`并不一定要集合对象，只要是可迭代对象即可，执行该方法的时候会将`B`隐性地转为集合对象进行对称差集操作  
        * set1 ^= set2 ^ …… ^ setn  
            * 结果  
                `set`类型版的<a href = '#set1 ^ set2 ^ …… ^ setn'>`set1 ^ set2 ^ …… ^ setn`</a>，可直接对原对象进行修改    
            * 备注  
                >1. 受集合对象运算法则的约束，集合对象只可以和集合对象使用运算符运算，`set`和`frozenset`可以互相使用运算符运算，
                    这是与`A.symmetric_difference_update(B1, B2, ...,Bn)`方法是不同的  
                >2. 该运算支持同时计算多个集合对象的对称差集，但是`A.symmetric_difference_update(B)`只支持两个对象求对称差集  
* 备注  
    >1. 作为一种无序的多项集，集合对象并不记录元素位置或插入顺序。相应地，集合不支持索引、切片或其他序列类对象的操作  
    >2. 集合对象是可遍历的，因此可以使用`for i in set/frozenset`这样的遍历语句  
    >3. 集合对象进行`|`/`|=`/`&`/`&=`/`-`/`-+`/`^`/`^=`等集合对象运算符操作时，如果参与运算的集合对象同时包括`set`和`frozenset`，
        则结果的类型取参与运算的第一个对象的类型  
    >4. `set`和`frozenset`均支持集合与集合的比较。两个集合当且仅当各为对方的子集时则相等。一个集合当且仅当其为另一个集合的真子集时则小于另一个集合。
         一个集合当且仅当其为另一个集合的真超集时则大于另一个集合  
    >5. `set`的实例与`frozenset`的实例之间基于它们的成员进行比较。例如`set('abc') == frozenset('abc')`返回`True``set('abc') in set([frozenset('abc')])`也一样  
    >6. 子集与相等比较并不能推广为完全排序函数。例如任意两个非空且不相交的集合不相等且互不为对方的子集，因此`a<b`、`a==b`或`a>b`比较均返回`False`  
    >7. 由于集合仅定义了部分排序（子集关系），因此由集合构成的列表`list.sort()`方法的输出并无定义  
### [![avatar](https://img.shields.io/badge/主题-函数定义与调用-red)](https://github.com/peterliu502/Hello_Python/blob/master/函数定义与调用.py)  
***
#### __time__  
2020-02-26
#### __content__  
##### [定义函数](https://github.com/peterliu502/Hello_Python/blob/master/函数定义与检查.py)  
* 格式
    * 规则    
        >1. 定义一个函数要使用`def`语句，依次写出函数名、括号`()`、括号中的参数和冒号`:`  
        >2. 然后，在缩进块中编写函数体  
        >3. 函数的返回值用`return`语句返回  
    * 结构示例  
        ```python
        # 前面空两行
        
        
        def 函数名(参数):
            函数体
        reture 返回值
        
        
        # 后面空两行
        ```  
    * 备注  
        >1. 函数体内部的语句在执行时，一旦执行到`return`时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑  
        >2. 函数如果没有`return`语句，函数执行完毕后也会返回结果，只是结果为`None`  
        >3. `return None`可以简写为`return`  
        >4. `return`多个值，会以`tuple`的形式返回  
        >5. 如果想定义一个什么事也不做的空函数，可以在函数体中用`pass`语句。`pass`也可以用来作为占位符，
            比如现在还没想好怎么写函数的代码，就可以先放一个`pass`，让代码能运行起来  
##### [检查参数](https://github.com/peterliu502/Hello_Python/blob/master/函数定义与检查.py)  
* 检查参数个数  
    调用函数时，如果参数个数不对，`Python`解释器会自动检查出来，并抛出`TypeError`  
* 检查参数类型  
    如果参数类型不对，`Python`解释器无法帮我们检查，必须自己设置报错机制。思路为`isintance()`+`raise`  
    * 报错设置方法  
        * [![avatar](https://img.shields.io/badge/函数-isinstance()-orange)](https://docs.python.org/zh-cn/3/library/functions.html#isinstance)  
            * 格式  
                isinstance(object, classinfo)  
            * 作用  
                如果参数`object`是参数`classinfo`的实例或者是其(直接、间接或虚拟)子类则返回`True`。如果`object`不是给定类型的对象，函数将总是返回`False`  
            * 备注  
                >1. 如果`classinfo`是类型对象元组（或由其他此类元组递归组成的元组），那么如果`object`是其中任何一个类型的实例就返回`True`  
                >2. 如果`classinfo`既不是类型，也不是类型元组或类型元组的元组，则将引发`TypeError`异常  
        * [![avatar](https://img.shields.io/badge/关键概念-raise-yellowgreen)](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#the-raise-statement)
            * 作用  
                `raise`可以显式地激活最近的一个异常，然后结束函数  
            * 格式  
                raise [expression [from expression]]  
            * 参数  
                * expression  
                    `raise`会将第一个`expression`求值为异常对象。它必须为`BaseException`的子类或实例  
                * from  
                    用于连接多个`expression`  
            * 备注  
                >1. 如果当前作用域内没有激活的异常，将会引发`RuntimeError`来提示错误  
                >2. 如果不带表达式，`raise`会重新引发当前作用域内最后一个激活的异常    
##### [调用函数](https://github.com/peterliu502/Hello_Python/blob/master/函数调用.py)  
* 本文件调用自定义函数  
    定义完自定义函数后就可以像内置函数一样直接使用  
* 跨文件使用自定义函数  
    * 方法
        >1. from filename import function
        >2. import function
    * 备注  
        >1. `filename`是指自定义函数所在文件的文件名，不含后缀
        >2. `function`只需要写函数名，不需要带`()`    
### [![avatar](https://img.shields.io/badge/主题-函数形参-red)](https://github.com/peterliu502/Hello_Python/blob/master/函数形参.py)  
***
#### __time__  
2020-02-28
#### __content__  
##### 形参类型  
* 必选参数 
    也可以理解为位置或关键词参数，是函数形参的默认形式，可以通过位置匹配或关键词匹配（`key`=`value`）两种方式赋值
    * 分类  
        * 位置参数  
            作为位置函数的实参是通过位置次序与定义函数时的位置形参进行匹配  
        * 关键词参数  
            作为关键词函数的实参通过关键词与同名关键词的形参进行匹配，无需遵循位置匹配规则  
        * 默认参数  
            必选参数的一种特殊形式，在定义函数时给参数设置了默认值，当调用函数时没有指定该参数的实参，则将该参数取默认值  
            默认参数可以有效地降低函数的调用难度    
    * 备注  
        >1. 必选参数部分如果实参混用位置参数与关键词参数，必须先写位置实参，且后面的关键词实参对应的形参不可以与位置实参冲突
        >2. 默认参数必须放在必选参数的最末尾  
        >3. 默认参数不可以赋为可变类型对象
* 可变参数
    可以接收任意数量的实参，分为可变位置参数与可变关键词参数  
    *分类  
        * 可变位置参数  
            可以接收任意数量的实参，所有参数会依次打包成一个元组  
        * 可变关键词参数  
            可以接收任意数量的关键词形式的实参（`key`=`value`），所有参数会依次打包成一个字典  
    * 备注  
        >1. 通过解包序列类型对象的方式(`*list` `*tuple`)给可变位置参数赋值，同理也可以用解包字典对象的方式(`**dict`)给可变关键词参数赋值  
        >2. 通过解包`dict`对象的方式给关键词参数赋值，传递的是深拷贝，函数内部修改并不会影响`dict`对象  
* 限定参数  
    限制了形参赋值方式的参数，分为仅限位置参数与仅限关键词参数  
    *分类  
        * 仅限位置参数  
            对应实参只能通过位置关系传参，通过插入一个`/`分隔符来将符号之前的形参设为仅限位置参数  
        * 仅限关键词参数  
            对应实参只能通过关键词传参，通过插入一个`*`分隔符来将符号之前的形参设为仅限位置参数  
    * 备注  
        >1. 当仅限关键词参数前面有一个可变位置参数时，可以不用加`*`分隔符，因为如果不强制使用关键词会被识别为可变位置参数的一部分，导致异常  
* 混合使用  
    以上几种形参类型均可混合使用，但定义时必须必须遵循以下顺序：  
    `仅限位置参数`-`必选参数`-`默认参数`-`可变位置参数`-`仅限关键词参数`-`可变关键词参数`  
    * 备注  
        >1. 其中前四种参数：`仅限位置参数`-`必选参数`-`默认参数`-`可变位置参数`都可以使用位置参数
            而后两种：`仅限关键词参数`-`可变关键词参数`必须使用关键词参数
            所以任何函数被调用时，无论函数是如何定义的都可以写成`func(*arg, **kw)`形式
            `*arg`实参和`**kw`实参分别给前四种形参和后两种形参赋值
        >2. 默认参数后接可变位置参数，其默认值是无效的，因为若默认参数省略则会把可变位置实参中的第一个元素识别为默认参数  
        >3. 必选参数如果后接可变位置参数，则不可以用关键词传参，因为违反了关键词参数必须在位置参数的后面的规则  
### [![avatar](https://img.shields.io/badge/主题-生成器与迭代器-red)](https://github.com/peterliu502/Hello_Python/blob/master/生成器与迭代器.py)  
***
#### __time__  
2020-03-02
#### __content__  
##### [![avatar](https://img.shields.io/badge/关键概念-生成器-yellowgreen)](https://docs.python.org/zh-cn/3/glossary.html#term-generator)  
* 解释  
    当出于内存等方面的考虑不希望一次性将`list`、`dict`和`str`等对象完整算出，只用在需要的时候给出下一个元素即可的时候。就可以将序列元素替换成对应的生成器（`generator`）  
* 生成方法  
    * [![avatar](https://img.shields.io/badge/关键概念-生成器表达式-yellowgreen)](https://docs.python.org/zh-cn/3/glossary.html#term-generator-expression)  
        * 定义  
            返回一个生成器迭代器的表达式       
        * 格式  
            (expression [if …… else expression] for …… in …… [if ……])
    * [![avatar](https://img.shields.io/badge/关键概念-生成器函数-yellowgreen)](https://docs.python.org/zh-cn/3/glossary.html#term-generator)                
        * 定义  
            返回一个`generator iterator`的函数。它看起来很像普通函数，不同点在于其包含`yield`表达式以便产生一系列值供给`for`循环使用或是通过`next()`函数逐一获取                                                                                                             
        * 备注  
            >1. `generator iterator`是`generator`函数所创建的对象。每个`yield`会临时暂停处理，记住当前位置执行状态
               （包括局部变量和挂起的`try`语句），而非像`return`一样直接中断。当该生成器迭代器恢复时，它会从离开位置继续执行（这与每次调用都从新开始的普通函数差别很大） 
            >2.  `yield`语句在语义上等同于`yield`表达式。`yield`语句可用来省略在使用等效的`yield`表达式语句时所必须的圆括号。
                 `yield`表达式和语句仅在定义`generator`函数时使用，并且仅被用于生成器函数的函数体内部。
                 在函数定义中使用`yield`就足以使得该定义创建的是生成器函数而非普通函数  
* 获取元素方法  
    * [![avatar](https://img.shields.io/badge/函数-next()-orange)](https://docs.python.org/zh-cn/3/library/functions.html#next)  
        * 格式  
            next(iterator[, default])
        * 作用  
            通过调用`iterator`的`__next__()`方法获取下一个元素。如果迭代器耗尽，则返回给定的`default`，如果没有默认值则触发`StopIteration`  
    * for in语句  
        * 格式  
            for elm in generator:  
        * 作用  
            因为`generator iterator`对象也是可以迭代的，所以也可以用`for in`语句的方法遍历`generator iterator`的元素，依次提取  
    * 备注  
        >1. `for in`方法比`next()`更常用  
        >2. 但如果生成器函数有返回值并想取出返回值，就只能用`next()`结合捕获`StopIteration`异常的办法  
##### [![avatar](https://img.shields.io/badge/关键概念-迭代器-yellowgreen)](https://docs.python.org/zh-cn/3/glossary.html#term-iterator)                  
* [![avatar](https://img.shields.io/badge/关键概念-可迭代对象-yellowgreen)](https://docs.python.org/zh-cn/3/glossary.html#term-iterable)  
    * 定义  
        `list`、`tuple`、`dict`、`set`、`str`、`generator`等可以直接作用于`for`循环的对象统称为可迭代对象(`Iterable`)  
    * 备注  
        >1. 可以使用`isinstance()`(需引入`collections`)判断一个对象是否是`Iterable`对象  
* [![avatar](https://img.shields.io/badge/关键概念-迭代器-yellowgreen)](https://docs.python.org/zh-cn/3/glossary.html#term-iterator)  
    * 定义  
        可以被`next()`函数调用并不断返回下一个值的对象(如`generator`)称为迭代器`Iterator`  
    * 备注  
        >1. 可以使用`isinstance()`(需引入`collections`)判断一个对象是否是`Iterator`对象  
        >2. `Iterable`对象可以通过`iter()`函数转为`Iterator`对象  
        >3. `for`循环和`next()`对象是可以等价转换的  
        >3. `Iterator`对象表示的是一个数据流，`Iterator`对象可以被`next()`函数调用并不断返回下一个数据，
            直到没有数据时抛出`StopIteration`错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
            只能不断通过`next()`函数实现按需计算下一个数据，所以`Iterator`的计算是惰性的，只有在需要返回下一个数据时它才会计算   
            `Iterator`甚至可以表示一个无限大的数据流，例如全体自然数。而使用`list`等类型是永远不可能存储全体自然数的  
### <a id = '高阶函数'>[![avatar](https://img.shields.io/badge/主题-高阶函数-red)](https://github.com/peterliu502/Hello_Python/blob/master/高阶函数.py)</a>    
***
#### __time__  
2020-03-06
#### __content__  
* 高阶函数  
    * 定义  
        接受函数为参数的函数，即为高阶函数（`Higher-order function`） 
    * 变量指向函数  
        将函数赋值给变量，变量便引用函数了。
        ```python
        function_abs = abs  # 将函数赋值给变量，变量便引用函数了
        print(function_abs(-1))  # 变量现在可以使用函数的功能了
        ```  
        函数名实质上也等同于指向函数的一个变量名.所以函数名也是可以被赋予其他值的（强烈不建议这么做），之后便不再能用该函数名调用函数了
        想在所有模块中都让某函数的指向改变，必须在使用`import`统一修改，格式为`import 函数所在模块; 函数所在模块.函数 = 自定义值`  
        ```python
        import builtins; builtins.abs = 10  # 修改abs变量的指向在其它模块也生效
        abs = 10  # 将abs函数名赋值为10
        ```
    * 与高阶函数相关的函数和方法  
        * [![avatar](https://img.shields.io/badge/函数-map()-orange)](https://docs.python.org/zh-cn/3/library/functions.html#map)  
            * 格式  
                map(function, iterable, ...)  
            * 参数  
                * function
                    `map()`调用的函数  
                * iterable  
                    为`function`提供实参的`iterable`对象  
            * 作用  
                返回一个将`function`应用于`iterable`中每一项并输出其结果的迭代器  
            * 备注  
                >1. 如果传入了额外的`iterable`参数，`function`必须接受相同个数的实参并被应用于从所有可迭代对象中并行获取的项  
                >2. 当有多个可迭代对象时，最短的可迭代对象耗尽则整个迭代就将结束  
        * [![avatar](https://img.shields.io/badge/方法-functools.reduce()-orange)](https://docs.python.org/zh-cn/3/library/functools.html#functools.reduce)  
            * 格式  
                将两个参数的`function`从左至右积累地应用到`iterable`的条目，以便将该可迭代对象缩减为单一的值。
                如果存在可选项`initializer`，它会被放在参与计算的可迭代对象的条目之前，并在可迭代对象为空时作为默认值。
                如果没有给出`initializer`并且`iterable`仅包含一个条目，则将返回第一项  
                ```python
                reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
                # 是计算 ((((1+2)+3)+4)+5) 的值
                # 左边的参数 x 是积累值而右边的参数 y 则是来自iterable的更新值。
                ``` 
            * 参数  
                * function
                    `map()`调用的函数  
                * iterable  
                    为`function`提供实参的`iterable`对象  
                * initializer  
                    首个实参的默认值  
        * [![avatar](https://img.shields.io/badge/函数-filter()-orange)](https://docs.python.org/zh-cn/3/library/functions.html#filter)  
            * 格式  
                filter(function, iterable)  
            * 参数  
                * function  
                    用于提供筛选标准的函数，返回值会被转为`True`/`False`
                * iterable  
                    提供待筛选对象的`iterable`
            * 作用  
                用`iterable`中函数`function`返回真的那些元素，构建一个新的迭代器。`iterable`可以是一个序列，
                一个支持迭代的容器，或一个迭代器。  
                如果`function`是`None`，则会假设它是一个身份函数，即直接用`iterable`中的元素值作为判断标准，
                所有返回假的元素（比如`0`、`False`、`None`、`[]`等）会被移除
            * 备注  
                >1. `filter(function, iterable)`相当于一个生成器表达式:
                ```python
                # function不是None的时候
                (item for item in iterable if function(item))
                # function是None的时候 
                (item for item in iterable if item)
                ```
        * <a id = 'sorted()'>[![avatar](https://img.shields.io/badge/函数-sorted()-orange)](https://docs.python.org/zh-cn/3/library/functions.html#sorted)</a>  
            * 格式  
                sorted(iterable, *, key=None, reverse=False)  
            * 参数  
                * iterable  
                    提供待排序的对象  
                * key  
                    通过引用一个函数来指定排序方法，即将`iterable`对象迭代进`key`函数中，然后对`key`的返回值进行排序  
                    为仅限关键字变量，默认为`None`(直接比较对象)  
                * reverse  
                    指定排序的顺序，`True`的话则进行逆序处理，为仅限关键字变量，默认为`False`
            * 备注  
                >1. 内置的`sorted()`确保是稳定的。如果一个排序确保不会改变比较结果相等的元素的相对顺序就称其为稳定的，
                    这有利于进行多重排序（例如先按部门、再按薪级排序）                  
### [![avatar](https://img.shields.io/badge/主题-返回函数-red)](https://github.com/peterliu502/Hello_Python/blob/master/返回函数.py)    
***
#### __time__  
2020-03-08
#### __content__
* 返回函数定义    
    指函数的返回值为一个函数，是<a href = '#高阶函数'>高阶函数</a>的一种用法  
* ![avatar](https://img.shields.io/badge/关键概念-闭包-yellowgreen)  
    当高阶函数返回一个内部函数时，这个内部函数可以引用外部高阶函数的参数和局部变量，可以保存下来一并返回，这种结构称之为闭包(`Closure`)  
    * ![avatar](https://img.shields.io/badge/关键概念-延迟绑定-yellowgreen)  
        因为闭包结构一般不会自动执行,所以会产生延迟绑定现象。具体来说就是返回函数中的所有变量都是以表达式的形式存在，没有与对象绑定。
        只有当函数被调用的时候才会开始将变量与对象绑定。  
        * 延迟绑定带来的问题  
            当变量为循环变量时延迟绑定就会出现问题：在返回函数的过程中高阶函数的循环语句已经在执行了，等到调用函数时循环语句已经结束了，
            所以循环变量只能绑定到循环语句中取到的最后一个值，示例代码如下：  
            ```python
            def count():
                fs = []
                for i in range(1, 4):
                    def f():
                        return i*i
                    fs.append(f)  # 注意append()的是i*i，而非1*1/2*2/3*3
                return fs
          
          
            f1, f2, f3 = count()
            # fs的值为[f, f, f],因为尚未被调用，所以三个f的返回值皆为i*i
            print(f1(), f2(), f3())
            # 调用f了，f内部各个变量开始绑定对象，而i此时为3，所以f1(), f2(), f3()皆为9(3*3)
            ```
        * 含循环语句的解决办法  
            切记返回闭包结构是不要包含循环变量或后续会变化的变量，很容易无法返回正常值。如果内部函数必须要包含循环变量，则可以在高阶函数内部再定义一个函数
            用于接收循环变量的值，将其转变为这个函数的局部变量，之后就不会受循环变量的影响了，参考下面代码：  
            ```python
            def count():
                def f(j):  # 定义一个用于接收循环变量i的函数
                    def g():
                        return j*j  # j已经是f的内部变量了，不受i变化的影响
                    return g  # 返回函数彼此独立，所以后面调用f时不会覆盖j值
                fs = []
                for i in range(1, 4):
                    fs.append(f(i)) # 调用f(i)，内部代码立刻被执行，因此i的当前值被传入f()
                return fs
            ```
* 备注  
    >* 高阶函数返回函数时，返回的不是函数的值，而是函数本身。因此这个函数是处于未执行状态，需要手动调用  
    ```python
    def return_func():  # 定义高阶函数
        def sec_func():  # 定义内部函数
            pass
        return sec_func  # 返回内部函数
  
  
    my_func = return_func()
    # 将return_func()的返回值，即sec_func()函数赋值给变量my_func
    # 但此时sec_func()并未被调用，所以不会执行sec_func()函数体
    my_func()  # 这里才是调用了sec_func()，开始执行sec_func()函数体
    ```
    >* 多次调用高阶返回函数，每个函数都是独立的，彼此互不影响.相当于返回内部函数的深拷贝  
    >* 闭包内的变量查找遵循<a href = '#LEGB规则'>LEGB规则</a>  
### [![avatar](https://img.shields.io/badge/主题-匿名函数-red)](https://github.com/peterliu502/Hello_Python/blob/master/匿名函数.py)    
***
#### __time__  
2020-03-08
#### __content__
* 含义  
    `Python`中也可以不用`def`关键字显性地定义函数，而改用匿名函数。在`Python`中，通过`lambda`关键字对匿名函数进行了有限支持  
* [![avatar](https://img.shields.io/badge/关键概念-lambda表达式-yellowgreen)](https://docs.python.org/zh-cn/3/reference/expressions.html#lambda)    
    * 含义  
        `lambda`表达式（有时称为`lambda`构型）被用于创建匿名函数。表达式会产生一个函数对象  
    * 格式  
        lambda *parameters: expression  
    * 参数  
        * parameters
            `lambda`的形参，可以接收多个参数  
        * expression  
            函数返回的表达式，一个`lambda`函数只能有一个表达式  
    * 备注  
        >* `lambda *parameters: expression`等价于以下代码：  
        ```python
        def <lambda>(parameters):
            return expression
        ```
        >* `lambda`函数同样可以赋值或作为高阶函数的参数或返回值  
        >* 高阶函数如果想返回`lambda`函数的返回值，可以表示为`return (lambda *parameters: expression)()` 
### [![avatar](https://img.shields.io/badge/主题-装饰器与偏函数-red)](https://github.com/peterliu502/Hello_Python/blob/master/装饰器与偏函数.py)    
***
#### __time__  
2020-03-11
#### __content__
##### [![avatar](https://img.shields.io/badge/关键概念-装饰器-yellowgreen)](https://docs.python.org/zh-cn/3/glossary.html#term-decorator)  
* 定义  
    装饰器(`decorator`)是指返回值为另一个函数的函数，通常使用`@wrapper`语法形式来进行函数变换。可以在不修改原函数的情况下，为原函数修补功能  
* 格式  
    * 自身不带参数的装饰器  
        ```python
        def decorator(func):  # 装饰器参数接收层
            def wrapper(*args, **kwargs):  # 目标函数参数接收层
                装饰器的执行语句  # 函数执行体
                return func(*args, **kwargs)  # 返回所接受的函数
        
       @decorator  # 将目标函数输入装饰器的语法糖
       def myfunc():
           return
       ```
       上文`@decorator`的语法糖等价于:
       ```python
       decorator(myfunc)
       ```
    * 自身带参数的装饰器  
        ```python
        def decorator(dcrt_para):  # 装饰器参数接收层
            def sub_decorator(func):  # 函数接收层
                def wrapper(*args, **kwargs):  # 目标函数参数接收层
                    装饰器的执行语句  # 函数执行体
                    return func(*args, **kwargs)  # 返回所接受的函数
                def wrapper
            def sub_decorator    
        
       @decorator(mypara)  # 将目标函数输入装饰器的语法糖，并输入装饰器参数
       def myfunc():
           return
       ```
       上文`@decorator`的语法糖等价于:
       ```python
       decorator(mypara)(myfunc)
       ```
* 备注  
    >1. 使用装饰器会把原函数的__name__属性也修改为`decorator`中的第二层函数的属性，这会导致后续无法正确使用该属性。
     所以应当使用`functools`模块中的`wraps`方法将该属性修正回来。`@function.wraps()`语句应放置在接收目标函数的那一层中:
     ```python
     def decorator(func):  # 装饰器参数接收层
         @function.wraps(func)  # 修正函数__name__属性
         def wrapper(*args, **kwargs):  # 目标函数参数接收层
              装饰器的执行语句  # 函数执行体
              return func(*args, **kwargs)  # 返回所接受的函数     
     ```
#####  [![avatar](https://img.shields.io/badge/关键概念-偏函数-yellowgreen)](https://docs.python.org/zh-cn/3/library/functools.html#functools.partial)  
* [![avatar](https://img.shields.io/badge/方法-functools.partial()-orange)](https://docs.python.org/zh-cn/3/library/functools.html#functools.partial)  
    `Python`中的偏函数(`Partial function`)功能主要是通过`functools.partial()`实现的  
    * 格式  
        functools.partial(func, /, *args, **keywords)  
    * 参数  
        * func  
            `func`是一个可调用对象或函数。对`partial`对象的调用将被转发给`func`并附带新的参数和关键字  
        * args  
            最左边的位置参数将放置在提供给`partial`对象调用的位置参数之前  
        * keywords  
            当调用`partial`对象时将要提供的关键字参数  
    * 定义  
        返回一个新的`partial`对象，当被调用时其行为类似于`func`附带位置参数`args`和关键字参数`keywords`被调用。
        如果为调用提供了更多的参数，它们会被附加到`args`。如果提供了额外的关键字参数，它们会扩展并重载`keywords`  
        `partial()`会被“冻结了”一部分函数参数和`/`或关键字的部分函数应用所使用，从而得到一个具有简化签名的新对象  
    * 备注  
        >1. `partial()`中`*args`,`**keywords`的赋值要遵循形参的顺序规则，比如对`func(a, b, c)`使用`partial(func, b=1)`，
            则形参c必须使用关键词赋值（因为位置参数不可以在关键词参数后面） 
        >2. `partial`对象与`function`对象的类似之处在于它们都是可调用、可弱引用的对象并可拥有属性。但两者也存在一些重要的区别。
            例如前者不会自动创建`__name__`和`__doc__`属性。而且，在类中定义的`partial`对象的行为类似于静态方法，
            并且不会在实例属性查找期间转换为绑定方法           
### [![avatar](https://img.shields.io/badge/主题-模块-red)](https://github.com/peterliu502/Hello_Python/blob/master/模块.py)    
***
#### __time__  
2020-03-15
#### __content__    
* [![avatar](https://img.shields.io/badge/关键概念-模块-yellowgreen)](https://docs.python.org/zh-cn/3/glossary.html#term-module)  
    在代码量很大的时候，处于可维护性等方面的考虑，需要将代码分类放置。这样的组织结构可以使得每个文件内的代码不会过多。  
    在`Python`中，是用后缀名为`.py`的文件作为分类存放代码的模块（`Module`），
    通过导入(`import`)的方法将代码串联起来，提高代码的可维护性与复用性。
    此外模块式的组织结构还可以避免同一命名空间内来自不同模块的同名属性(`attribute`函数、类等)冲突，
    可以通过各属性的模块前缀加以区别，例子如下:  
```python
    import numpy
    import math
    import scipy
    
    print(math.pi, 'from the math module') 
    print(numpy.pi, 'from the numpy package') 
    print(scipy.pi, 'from the scipy package')
```
    * 备注
        >1. 自定义的`attribute name`尽量不要与`python`内置`attribute name`重复
        >2. 自定义`attribute name`要遵循`python`命名规范  
* [![avatar](https://img.shields.io/badge/关键概念-包-yellowgreen)](https://docs.python.org/zh-cn/3/glossary.html#term-package)  
    `module`也可能会出现命名冲突的问题，因此需要借助包(`package`)来实现对module的管理。  
    具体来说就是将命名冲突的module放进不同的package当中。一个包的目录结构如下：
    ```
       mypackage
        ├─ __init__.py
        ├─ mymodule1.py
        └─ mymodule2.py 
    ```
    于是`mymodule1.py`的模块名变为了`mypackage.mymodule1.py`。
    通过`mypackage.`前缀与同名模块进行区分
    `package`也可以采用多级结构，可以在下面继续嵌套子包，
    下面的`web`就是`mymodule`的子包:
    ```
       mycompany
         ├─ web
         │  ├─ __init__.py
         │  ├─ utils.py
         │  └─ www.py
         ├─ __init__.py
         ├─ abc.py
         └─ utils.py
    ```
    总的来说引入`package`之后，只要顶层`package name`不重名，那就不会发生重名问题  
    * 备注
        >1. 自定义的`module name`尽量不要与`module name`内置属性名重复
        >2. 自定义`module name`要遵循`python`命名规范  
* __init__.py    
    * __init__.py的命名方式  
    `__init__.py`的模块名是它所在的`package`目录名，而非它自身的目录名+文件名。
    在`mycompany`这个`package`中`__init__.py`的`module name`不是`mycompany.__init__.py`而是`mycompany`。同理`web`中`__init__.py`的`module name`
    不是`mycompany.web.__init__.py`而是`mycompany.web`  
    * __init__.py的作用
        * 区别包与普通文件夹  
            `__init__.py`是区别`package`与普通文件夹的重要因素。
            即只有内含了一个名为`__init__.py`文件的文件夹，
            才能被`python`识别为`package`  
        * 批量导入包内模块  
            `__init__.py`内容可以为空，但也可以用来批量导入`package`内的`module`，
            * 批量导入方法  
                * 提前import进同级的__init__.py  
                    将本`package`中的`module`先`import`进同级的`__init__.py`,
                    然后只需`import`该`__init__.py`就可以将本`package`中的`module`全部引入  
                * 通配符法  
                    可以将`package`中的所有`module`以`list`形式赋值给·__init__.py·中的·__all__·属性。
                    `module name`必须作为`list`的`str`格式元素。
                    然后使用`from package[.subpackage] import *`方式一次性引入所有`module`  
* [![avatar](https://img.shields.io/badge/关键概念-import语句-yellowgreen)](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#grammar-token-import-stmt)  
    `import`主要用来导入`package`/`module`/`attribute`,可以拓展为`from import as`结构  
    * 具体句型  
        * import package[.subpackage].module  
            对于使用`import package[.subpackage].module`方式引入的`module`
            调用时必须按照`package[.subpackage].module.attribute`的格式
            整写出`module`与`attribute`的名字  
        * from package[.subpackage] import module  
            对于使用`from package[.subpackage] import module`方式引入`module`
            调用时只需写`module.attribute`即可，但这种方式遇到来自不同`package`的同名`module`时会触发命名空间冲突  
        * from package[.subpackage].module import attribute  
            对于使用`from package[.subpackage].module import attribute`方式引入`module`
            调用时可以直接用`attribute`调用，但是当来自不同`module`的`attribute`同名时也会触发命名空间冲突  
        * from package[.subpackage].module import attribute as alias  
            给引入的`attribute`起一个别名，然后就可以以这个别名来调用`attribute`  
            其他规则和`from package[.subpackage].module import attribute`类似              
        * from package[.subpackage] import module as alias  
            给引入的`module`起一个别名，然后就可以以这个别名来调用`module`  
            其他规则和`from package[.subpackage] import module`类似  
    * 备注 
        >1. 当`import`语句包含多个对象（由逗号分隔）时，每个对象将被分别执行，
         如同这些对象被分成独立的`import`语句一样  
        >2. `import`语句支持使用相对路径导入某一`module`或`package`的上级`package`，
        具体方法是在`module`或`package`前面加前缀`.`,没加一个代表回溯一级  
        ```python
           # 对于package1.package2.module而言：
           import .module == import package2
           import ..module == import package3
         ```
* [![avatar](https://img.shields.io/badge/关键概念-私有变量-yellowgreen)](https://docs.python.org/zh-cn/3/tutorial/classes.html#tut-private)  
    大多数`Python`代码都遵循这样一个约定：带有一个下划线的名称(例如`_spam`)应该被当作是`API`的私有(`private`)部分(无论它是函数、方法或是数据成员)。
    这应当被视为一个实现细节，可能不经通知即加以改变  
    * 备注  
        >1. 需要注意的是，仅限从一个对象内部访问的“私有”实例变量在`Python`中并不存在。即`Python`没有任何机制可以保证私有变量无法被外部掉用  
### [![avatar](https://img.shields.io/badge/主题-面向对象编程-red)](https://github.com/peterliu502/Hello_Python/blob/master/面向对象编程.py)   
***
#### __time__  
2020-03-16
#### __content__  
##### ![avatar](https://img.shields.io/badge/关键概念-面向过程编程-yellowgreen)  
面向过程的程序设计(`Procedure-Oriented Programming`，简称为`POP`)把计算机程序视为一系列的命令集合，即一组函数的顺序执行。
为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度  
##### ![avatar](https://img.shields.io/badge/关键概念-面向对象编程-yellowgreen)  
面向对象编程(`Object Oriented Programming`，简称`OOP`)，是一种程序设计思想。OOP把对象作为程序的基本单元，
一个对象包含了数据和操作数据的函数。面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，
并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递  
* [![avatar](https://img.shields.io/badge/关键概念-类-yellowgreen)](https://docs.python.org/zh-cn/3/tutorial/classes.html#classes)  
在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（`Class`）的概念。
类提供了一种组合数据和功能的方法。创建一个新类意味着创建一个新的对象 类型，从而允许创建一个该类型的新实例(`Instance`)。
每个类的实例可以拥有保存自己状态的属性(`attribute`)。 一个类的实例也可以有改变自己状态的(定义在类中的)方法(`method`)   
    * [![avatar](https://img.shields.io/badge/关键概念-类对象-yellowgreen)](https://docs.python.org/zh-cn/3/tutorial/classes.html#class-objects)  
        * 定义类  
            
    * [![avatar](https://img.shields.io/badge/关键概念-实例对象-yellowgreen)](https://docs.python.org/zh-cn/3/tutorial/classes.html#instance-objects)  
    * [![avatar](https://img.shields.io/badge/关键概念-方法对象-yellowgreen)](https://docs.python.org/zh-cn/3/tutorial/classes.html#method-objects)  
    * 备注  
        >1. Class与Instance的关系：`Class`是一种抽象概念，比如我们定义的`Class`——`Student`，是指学生这个概念，
         而实例（`Instance`）则是一个个具体的`Student`，比如，`Bart Simpson`和`Lisa Simpson`是两个具体的`Student`。
         所以，面向对象的设计思想是抽象出`Class`，根据`Class`创建`Instance`  