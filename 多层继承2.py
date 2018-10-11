#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"
class Animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")

class Dog(Animal):
    def bark(self):
        print("汪汪叫")

class XTQ(Dog):
    pass

dog1 = XTQ()
dog1.eat()
dog1.drink()
dog1.bark()

print(Dog.__mro__)#查看继承连