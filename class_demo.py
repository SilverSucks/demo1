# @Time : 2020/11/22 14:36
# @Author : lkl

class Student:
    native = 'luohe'  # 籍贯
    def __init__(self, name, age):
        self.name = name    # self.name称为实体属性
        self.age = age

    # 实例方法
    def eat(self):
        print('在吃饭')
        pass
    # 静态方法
    @staticmethod
    def phone():
        print('198...')
        pass
    # 类方法
    @classmethod
    def name(cls):
        print('这是类方法...')
        pass
    pass

# 创建Student类的对象
stu = Student('lkl',19)
print(id(stu))  # 有没有开内存空间