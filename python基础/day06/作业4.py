#创建一个列表 邀请3个人 
yaos = ['康俊','陈怀勇','翠花']
# 请他们来跟我共进晚餐
for name in yaos:
    print('你好,来我家吧%s,我家没人'%name)
print('%s因为来了...无法赴约'%yaos[2])
print('-------------------------------')

yaos[2] = input('请输入您想邀请的姐妹')

i = 0
while i < len(yaos):
    print('请来我家四人行吧%s'%yaos[i])
    i+=1


print('找到更大的餐桌')
print('---------------------------')

# 列表添加元素
yaos.insert(0,'王润泽')
# 定义一个变量 
center = int(len(yaos)/2)

# 待定
yaos.insert(center,'庞松源')

yaos.append('李文浩')

print(yaos)

# 吧列表转化成字符串
# 吧字符串进行增删改查的操作（根据某一个符号分隔进行提取'

#print('最终的名单:%s'%yaos)

# 只能邀请2位
print('对不起，现在只能邀请两位嘉宾')

print('到底现在是多少人%s'%yaos)

i = 1
count = len(yaos) - 1
print('长度%s'%count)
while i < count:
    print('很抱歉%s'%yaos[-1])
    yaos.pop()
    i+=1
    #print(yaos)

print(yaos)


c_h = len(yaos)

for i in range(0,c_h):
    del yaos[0]
    i+=1
print(yaos)
    



# 以下代码，逻辑是正确的，但是，输出是错误的，python官方建议，不要在for循环遍历的时候 对列表进行修改
## pop()  不断的删除  
#for name in yaos:
##    if int(len(yaos)) == 1:
##        print('只剩两位嘉宾')
##        break
#    #print('走了几次%d'%(len(yaos)))    
#    yaos.remove(name)
#    print(yaos)
#






