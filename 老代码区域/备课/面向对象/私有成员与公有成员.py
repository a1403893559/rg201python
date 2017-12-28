#私有成员一般情况下外部不能直接访问 是在类的内部操作 或者在类的外部调用方法间接实现
class A:
    def __init__(self,value1 = 0,value2 = 0):#构造函数
        self._value = value1
        self.__value2 = value2
        