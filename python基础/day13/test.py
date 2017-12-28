class Dog:
    def __init__(self):
        self.name = '狗狗'

    def printName(self):

        print(self.name)

    def __str__(self):
        msg = '我的名字叫' + self.name
        return msg


surgar = Dog()
surgar.printName()
print(surgar)
