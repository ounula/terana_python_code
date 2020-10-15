"""
    封装设计思想
        需求：老张开车去东北

        类：承担行为
        对象：承担数据


        设计模式：
            1：初始化创建实例对象
            2：每次调用函数创建实例对象
            3：不创建实例对象
"""


class Person:
    def __init__(self, name=None):
        self.name = name
        # 方法2：初始化创建实例对象，只生成一辆车
        self.car = Car()

    def go_to(self, position):
        # 方法1：
        # Car().run()# 每次调用生成新的车实例
        print(f'{self.name}去{position}')
        self.car.run()

    def go_to_2(self, position, vehicle):
        # 方法3： 实例化作为参数传入
        print(f'{self.name}去{position}')
        vehicle.run()


class Car:
    def run(self):  # 实例方法
        print("正在行驶")
