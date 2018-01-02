"""设计一个类：设计一个卖车的4S店"""
# # 1、定义类（车类、4S店类）
# class Car(object): # 基类（超类）
#     def move(self):
#         print('车--在移动')
#     def music(self):
#         print('车--放音乐')
#     def stop(self):
#         print('车--停车')

# # 2、销售车4s店的类
# class CarStroe(object):
#     def order(self):
#         self.car = Car()#找一辆车
#         return self.car


# buy_car = CarStroe()
# car = buy_car.order()
# car.move()
# car.music()
# car.stop()


# 假设我这个4S店类专门卖现代车
class 伊兰特车类(object):
    def 移动(self):
        print('移动')
    def 停止(self):
        print('停车')

class 索纳塔车类(object):
    def 移动(self):
        print('移动')
    def 停止(self):
        print('停车')

class 零售店类(object):
    def 提车(self,typeName):
        if typeName == '索纳塔':
            car = 索纳塔车类()
            return car
        elif typeName == '伊兰特':
            car = 伊兰特车类()
            return car
        
售车员 = 零售店类()
用户到手的车钥匙 = 售车员.提车('索纳塔')
用户到手的车钥匙.移动()
用户到手的车钥匙.停止()


        