#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"

class Dog:
    def game(self):
        print("小狗和主任玩捡球的游戏")
class Wolfdog(Dog):
    def game(self):
        print("狼狗和主任玩跳绳的游戏")
class Xtq(Wolfdog):
    def game(self):
        print("哮天犬和主任玩飞行的游戏")

class Persion:
    def play_select(self,obj):
        obj.game()

dog1 = Dog()
wolfdog = Wolfdog()
xtq = Xtq()
p = Persion()
p.play_select(xtq)