class People(object):
    country = 'china'

    # 类方法 classmethod来进修饰
    @classmethod
    def getCountry(cls):
        return cls.country

    @classmethod
    def setCountry(cls, country):
        cls.country = country


p = People()
print(p.getCountry())  # 可以通过实例引用
print(People.getCountry())  # 可以通过类对象引用
