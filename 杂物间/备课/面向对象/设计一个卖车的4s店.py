# 设计一个卖车的4S店，该怎么做呢？
# 定义类
class Car(object):

# 定义车的方法
    def move(self):
        print('---车在移动----')
    def stop(slef):
        print('-----停车------')

# 定义一个销售车的店类
class CarStore(object):
    def order(self):
        self.car = Car()#找一辆车
        self.car.move()
        self.car.stop()

