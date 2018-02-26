def listDemo(alist):#修改列表的元素值
    #取出索引为0的元素的值 传进来的值是一个数字
    alist[0] = alist[0]+1
    return alist


a = [2]
print('外界的原来的未传进去的列表a的值为:',a)

print('函数里面的列表:',listDemo(a))
print('-'*20)
print('函数外的a:',a)
print('-'*20)
print('第二次调用函数',listDemo(a))
print('-'*20)
print('外界的a=',a)
