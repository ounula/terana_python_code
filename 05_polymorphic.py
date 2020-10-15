"""
多态
    重写：子类实现了与父类中相同的方法（方法名，参数），调用该方法时，实际执行的是子类的方法
        内置可重写函数：在python中，以双下划线开头、双下划线结尾的是系统定义的成员。
        __str__函数：将对象转换为字符串（对人友好）
        __repr__函数：将对象转换为字符串（解释器可识别）
"""


class Dog(object):  # 所有类均继承object类
    def __str__(self):  # 打印对象时用
        return "阿斯顿"

    def __repr__(self):  # 拷贝对象时用
        return f"Dog()"

    def __eq__(self, other):
        pass  # 重写 == 方法，满足使用python自带方法

    def __ne__(self, other):
        pass  # 重写 != 方法

    def __lt__(self, other):
        pass  # 重写 < 方法，自定义对象比较 , sort方法依赖

    def __le__(self, other):
        pass  # 重写 <= 方法

    def __gt__(self, other):
        pass  # 重写 > 方法

    def __ge__(self, other):
        pass  # 重写 >= 方法

    def __add__(self, other):
        pass  # 重写 + 方法

    def __mul__(self, other):
        pass  # 重写* 方法

    def __truediv__(self, other):
        pass  # 重写 / 方法

    def __floordiv__(self, other):
        pass  # 重写 // 方法


d01 = Dog()
d02 = eval(d01.__repr__())  # 将字符串作为代码执行

eval(input())  # 无所不能
