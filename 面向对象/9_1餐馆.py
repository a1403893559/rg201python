class Restaurant(object):
    def __init__(self):
        self.restaurant_name = '李氏连锁餐馆'  
        self.cuisine_type = '泰餐'
        self.number_served = 0
        
    
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print('正在营业中')
    
    def set_number_served(self,num):
        self.number_served = num
        print(self.number_served)
    
    def increment_number_served(self,num):
        self.number_served += num
        print('总人数为%d人'%self.number_served)


class IceCreamStand(Restaurant):
    def __init__(self):
        self.flavors = ['草莓','巧克力','榴莲']
    
    def show(self):
        print(self.flavors)


restaurant = Restaurant()
print(restaurant.restaurant_name,restaurant.cuisine_type)
print('-'*30)
restaurant.describe_restaurant()
restaurant.open_restaurant()
print('-'*30)
r2 = Restaurant()
r2.describe_restaurant()
print('-'*30)
r3 = Restaurant()
r3.describe_restaurant()
print('-'*30)
r4 = Restaurant()
r4.number_served = 5
print(r4.number_served)
r4.number_served =8
print(r4.number_served)
r4.set_number_served(7)
r4.increment_number_served(5)
r4.increment_number_served(1)


ice = IceCreamStand()
ice.show()
