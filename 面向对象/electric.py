class Battey(object):

    def __init__(self,r):
        self.range = r

    def upgrade_battery(self):
        if self.range != 85:
            self.range = 85
    def get_range(self):
        print('现在的电量为:%s'%self.range)
xxx = input('请输入当前电量')
b = Battey(xxx)
b.get_range()
b.upgrade_battery()
b.get_range()         