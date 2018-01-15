"""property
1、装饰器
2、语法糖 sugur


"""

class Money(object):
    def __init__(self):
        self.__money = 0
    
    @property
    def money(self):
        return self.__money
    
    @money.setter
    def money(self,value):
        if isinstance(value,int):
            self.__money = value
        else:
            print('error:不是整数类型')
    
    #money = property(getMoney,setMoney)


m = Money()
#m.setMoney(100.5)
#print(m.getMoney())

m.money = 100.5
print(m.money)


