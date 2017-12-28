'''
思考一个问题
现在需要定义一个函数 这个函数能够完成2个数的加法运算   我们需要怎么设计?

'''


def addsum(a,b):
    print(a+b)

while True:
    a = int(input('请输入数字1'))
    b = int(input('请输入数字2'))
    addsum(a,b)
    


#addsum(1,2)
#addsum(a=1,b=2)
#addsum(b=2,a=1)
#addsum(2,1)#跟上面三句话的意思不一样

#addsum(1,b=2)这是错误的写法
#作业：  要求定义一个函数，能够输出自己的姓名和年龄，并且调用这个函数让他执行
#1、使用def定义函数
#2、编写完函数之后通过函数名（）调用
def printAge(name,age):
    print('姓名\n%s\t年龄\n%s\t'%(name,age))

printAge('李文浩',18)






