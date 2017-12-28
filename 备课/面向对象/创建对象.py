'''通过一天的学习，我们知道什么是类，
什么是对象，简单的说类可以理解为一张图纸，然后我们拿着这张图纸给工人去生产
python中我们可以根据已经定义的类去创建一个个对象
'''
#1、定义一个类
class Car():
	#移动
	def move(self):
		print('车在奔跑')
	#鸣笛
	def toot(slef):
		print('车在鸣笛..嘟嘟')

#2、创建一个对象，并且变量BWM来保存他的引用
BMW = Car()
BMW.color = '黑色'
BMW.wheelNum = 4 # 轮子数量
BMW.move()
BMW.toot()
print(BMW.color)
print(BMW.wheelNum)
		