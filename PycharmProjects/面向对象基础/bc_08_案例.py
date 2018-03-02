class Person:
    """人类"""

    def __init__(self, name, weight):
        # slef.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        # __str__方法必须返回一个字符串
        return "我的名字叫%s 体重 %.2f 公斤 " % (self.name, self.weight)

    def run(self):
        """跑步"""
        print("%s 爱跑步，跑步锻炼身体" % self.name)
        self.weight -= 0.5

    def eat(self):
        """吃东西"""
        print("%s 是吃货，吃完这顿在减肥" % self.name)
        self.weight += 1


xiaoming = Person("小明", 75)
xiaoming.run()
xiaoming.eat()
xiaoming.eat()
print(xiaoming)
