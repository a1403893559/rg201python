class Cat(object):
    def __init__(self, name, color='白色'):
        self.name = name
        self.color = color
        self.__eyes = '三只眼'

    def run(self):
        print('抓老鼠')

    def __kai(self):
        print('开天眼')

    def getEyes(self):
        return self.__eyes

    def eat(self):
        print('吃鱼')


class BosiCat(Cat):
    def swim(self):
        print('会游泳')


b = BosiCat('波斯猫', '红色')
b.run()
b.eat()
b.swim()
print(b.getEyes())
