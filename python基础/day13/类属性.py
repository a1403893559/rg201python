# class People(object):
# 	name = 'Tom' #公有属性
# 	__age = 12 #私有属性


# p = People()


# print(p.name)#正确
# print(People.name)#正确
# #print(p.__age) #错误，不能在类外通过实例化对象访问私有的属性
# #print(People.__age)#错误，不能在类外通过类对象访问私有类属性

class People(object):
	address = '山东' #类属性
	def __init__(self):
		self.name = 'XiaoWang'#实例属性
		self.age = 20#实例属性

p = People()
p.age = 12#实例属性 
print(p.address)#正确
print(p.name)#正确
print(p.age)#正确

print(People.address)#正确
#print(People.name)#错误
#print(People.age)#错误
