class Person(object):

    def __init__(self,name,age,taste):
        self.name = name
        self._age = age
        self.__taste = taste

    def showperson(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    def _work(self):
        print('工作')

    def __away(self):
        print('away')


class Student(Person):

    def constrcution(self,name,age,taste):
        self.name = name
        self._age = age
        self.__taste = taste

    def showstudent(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    @staticmethod
    def testbug():
        _Bug.showbug()


class _Bug(object):
    @staticmethod
    def showbug():
        print('showbug')


if __name__ == '__main__':
    s1 = Student('李文浩',17,'football')
    s1.showperson()
    print('----------------')
    # 无法访问 __taste 导致报错
    # s1.showstudent()
    
    s1.constrcution('郭强',19,'basketball')
    s1.showperson()
    print('-----------------')
    
    s1.showstudent()
    
    print('-------------------')
    
    s1.testbug()

