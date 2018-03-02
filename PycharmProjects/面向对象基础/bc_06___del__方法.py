class Cat:

    def __init__(self,new_name):
        self.name = new_name
        print("%s来了"%self.name)

    # 对象离开这个世界的时候调用 (不需要主动调用)
    def __del__(self):
        print("我去了%s"%self.name)

# Tom 是一个全局变量
tom = Cat("Tom")
print(tom.name)

del tom
print("-"*50)


