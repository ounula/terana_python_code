"""
    封装
"""


# 读与写
# 快捷键：props
class MyClass:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 18 or value < 7:
            raise Exception("age error")
        self.__age = value


# 只读
# 快捷键：prop
class MyClass02:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age


# 只写
class MyClass03:
    def __init__(self, age):
        self.age = age

    age = property()

    @age.setter
    def age(self, value):
        self.__age = value


if __name__ == '__main__':
    w01 = MyClass03(8)
    print(w01.__dict__)
