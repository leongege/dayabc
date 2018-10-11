#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"
class Grandpa:
    def gets(self):
        print("money")
class Father(Grandpa):
    def fangzi(self):
        print("hours")
class Child(Father):
    pass

erzi = Child()
erzi.gets()
erzi.fangzi()

print(Child.__mro__)#查看继承连