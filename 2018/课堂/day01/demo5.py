class Person(object):

    def __init__(self,name,age,taste):
        self.name = name
        self._age = age
        self.__taste = taste

    def showPerson(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    def dowork(self):
        self._work()
        self.__away()

    def _work(self):
        print('工作')

    def __away(self):
        print('away')


class Student(Person):
    def construction(self,name,age,taste):
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

if __name__ =='__main__':
    s1 = Student('陈怀远',15,'woman')
    s1.showPerson()
    print('*'*20)
    #s1.showstudent()
    s1.construction('KJ',16,'py')
    s1.showstudent()
    s1.showPerson()
    print('-------------------')
    Student.testbug()

