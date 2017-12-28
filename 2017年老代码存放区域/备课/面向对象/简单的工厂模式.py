"""
在之前的案例中，设计4S车店  遗留了一个问题  就是当
北京现代又产生一种新车类型的车时，又得在CarStore类
修改  所以这里引入一个新的概念  就是工厂方法
"""

# 定义伊兰特车类
class YilanteCar(object):
    
    # 定义车的方法
    def move(self):
        print('车在移动')
    def stop(self):
        print('停车')
    # 定义索纳塔车类
class SuonataCar(object):

        #定义车的方法
    def move(self):
        print('车在移动')
        
    def stop(self):
        print('停车')
 # 用来生成具体的对象
def craeteCar(typeName):
    if typeName == '伊兰特':
        car = YilanteCar()
    elif typeName == '索纳塔':
        car = SuonataCar()
    return car

# 定义一个销售北京现代车的店类
class CarStore(object):
    def order(self,typeName):
        #让工厂根据类型 生产一辆汽车
        car = craeteCar(typeName)
        return car

    