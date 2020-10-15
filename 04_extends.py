"""
继承
    子类对象，可以调用父类方法和子类方法
数据的继承
    1、子类没有构造函数，可以直接使用父类的
    2、子类有构造函数，不使用父类的构造函数，若想使用父类的构造函数，需在子类的构造函数内加上super().__init__()
"""


class Person:
    pass


class Student(Person):
    pass


class Teacher(Person):
    pass


w = Student()
w02 = Teacher()
w03 = Person()

# isinstance (对象，类型)        判断对象与类型的关系
# 学生对象        是一种         学生类型
print(isinstance(w, Student))  # True
# 学生对象         是一种         人类型
print(isinstance(w, Person))  # True
# 学生对象        是一种         老师类型
print(isinstance(w, Teacher))  # False
# 人对象             是一种          学生类型
print(isinstance(w03, Student))  # False

# is subclass(类型，类型)         判断类型与类型的关系
# 学生类型          是一种         学生类型
print(issubclass(Student, Student))  # True
# 学生类型         是一种         人类型
print(issubclass(Student, Person))  # True
# 学生类型         是一种         老师类型
print(issubclass(Student, Teacher))  # False
# 人类型            是一种          学生类型
print(issubclass(Person, Student))  # False

# type      判断类型是否相同
# 学生对象的类型       是        学生类型
print(type(w) == Student)  # True
# 学生对象的类型       是        人类型
print(type(w) == Person)  # False
# 学生对象的类型       是       老师类型
print(type(w) == Teacher)  # False
# 人对象的类型          是        学生类型
print(type(w03) == Student)  # False


# example
class Animal:
    def __init__(self, age):
        self.age = age
        print(f'我{age}岁')

    def eat(self):
        print('吃')


class Dog(Animal):
    def __init__(self, type,age):
        self.type = type
        print(f'我的种类是{type}')
        super().__init__(age)

    def run(self):
        print('跑')


class Bird(Animal):
    def fly(self):
        print('飞')



