class 鸭子(动物类):
    def 走(self):
        print('我是一只鸭子,我可以横着走')
    def 游泳(self):
        print('我是一只鸭子，我会游泳')

class 人类(动物类):
    def 走(self):
        print('我是一个人，我可以直着走')
    def 游泳(self):
        print('我是一个人，我会游泳')

class 鱼类(动物类):
    def 走(self):
        print('我不会走')
    def 游泳(self):
        print('我会游')

class 动物类(object):
    def 走(self):
        pass
    def 游泳(self):
        pass