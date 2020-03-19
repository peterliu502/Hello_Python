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
# 定义class
class Stu(object):
    # 使用class关键词定义class
    # 紧跟class的是类名ClassName,按规范需要首字母大写
    # 后面()内的是基类名BaseClassName，表明定义的这个class由哪个class派生/继承下来的
    # 如果没有合适的基类，就使用`object`类，这是所有class最终都会继承的class

    def __init__(self, name, score):
        # 形参的规则与普通函数相同
        # 为了发挥class作为创建instance的模板作用，可使用特殊method __init__，使得name和score attribute在instance创建时就要绑定
        # __init__ method的第一个参数必须是self，指代instance自身，后面是创建instance时创建的参数
        self.name = name
        # 意为将形参name接收到的对象赋值给instance(self)的name attribute
        self.score = score
        # 意为将形参score接收到的对象赋值给instance(self)的score attribute

    def print_score(self):
        # class的instance可以保留类的所有attribute数据，想要访问这些内部数据没必要专门在外部设计函数来访问它们
        # 可以直接在class的内部定义调用这些数据的函数，就可以尽可能地将这些数据限制在class内部，这称之为数据封装
        # 对数据和逻辑封装的好处在于调用很容易，但却不用知道内部实现的细节，可以当个黑盒使用
        # 这些封装数据的函数是和class本身是关联起来的，我们称之为class的method，或者说method就是与instance绑定的函数
        # 要定义一个method，除了第一个参数是self外，其他和普通函数一样
        # 要调用一个method，只需要在instance变量上直接调用
        # 除了self不用传递，其他参数正常传入，instance的attribute在method内可以通过self参数调用
        print('{:s}\'s score is {:d}'.format(self.name, self.score))


# 创建instance
lisa = Stu('Lisa', 79)
# 创建instance是通过类名+()实现的
# 将Stu class的instance赋值给变量bart
bart = Stu('Bart', 59)
# 但由于使用__init__ method，就不能传入空的参数了，所以name和score attribute必须在创建instance时直接绑定
# self参数不用传，Python解释器自己会把instance变量传进去
bart.age = 18
# 也可以自由地给一个instance变量绑定attribute，比如，给instance bart绑定一个没定义过的attribute age
# 和静态语言不同，Python允许对instance变量绑定任何数据
# 也就是说，对于两个instance变量，虽然它们都是同一个class的不同instance，但拥有的变量名称都可能不同
# 比如lisa instance就没有age这个attribute
print('bart.name =', bart.name)
print('bart.score =', bart.score)
print('bart.age =', bart.age)


# 调用instance的method
# 直接通过instance调用
bart.print_score()
lisa.print_score()


class Student(object):
    count = 0

    def __init__(self, name, score):
        Student.count += 1
        # 注意Student.attribute的值每次更新都会留在class里，下一次实例化直接赋予最新的值
        self.name = name
        # 而self.attribute只属于instance，class只提供模板作用
        # 即class每次实例化都会把所有数据copy一份给instance，但是instance接收到的参数不会传给class
        self.score = score


bart = Student('bart', 11)
print(bart.count)
bart = Student('bart', 11)
print(bart.count)
bart = Student('bart', 11)
print(bart.count)
bart = Student('bart', 11)
