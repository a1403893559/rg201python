# """设计一个卖车的4S店，该怎么做？"""
# # 定义车类
# class Car(object):
#     # 定义车的方法
#     def move(self):
#         print('移动')
    
#     def stop(self):
#         print('停车')
    
# # 定义一个销售车的店类
# class CarStore(object):

#     def order(self):
#         self.car = Car()# 找到一辆车
#         self.car.move()
#         self.car.stop()

#buy_car = CarStore()
#buy_car.order()
print('------------------------------------------------------------------------------------')


class BMW(object):
    def move(self):
        print('车在移动')
    def stop(self):
        print('停车')

class BC(object):
    def move(self):
        print('车在移动')
    def stop(self):
        print('停车')

class CarStore(object):

    def order(self,typeName):
        # 根据用户的不同需要，生成不同的类型的车
        if typeName == '宝马':
            car = BMW()
        elif typeName == '奔驰':
            car = BC()
        return car

buy_car = CarStore()
buy_car.order('宝马')