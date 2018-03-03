class Person:
    def __init__(self):
        # 体重 weight:体重
        self.weight = 240
        # 名字
        self.name = "段金松"

    # 吃东西
    def eat(self):
        self.weight += 1
        print(self.name + "吃完以后：" + str(self.weight))

    # 跑步
    def run(self):
        self.weight -= 0.5
        print(self.name+"跑完以后:"+str(self.weight))

kj = Person()
kj.name = "康俊"
kj.weight = 100
kj.eat()
kj.eat()
kj.run()
kj.run()

