"""
Animal类，动物的基本类型

属性包括
- name，动物的名字
- age，动物的年龄

方法
-make_sound()，打印出动物的叫声
-move（），打印出动物的移动方式

"""



class Animal:
        def __init__(self, name, age):
            self.name = name
            self.age = age
            
        def make_sound(self):
            print('{} is making sound'.format(self.name))
            
        def move(self):
            print('{} is moving'.format(self.name))
            
        def __str__(self):
            return 'Name: {}, Age: {}'.format(self.name, self.age)
