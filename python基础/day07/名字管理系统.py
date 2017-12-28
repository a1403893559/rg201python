'''
名字管理系统 
1、添加一个新的名字
2、删除名字
3、修改名字
4、查询名字
'''
# 1、打印分割线
print('*'*50)
# 系统功能提示(通过打印)
print('名字关系管理系统V1.0')
print('1、添加一个新的名字')
print('2、删除一个名字')
print('3、修改一个名字')
print('4、查询一个名字')
print('5、退出系统')
print('*'*50)

# 2、需要有一个值来记录 记录用户输入了什么 1   2    3   4  来决定我们后面的代码
#num = int(input('请输入功能序号'))
names = []
while True:
    num = int(input('请在此输入你需要的功能'))
    print('num=%d'%num)
    if num==1:
        name = input('请输入要添加的用户名')
        names.append(name)
        print('添加成功,当前的名字一共有%s'%names)
    elif num==2:
        name = input('请输入要删除的用户')
        names.remove(name)
        print('删除成功，删除以后还有%s'%names)
    elif num==3:
        name = input('请输入要修改的用户')
        print('name_user=%s'%name)
        # 修改用列表不好修改
        if name in names:
            print('name_user=%s'%name)
        # 修改用列表不好修改
            nameIndex = names.index(name)
            #print('============%nameIndex=%d'%nameIndex)
            names[nameIndex] = input('请输入要修改的内容')
            print('修改以后的列表内容%s'%names)
        else:
            print('对不起，您所输入的用户不存在')
    elif num==4:
        find_name = input('请输入查询名字')
        if find_name in names:
            print('查到你要的人')
        else:
            print('查无此人')
    elif num==5:
        break
    else:
        print('输入错误请重新输入')
    


