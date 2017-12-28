# 偷王者荣耀 升级版   1、老师来了 就藏手机   老师走了  继续玩


# 首先我要先确定我是目前  在第几杀
count = 0
# 还要一个耳报神 告诉我 老师班主任   来没有来
bang_zhu = 0#0表示没有来   1表示来了

# 要先判断 我的游戏有没有正在进行（你如果没有输了 或者没有赢 就正在进行）
while count<=5 and bang_zhu !=1:
    print('目前在第%d杀'%count)
    # 判断班主任来了没有
    bang_zhu = int(input('班主任来了没?'))
    if bang_zhu == 1:
        print('当在第%d杀的时候，班主任来了'%count)
        bang_zhu = 0
        continue#中断一次循环
    
 #   bang_zhu = 0
    #每一次循环我都要增加一杀
    count += 1

if count>=5:
    print('游戏胜利')
else:
    print('游戏结束')


