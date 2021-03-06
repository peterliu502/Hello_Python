#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import codecs
import urllib.parse
print("ord()函数:")  # ord()函数
print('函数返回值数据类型:', type(ord('中')), sep='\n')  # ord()函数返回的是int类型
# 下面转完二进制之后需要在高位补0，补齐16位之后才是
print('函数二进制返回值:', bin(ord('中')), sep='\n')  # 汉字字符转十进制再转二进制
print(bin(ord('A')))  # ASCII字符转十进制再转二进制
print(bin(ord('1')))  # ASCII字符转十进制再转二进制
print(bin(1), end='\n\n')  # 字符1与数字1的区别，即ord('1')不等于1

print("chr()函数:")  # chr()函数
print('函数返回值数据类型:', type(chr(65)), sep='\n')  # chr()函数返回的是str类型
print(chr(65))  # 数字转ASCII字符
# 四种进制下的int转字符，结果是一样的
print(chr(20013))  # 十进制
print(chr(0b100111000101101))  # 二进制
print(chr(0x4e2d))  # 十六进制
print(chr(0o47055))  # 八进制
print('\u4e2d\u6587', end='\n\n')  # python可直接支持Unicode，直接在字符串中输入16进制的Unicode码即可输出字符

print("encode()函数：")  # encode()函数，作用是将python默认的Unicode编码解码为其他编码的字节串
# str.encode(encoding="utf-8", errors="strict")
print("65/'65'/b'65'的区别:")
print(type(65))  # int类型
print(type("65"))  # str类型，只有ASCII码字符时每个字符1字节，当字符串中有非ASCII码字符时1个字符2字节
# 和Unicode码有所区别，目前没有找到合理的解释，疑似字符串为纯ASCII字符时采用ASCII编码，而非Unicode编码，暂无验证方法
print(type(b"65"), end='\n\n')  # byte类型，1个字符1字节

print('转码测试:')
print('中文'.encode())  # encoding缺省则默认解码成utf-8编码
print('中文'.encode('gbk'))  # 汉字字符Unicode编码解码成gbk编码
print('中文'.encode('utf-8'))  # 汉字字符Unicode编码解码成utf-8编码
print('中文'.encode('utf-16'))  # 汉字字符Unicode编码解码成utf-16编码
print('123abc'.encode('gbk'))  # ASCII字符Unicode编码解码成gbk编码
print('123abc'.encode('utf-8'))  # ASCII字符Unicode编码解码成utf-8编码
print('123abc'.encode('utf-16'), end='\n\n')  # ASCII字符Unicode编码解码成utf-16编码
print('中'.encode('gbk'))  # 汉字字符Unicode编码解码成gbk编码
print('中'.encode('utf-8'))  # 汉字字符Unicode编码解码成utf-8编码
print('中'.encode('utf-16'))  # 汉字字符Unicode编码解码成utf-16编码
print('A'.encode('gbk'))  # 汉字字符Unicode编码解码成gbk编码
print('A'.encode('utf-8'))  # 汉字字符Unicode编码解码成utf-8编码
print('A'.encode('utf-16'), end='\n\n')  # 汉字字符Unicode编码解码成utf-16编码

print('errors处理:')
print('123中文'.encode(encoding='ascii', errors='ignore'))  # 对无法解码的部分进行忽略
print('123中文'.encode(encoding='ascii', errors='replace'))  # 对无法解码的部分用？代替
print('123中文'.encode(encoding='ascii', errors='xmlcharrefreplace'))  # 对无法解码的部分用XML字符引用代替
print('123中文'.encode(encoding='ascii', errors='backslashreplace'))  # 对无法解码的部分使用带反斜杠的转义序列进行替换
print('123中文'.encode(encoding='ascii', errors='namereplace'), end='\n\n')  # 对无法解码的部分用\N{...} 转义序列进行替换

print("decode()函数：")  # decode()函数，作用是将非Unicode编码的字节串编码为Unicode编码的字符串
# byte.decode(encoding="utf-8", errors="strict")
print('转码测试:')
print(b'\xd6\xd0\xce\xc4'.decode("gbk"))  # gbk编码成Unicode编码
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode("utf-8"))  # utf-8编码成Unicode编码
print(b'\xff\xfe-N\x87e'.decode("utf-16"), end='\n\n')  # utf-16编码成Unicode编码
print('errors测试:')
print(b'\xe4\xb8\xad\xe6\x96\x87\xff'.decode("utf-8", 'ignore'))  # 对无法编码的部分进行忽略
print(b'\xe4\xb8\xad\xe6\x96\x87\xff'.decode("utf-8", 'replace'))  # 对无法编码的部分用�代替
print(b'\xe4\xb8\xad\xe6\x96\x87\xff'.decode("utf-8", "backslashreplace"), end='\n\n')  # 对无法编码的部分用XML字符引用代替

print('url中乱码转Unicode字符')
print('方法1:codecs.escape_decode()')
str1 = '%E5%87%BD%E6%95%B0'
str2 = str1.replace('%', r'\x')
# print(str2)
bytes1 = str2.encode('utf-8')
# print(bytes1)
bytes2 = codecs.escape_decode(bytes1, 'hex-escape')
# 需要import codecs
print(bytes2[0].decode())

print('方法2:codecs.decode()')
str1 = '%E5%87%BD%E6%95%B0'
str2 = str1.replace('%', '')
# print(str2)
bytes1 = codecs.decode(str2, "hex")
# 需要import codecs
# print(bytes1)
str3 = bytes1.decode()
print(str3)

print('方法3:urllib.parse.unquote()')
str1 = '%E5%87%BD%E6%95%B0'
str2 = urllib.parse.unquote(str1)
# 需要import urllib.parse，光import urllib会引发错误
print(str2, end='\n\n')

print('占位符%测试')
# 格式 : %[- + 0 宽度.精度]类型码
# - : 左对齐(默认是右对齐)
# + : 显示正号
# 0 : 左侧空白位置补零
# 宽度 : 整个数据输出的最小宽度
# 精度 : 保留小数点后多少位
a = int('29a', 16)
print('a=%s b=%f c=%d d=%x e=%d f=%s g=%d h=%x i=%f' % (666, 666, 66.666, 666, 666, a, 0o1011, 0b1010, 0x1011))
# 所有占位符都可以接受变量参数
# %d %x %f对参数的类型与进制没有要求，会自动转换。其中%d会对float类型参数向-inf取整
# %s 可以将任何类型的变量转为str类型
print('%4d' % 1)  # %x表示补齐x位，默认状态下位数不够则在左侧用空格补齐，浮点数的小数点以及小数部分也占位数
print('%04d' % 1)  # %0x表示补齐x位，位数不够则在左侧用0补齐
print('%04d' % 123456)  # 原数字超出占位符设定的位数可以正常显示
print('%6.4d %2.4d' % (1, 1))  # %d中，因为整数不存在小数点，所以%a.bd（a>b）会被显示为a位数，其中右侧b位数会补0，b<a则等于%0bd。
print('%06.4d %02.4d' % (1, 1))  # %0a.bd若a>b则等于%0ad，否则等于%0bd。
print('%8.4f %2.4f' % (1, 1))  # %a.bf（a>b）会被显示为a位数（含小数与小数点），原数字位数不够则在左侧用空格补齐，其中b位小数，b<a则等于%bf。
print('%08.4f %02.4f' % (1, 1))  # %0a.bf（a>b）会被显示为a位数（含小数与小数点），原数字位数不够则在左侧用0补齐，其中b位小数，b<a则等于%0bf
print('%08.5s %-04s' % ('123.123', 1.0))
# %-0a.bs中，补位符0会失效，a表示字符最小宽度，b代表字符最大大小，即只显示接收的对象中的左起b位（因为是字符串类型，所以位数包含小数点）
print('%-04d' % 1)  # 左对齐模式下补0无效，补0只能在左侧补
print('%%f \%f' % 1, end='\n\n')  # 字符串中需要出现%，可以用%%转义，\转义则无效

print('format测试')
print('format测试:{0:@<+#10d}'.format(1234))  # <左对齐，右侧补位
print('format测试:{0:@>+#10d}'.format(1234))  # >右对齐，左侧补位
print('format测试:{0:@=+#10d}'.format(1234))  # =在前缀（正负号与进制前缀）与数字之间补位
print('format测试:{0:@^+#10d}'.format(1234))  # ^居中，两侧补位
print('format测试:二进制:{0:@^+#10b} 八进制:{1:@^+#10o} 十六进制:{2:@^+#10x}'
      .format(1234, 1234, 1234))  # 非十进制格式化
print('format测试:{0:@=+#10o}'.format(1234))  # 非十进制=对齐，在进制前缀的位置后面补位
print('format测试:{0:@=+10o}'.format(1234))  # #对非十进制整数会强制显示进制前缀
print('format测试:{0:@=+#10.0f}'.format(1234))  # #对浮点数会强制显示小数点
print('format测试:{0:@=+#10.3f} {1:@=+#10.2g} {2:@=+#10.3g} {3:@=+#10.4g} {4:@=+#10.5g} {5:@=+#10.6g}'
      .format(1234.5678, 1234.5678, 1234.5678, 1234.5678, 1234.5678, 1234.5678, 1234.5678))
# {:a.bg}中a表示最小宽度，b表示最大字符大小，即对obj左起显示多少位（不含小数点）
# 若b小于obj中小数点前的位数，则输出结果会采用科学计数法，科学计数法中的'e''+'以及表示幂的字符也占据宽度
print('format测试:{0:@=+#10.1e} {1:@=+#10.2e} {2:@=+#10.3e} {3:@=+#10.4e} {4:@=+#10.5e} {5:@=+#10.6e}'
      .format(1234.5678, 1234.5678, 1234.5678, 1234.5678, 1234.5678, 1234.5678, 1234.5678))
# {:a.be}中a表示最小宽度，b表示显示到系数小数点后多少位，科学计数法中的'e''+'以及表示幂的字符也占据宽度
print('format测试:{0:@<10.3s} {1:@<10.8s}'.format('123.123', '123.123'))
# {a.bs}中，a表示字符最小宽度，b代表字符最大大小，即只显示接收的对象中的左起b位（因为是字符串类型，所以位数包含小数点）
print('format测试:{0:@=+10,.1f}'.format(12345))  # ','作千位分隔符
print('format测试:{0:@=+10_.1f}'.format(12345))  # '_'作千位分隔符
print('format测试:{0:@=+10n}'.format(1_234.5))  # 使用{n}接收想要保留千位分隔符'_'的对象，换成其他类型会吞掉'_'
print('format测试:{!a:8s} {!a:s}'
      .format(123.4, '123\n爱你'))  # !a会将数字转ASCII字符。str中的ASCII字符不变，非ASCII字符转Unicode码，转义符无效
print('format测试:{!s:8s} {!s:s}'.format(123.4, '123\n爱你'))  # !s会将数字转str，str保持不变，转义符有效
print('format测试:{!r:s} {!r:s} {!r:s}'.format(123.4, '123\n爱你', a))  # !r会调用repr()
print('format测试:{!r:<0s}'.format(123.4))  # 启用width前的0时，必须指定一个非=的对齐方式，默认的=对齐方式会报错
print('format测试:{test1[0]!r:s} {test2.day!r:s}'
      .format(test1=range(1, 10), test2=datetime.datetime.now()), end='\n\n')  # 在field_name中使用参数索引与属性

print('作业:')
s1 = 72
s2 = 85
s3 = '小明今年成绩提高了'
print('方法一：%f')
print(s3 + '%4.1f%%' % (float((s2 - s1) / s1) * 100))
print('方法二：format()')
print(s3 + '{:4.1f}%'.format(float((s2 - s1) / s1) * 100))
print('方法二：format()变种')
print(s3 + '{:4.1%}'.format(float((s2 - s1) / s1)))
