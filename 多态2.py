#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"
class Car:
    def back(self):
        print("后退5步")

class Bus(Car):
    def back(self):
        print("后退两步")

class Persion:
    def command(self,obj):
        obj.back()

cars = Car()
buss = Bus()
p = Persion()
p.command(buss)

# 使用父类的方法，也可以使用子类的方法