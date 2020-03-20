# 面向过程编程
# student信息用dict储存
stu1 = {'name': 'Bob', 'score': 90}
stu2 = {'name': 'Mary', 'score': 86}


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


# 继承
class PrimarySchoolStu(Stu):  # 继承自class Stu
    def hello(self):  # 在基类基础上增加新method也可以对基类的基础上进行修改
        return print('Hello, my name is {:s}. I\'m a primary school student.'.format(self.name))
        # 可以看到PrimarySchoolStu继承了Stu的attribute

    def print_score(self):  # 也可以直接在基类的基础上对method进行修改(本质上是替换了print_score的指代对象)
        print('Little {:s}\'s score is {:d}'.format(self.name, self.score))


Tom = PrimarySchoolStu('Tom', 80)
Tom.print_score()
# 继承了基类Stu的全部属性与方法
Tom.hello()
# 子类自己的方法


# 对象的类型判断
print(isinstance(Tom, PrimarySchoolStu))
print(isinstance(Tom, Stu))  # instance对象的类型既是直接派生它的class，同时也可以识别为它的任意基类(如果有的话)
print(isinstance(lisa, PrimarySchoolStu))
print(isinstance(lisa, Stu))  # 但是基类的instance对象类型不能被识别为它的subclass


# 多态
class Animal(object):
    def shout(self):
        pass


class Dog(Animal):
    def shout(self):
        return 'Wang Wang!'


class Cat(Animal):
    def shout(self):
        return 'Miao Miao!'


class Cow(Animal):
    def shout(self):
        return 'Mu Mu!'


def shout(animal: Animal):
    print(animal.shout())
    return


class Human(object):
    def shout(self):
        return 'Shut up!'


# 多态就是将class通过派生出不同的subclass（Animal->Dog/Cat/Cow）
# 实现同一个基类method在不同subclass上呈现不同形态的结果（Animal.shout->Dog.shout/Cat.shout/Cow.shout）
# 针对这一特性，当我们想设计对所有subclass适用的method时，只需考虑基类的数据情况(shout(animal))
# 而不用逐个对subclass进行适配，因为基类的操作会对其所有subclass兼容
# 后续基类继续产生新subclass时，只要确保method编写正确，不用管原来的代码是如何调用的，这些method仍会适用于新subclass
# 因此对于一个变量，我们只需要知道它是属于哪个class，无需确切地知道它是哪个subclass，只要method编写正确，就可以放心地调用
# 这样调用方只管调用，不用管细节
# 同时因为不同subclass间的同名method作用不同，所以可以实现一个接口不同效果
shout(Dog())
shout(Cat())
shout(Cow())

