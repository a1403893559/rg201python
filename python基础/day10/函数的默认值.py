def sum1(a,b=1):
    pass

sum1(5,4)
print('-'*30)

def sum2(name1,names=[]):
    '''如果默认值参数，外界没有传任何值的时候，python会吧上次保存的值进行叠加'''
    if names is None:
        names = []
    names.append(name1)
    print(names)
sum2('后羿',['射手'])
print('-'*20)
sum2('李白')
print('-'*20)
sum2('韩信')
sum2('猪妹')
sum2('哈哈')
