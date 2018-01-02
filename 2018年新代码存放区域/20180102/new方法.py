class B(object):
    def move(self):
        print('走')


class A(B):

    def move(self):
        print('爬')
    
    def __init__(self):
        print('这是init方法')
    
    def __str__(self):
        print('这是一个__str__方法')
    
    def __del__(self):
        print('这是一个__del__方法')
    
    def __new__(cls):# 你要实例化的类
        # print('A:',id(A))
        # print('cls:',id(cls))
        # ret = B.__new__(cls)
        # return ret
        print('有一个新的飞机降临了')
        # print('这是new方法')
        

for i in range(1,10):
    a = A()

# a = A()
# a.move()
