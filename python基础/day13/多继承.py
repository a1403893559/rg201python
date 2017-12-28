class Animal(object):
    def zu(self):
        print('我是老祖宗')


class Ma(Animal):
    def __init__(self):
        zi_G = '有'

    def fly(self):
        print('飞')

    def heihei(self):
        print('我会嘿嘿')

    def zu(self):
        print('我是新祖宗')


class Lv(Animal):
    def __init__(self):
        Mao = '有'

    def swim(self):
        print('游')

    def heihei(self):
        print('我会赫赫')


class LZ(Lv, Ma):
    def haha(self):
        print('我会哈哈')

    def heihei(self):
        print('大傻逼')


骡子 = LZ()
骡子.swim()
骡子.fly()
骡子.haha()
骡子.heihei()
骡子.zu()
