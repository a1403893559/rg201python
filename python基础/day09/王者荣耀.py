'''
1、腾讯的一款游戏：王者荣耀
2、网易：吃鸡（荒野求生）
王者荣耀： 法师 战士  射手 刺客  辅助 坦克
网易：男人  女人
> 需求一，创建一个5V5游戏战场，选择英雄类型,在此之前我们需要干嘛，匹配，在匹配我们需要打开这个游戏，在打开游戏之前下载APP
'''
# 注册王者荣耀
def wzry_register():
    pass
# 登录王者荣耀
def wzry_login():
    pass
# 登录/注册是否成功
def wzry_isregister_or_islogin():
    pass
# 王者荣耀APP
def wzry_app(start):#这句话的意思是，让用户告诉我，要不要开始游戏1，表示开始游戏，2表示结束游戏，其他表示卸载游戏
    #当前接收参数是
    print('start=%d'%start)
    if start == 1:#开始游戏
        print('开始游戏')
        # 当你点开APP哪一刻 是不是要先注册
        wzry_register()         
    elif start == 2:#游戏结束
        print('结束游戏')
    else:
        print('卸载游戏')

#调用这个APP（前提是什么，你下载过这个游戏）调用这个app的时候 需要输入一个值来告诉手机或者程序  我要干什么
# 1 开始   2结束  3卸载
user_id = int(input('请输入序号'))
# 我把用户输入的序号 传递进参数里面
wzry_app(user_id)




