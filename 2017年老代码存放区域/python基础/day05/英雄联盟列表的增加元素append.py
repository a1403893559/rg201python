# 寒冰射手   德玛西亚  猪妹  德玛西亚皇子 盲僧   康俊 原建波   白浩

# 命名一个变量，变量的名字 lol 
lol = ['寒冰射手','德玛西亚','康俊']

# 在新英雄出现之前有那些英雄:
for i in lol:
    print('英雄登场啦%s'%i)
    print('-------------------')

# 增加元素 append extend insert
#lol.append('盲僧')


# 需求是：在命令行输入一个字符串（命令行输入一个英雄），添加到我们列表的末尾

# 1、第一步我们需要 在命令行输入
test = input('请输入你要加入的英雄')
# 2、把输入的的值加入到列表末尾
lol.append(test)


for i in lol:
    print('最新的战队有哪些英雄:%s'%i)

#print(lol)
