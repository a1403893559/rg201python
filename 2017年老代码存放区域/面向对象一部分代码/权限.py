class 用户(object):
    def __init__(self):
        self.姓 = '张'
        self.名字 = '三'
        self.年龄 = 28
        self.家庭住址 = '山西太原'
    
    def 用户详情(self):
        print(self.姓,self.名字,self.年龄,self.家庭住址)

    def 问候(self):
        print('快餐300，包夜50')

class 管理员类(用户):
    def __init__(self,shang):
        shang.秀一下管理员的权限
class 展示权限类(object):
    def __init__(self):
        self.权限 = ['可以上网','可以看片']
    def 秀一下管理员的权限(self):
        print(self.权限)
        return self.权限

上方宝剑 = 展示权限类()
张佳毅 = 管理员类(上方宝剑)


# 张佳毅 = 管理员类()
# 张佳毅.秀一下管理员的权限()
# 张佳毅.问候()


# 李文浩 = 用户()
# 李文浩.姓 = '李'
# 李文浩.名字 = '文浩'
# 李文浩.用户详情()
# 李文浩.问候()

# 老九 = 用户()
# 老九.姓 = '张'
# 老九.名字 = '妹妹'
# 老九.用户详情()
# 老九.问候()