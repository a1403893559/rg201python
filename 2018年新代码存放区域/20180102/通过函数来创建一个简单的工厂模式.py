class CarStore(object):
    def __init__(self):
        self.car = CarFactory()

    def buy_car(self,typeName):
        self.car = self.car.zao_che(typeName)
        return self.car        
# 提车
class CarFactory():
    def zao_che(self,typeName):
        if typeName == 'YLT':
            car = YLTCar()
            return car
        elif typeName == 'STN':
            car = STNCar()
            return car

class YLTCar(object):
    def move(self):
        print('车移动')

class STNCar(object):
    def move(self):
        print('车移动')

a = CarStore()
b = a.buy_car('YLT')
b.move()
