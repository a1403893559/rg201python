class 人类:
    def __init__(self, newLeg='黑色'):
        self.__皮肤 = newLeg
        self.鼻子 = '矮'

    def 输出Ta的外表(self):
        print(self.__皮肤)
        print(self.鼻子)

    def 修改韩方的皮肤颜色(self, newCoLor):

        self.__皮肤 = newCoLor

    def 读取韩方现在的皮肤颜色(self):
        return self.__皮肤

    def __del__(self):
        print('已经死了')


韩方 = 人类()
韩方.输出Ta的外表()
#韩方.__皮肤 = '白色'
韩方.鼻子 = '挺挺的'
print('中国失败整容后')
韩方.输出Ta的外表()
print('再次去韩国之路开始了')
韩方.修改韩方的皮肤颜色('白色')
韩方.输出Ta的外表()


韩方.读取韩方现在的皮肤颜色()

del 韩方
