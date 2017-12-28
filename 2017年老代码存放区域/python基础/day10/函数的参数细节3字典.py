def hongKong(nameDic):
    nameDic['香港']='中国'
    print('函数里面的操作结果:',nameDic)

a = {'香港':'英国'}
print('调用函数之前的a=',a)
hongKong(a)
print('外界的a：',a)

