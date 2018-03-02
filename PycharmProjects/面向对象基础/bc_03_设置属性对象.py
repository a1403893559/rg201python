class Cat:
    def eat(self):
        print("小猫爱吃鱼"+self.name)

    def drink(self):
        print("小猫要喝水")

# 创建猫对象
tom = Cat()

# 可以使用 .属性名 利用赋值语句就可以了
tom.name = "Tom"

tom.eat()
tom.drink()
print(tom)

# 在创建一个猫对象
lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)

lazy_cat2 = lazy_cat
print(lazy_cat2)