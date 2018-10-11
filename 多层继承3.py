#!/usr/bin/pyenv  python
# -*- coding:utf-8 _*_
__author__ = "leon"

class Mp3:
    def music(self):
        print("听歌")
class Moto(Mp3):
    def tel(self):
        print("打电话")
class Apple(Moto):
    def game(self):
        print("打游戏")
a1 = Apple()
a1.music()
a1.tel()
a1.game()
