a = [x for x in range(4)]
print('列表a内容为:',a)
b = [x for x in range(3,4)]
print('列表b的内容为：',b)
c = [x for x in range(3,19)]
print('列表c的内容为:',c)
d = [x for x in range(3,19,2)]
print('列表d内容是:',d)
# for循环
e = [x for x in range(3,10) if x%2==0]
print('列表e:',e)
f = [x for x in range(3,10) if x%2!=0]
print('列表f：',f)
g = [x for x in range(3,10)]
print('g:',g)
print('----------------华丽分割线----------------')
# 2个for循环
h = [(x,y) for x in range(1,3) for y in range(3)]
print(h)
# 4个for循环
j = [(x,y,z) for x in range(1,3) for y in range(3) for z in range(4,6)]
print(j)