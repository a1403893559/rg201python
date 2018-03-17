def print_passwd():
    # 1 用户输入密码
    pwd = input("请输入密码")

    # 2 对输入的密码进行判断
    if len(pwd) > 8:
        print("密码正确")
    else:
        print("密码错误")
        ex = Exception("密码少于8位")
        raise ex


print_passwd()
