'''
函数：用来封装某一段功能代码的，一个函数我们尽可能的去只实现一个功能
函数的定义时 切记 圆括号  不能省略 圆括号里面是我们的参数列表  那么如果是多个参数我们需要使用  逗号隔开

'''
def printMax(a,b):
    '''函数的说明文档'''
    print('外界传进来的a=%d,b=%d'%(a,b))
    if a>b:
        print(a)
    else:
        #a = 5
        #b = 10
        #c = a#5  c=5
        #d = b#10 d=10
        #b = c
        #a = d
        a,b = b,a
        # print('a=',a)
        print('交换AB的值以后的')
        print('a=%d'%a)
        print('b=%d'%b)


printMax(5,10)




