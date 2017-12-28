'''
王者荣耀正式版V1.0
1、功能提示，提示你这个系统有哪些功能
2、开始业务逻辑
3、退出
'''
wzry_gnts = '王者荣耀系统功能提示'
print(wzry_gnts.center(30))
print('*'*40)
print('功能1:%s\n功能2：%s\n'%('注册','登录'))
print('*'*40)

# 需要一个数组（列表）来存储用户输入的账号和密码
# account_list
account_list = [{'name':'libai','passwd':'123456'}]
# 要写两个按钮 这两个按钮就是两个函数
def login(account='libai',passwd='123456'):
    '''登录'''
    #print('登录')
    for dic in account_list:
        if account == dic['name']:
            # 进入这里 说明 账号已经正确，那么现在我们需要判断密码对不对
            if dic['passwd'] == passwd:
                print('登录成功')
            else:
                print('密码错误')
        else:
            print('账号输入错误')
    

def register(zhanghao='何志国',mima='123456'):
    '''注册'''
    #print('注册')
    for dic in account_list:
        if dic['name']==zhanghao:
            print('您的账号已经被注册')
        else:
            #创建一个临时字典
            tempDic = {}
            #把用户输入的账号存进字典
            tempDic['name']=zhanghao
            #吧用户输入的密码存进字典
            tempDic['passwd']=mima
            #吧字典存进列表里面
            account_list.append(tempDic)
            print('账号创建成功')
            break

    
print('-'*50)
account = input('请输入账号')
passwd = input('请输入密码')
#login(account,passwd)
#login()
print('-'*50)
register(account,passwd)
