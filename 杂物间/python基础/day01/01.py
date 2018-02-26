import os


class Xrk:
    """docstring for xrk"""

    def __init__(self):
        #super(xrk, self).__init__()
        #self.arg = arg
        self.color = '红色'

    def act(self):
        print('放阳光')


xrk = Xrk()
xrk.name = '向日葵'
xrk.color = '绿色'
xrk.height = 150
print('%s颜色是%s，身高%d' % (xrk.name, xrk.color, xrk.height))
print(os.getcwd())
