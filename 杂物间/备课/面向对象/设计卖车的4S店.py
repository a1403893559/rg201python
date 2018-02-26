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


# class BMW(object):
#     def move(self):
#         print('车在移动')
#     def stop(self):
#         print('停车')

# class BC(object):
#     def move(self):
#         print('车在移动')
#     def stop(self):
#         print('停车')

# class CarStore(object):

#     def order(self,typeName):
#         # 根据用户的不同需要，生成不同的类型的车
#         if typeName == '宝马':
#             car = BMW()
#         elif typeName == '奔驰':
#             car = BC()
#         return car

# buy_car = CarStore()
# buy_car.order('宝马')
print('-----------------------------------------------------------')

# 定义伊兰特车类
class YLTCar(object):
    
    #定义车的方法
    def move(self):
        print('车在移动')
    
    def stop(self):
        print('停车')
    
# 定义索纳塔车类
class SNTCar(object):
    
    #定义车的方法
    def move(self):
        print('车在移动')
    def stop(self):
        print('停车')

# 定义一个生产汽车的工厂 让其根据具体的订单生产车
class CarFactory(object):
    def createCar(typeName):
        if typeName == '伊兰特':
            car = YLTCar()
        elif typeName == '索纳塔':
            car = SNTCar()
        return car

# 定义一个销售北京现代车的店类
class CarStore(object):
    
    def __init__(self):
        self.carFactory = CarFactory()

    def order(self,typeName):
        car = self.carFactory.createCar(typeName)
        return car
