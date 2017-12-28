'''
学员管理系统V1.0
1 必须使用函数 完成对程序的模块化
学员信息至少包含：姓名 年龄 学号 
功能必须有 添加  删除  修改  查询 退出
分析：
1、姓名：张兆恒  年龄：6  学号：01
         李文浩        1        02
         翠花          3        03
2、我们的这些信息 需要有一个地方来存储，那么这个我们就使用列表  
3、添加 
4、删除
5、修改
6、查询
7、退出（每一个功能我们都可以写成一个函数)
'''
# 我们将来的操作 ，都是在操作这个容器，这个容器里面，装了我们所有的 学员信息，每一个学员信息 装到一个小袋子里然后放到容器里
# 盒子 盒子里面装了一张张名片
he_Zi = []
# 定义一个函数 这个函数 什么都不做 就输出横线
def printLine():
    # 输出一条横线
    print('*'*50)

# 1、添加
# addStudent
def tian_jia():
    # 用户的信息 姓名  年龄   学号
    name = input('请输入姓名')
    age = input('请输入年龄')
    num = input('学号')
    # 需要吧用户的信息 包装起来 然后存到列表里面    包装 就是用字典来包装
    # 创建字典 我得到了一个人的数据了
    xin_xi = {'姓名':name,'年龄':age,'学号':num}
    # 需要吧这一行信息  插入到我们名单里面 或者说也可以理解为 吧这一张名片 放到名片盒子里面 名片盒子是一个列表（数组）这里面就涉及一个知识 列表怎么添加数据：列表添加数据的语法格式写一下 列表.append(你要添加的内容)
    he_Zi.append(xin_xi)
    #函数的调用 当我调用了这个函数 什么都没做  就是输出一条横线而已
    printLine()
    print('现在有的学生是%s'%he_Zi)
    printLine()


    # 吧一个人的数据 添加到我们总的名单里面 前面我们定义的名单是 he_ze
#    pass #pass就是什么都不做 如果你不写语法就错误了，因为你不写这就不是一个完整的函数了


#2、删除
# delete 
def shan_chu():
    # 我要删除 学生  要求你至少要告诉我你要删除的学生的名字
    name = input('请输入要删除的名字')
    # 要从盒子里面去找名片 或者说要从名单里面去找到在哪一行 
    # 需要遍历
    # 需要有一个计数器 来记录我到了第几行
    count = 0
    for dic in he_Zi:
        if dic['姓名'] == name:
            del he_Zi[count] 
        else:
            #print('查无此人')
            count+=1
    print('此时还有%s'%he_Zi)
    printLine()

#3、修改
# change
def xiu_gai():
    # 要修改什么  就先吧你要修改的内容输入
    name = input('请输入要修改的学员名字')
    count = 0
    for dic in he_Zi:
        if dic['姓名']==name:
            he_Zi[count]['姓名']=input('请输入姓名')
            he_Zi[count]['年龄']=input('请输入年龄')
            he_Zi[count]['学号']=input('请输入学号')
        else:
            count+=1
    printLine()
    print('现在有哪些%s'%he_Zi)
    printLine()

#4、查询
def cha_xun():
    for dic in he_Zi:
        print('姓名%s\t年龄%s\t学号%s\t'%(
        dic['姓名'],dic['年龄'],dic['学号']))
#5、退出
# exit
def tui_chu():
    pass


# 调用函数
tian_jia()
tian_jia()
tian_jia()
shan_chu()
xiu_gai()
cha_xun()
