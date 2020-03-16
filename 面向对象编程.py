# 面向过程编程
# student信息用dict储存
stu1 = {'name':'Bob', 'score':90}
stu2 = {'name':'Mary', 'score':86}


# 打印student信息的功能用function完成
def print_score(stu):
    return '{:s}\'s score is {:d}'.format(stu['name'], stu['score'])


# 测试
print(print_score(stu1))
print(print_score(stu2))


# 面向对象编程
# 定义类
class Stu(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('{:s}\'s score is {:d}'.format(self.name, self.score))


# 创建实例
bart = Stu('Bart', 59)
lisa = Stu('Lisa', 87)
# 调用实例的方法
bart.print_score()
lisa.print_score()
