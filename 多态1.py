#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"
# 子类和父类的方法名相同的情况下，重写 ，重写之后，默认调用的是子类的方法
# 如果想使用父类的方法
# 1父类名.方法名（self）
# 2 super(类名 ,self).方法名()  super函数会查询继承连中指定类的下一个类
# 3 super().方法名()   当前类的下一个类的方法
class Meat(object):
    def __init__(self):  #魔法方法__init__，都会被子类所继承
        self.name = "肉"
        self.weight = 2
class Ham(Meat):
    #pass
    def __init__(self):
        super().__init__()
        self.name = "火腿"
class Persion:
    def eat(self,obj):
        print("他喜欢吃%s" %obj.name)
rou = Meat()
print(rou.name)

huo = Ham()
print(huo.weight)
obj = Persion()
# obj.eat(huo)
obj.eat(huo)

# 使用父类的方法，也可以使用子类的方法