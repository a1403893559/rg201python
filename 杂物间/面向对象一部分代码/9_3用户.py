class User(object):
    def __init__(self):
        self.first_name = '王'
        self.last_name = '宇飞'
        self.sex = '男'
        self.age = '17'
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)
        return self.login_attempts

    def rset_login_attempts(self):
        self.login_attempts = 0
    
    def describe_user(self):
        print(self.first_name,self.last_name,self.sex,self.age)

    def greet_user(self):
        print('你好，快餐300，过夜500要不要，留个微信呗，我叫%s'%self.last_name)    

class Admin(User):
    def print_show(self,p):
        print(p.show_privilegs())
class Privilegs(object):
    def __init__(self):
        self.privilegs = ['能发起POST请求','能发起GET请求']
    def show_privilegs(self):
        return self.privilegs

p = Privilegs()
ad = Admin()
ad.print_show(p)
# p = Privilegs()
# p.show_privilegs()

# u1 = User()
# u1.first_name = '李'
# u1.last_name = '文浩'
# u1.describe_user()
# u1.greet_user()

# u1.increment_login_attempts()
# u1.increment_login_attempts()
# u1.increment_login_attempts()
# u1.increment_login_attempts()
# u1.increment_login_attempts()
# u1.increment_login_attempts()
# print(u1.login_attempts)
# u1.rset_login_attempts()
# print(u1.login_attempts)


# ad = Admin()
# ad.show_privilegs()