# 将一些朋友的姓名 存储在一个列表里面 并且将其命名为 names 依次访问 该列表的每一个元素 从而将每一个朋友的名字都打印出来

# 1/存储 朋友的姓名  题目告诉我们必须用列表 并且变量名为names
# 列表是python里面的基本数据类型之一 是我们用来存储 元素的容器 在其他语言 也叫数组  格式是以中括号括起来 以逗号分割的
names = ['陈怀勇','康俊','翠花']
# 依次访问 列表（数组） 是有序的  比如陈怀勇是0 康俊是1 翠花是2...
#name=names[0]
#name=names[1]
#name=names[2]
# 这个时候  我使用for 或者 while循环来访问和输出数据
# 这是用for循环的方法来做
for name in names:
    print('hello:%s'%name)


print('--------以下是使用while------')
# 使用while循环来写这题 重复做事 需要一个计数器  来确定  来告诉  程序 需要重复执行多少次   如果你没有计数器或者计数器不增加会怎么样？  会死循环 
#创建一个计数器  可以理解为创建一个变量存储int型数据 用于记录 while循环的次数
i = 0

# while循环  后面跟的是循环条件和循环体 循环条件就是满足什么条件的情况下循环 循环体就是要重复的内容
while i < len(names):
    #print('列表长度%d'%len(names))
    #print('第%d次重复'%i)
    print('hello%s'%names[i])
    i+=1















