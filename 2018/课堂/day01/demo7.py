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
            print('error:不是整型数字')
    
    #money = property(getMoney,setMoney)



#m = Money()
#print(m.getMoney())
#m.setMoney(100)
#print(m.getMoney())
m = Money()
m.money =100
print(m.money)
