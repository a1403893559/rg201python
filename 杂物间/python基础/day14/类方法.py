class People(object):
    country = 'China'
    
    def __init__(self):
        self.name = '日本'

    @staticmethod
    def getCountry()
        return People.country

    @classmethod
    def getCountyr(cls):
        return cls.country

    def 走(self):
        print('走')

p = People()
People.getCountyr()

# print(People.走())

# print(People.getCountyr())

# p = People()
# print(p.getCountyr())


