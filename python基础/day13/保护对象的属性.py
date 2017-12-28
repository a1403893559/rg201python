class People:
    def __init__(self, name):
        self.__name = name
        self.age = 18

    def getName(self):
        return self.__name

    def setName(self, newName):
        if len(newName) >= 5:
            self.__name = newName
        else:
            print('error:名字的长度需要大于等于5')


xiaoming = People('jiumeimei')
print(xiaoming.getName())
print(xiaoming.age)
