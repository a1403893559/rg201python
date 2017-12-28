# 说明形式参数 什么是实际参数 形参  实参

def addOne(a):
    a = a + 1
    return a

a = 3
print('函数内部的a的值:',addOne(a))
print('函数外面的值:',a)
