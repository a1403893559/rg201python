
import os
def linear(a,b):
    def result(x):     #在python中,函数是可以嵌套定义的
        return a * x+b
    return result

taxes = linear(0.3,2)
test = taxes(5)
print(test)


