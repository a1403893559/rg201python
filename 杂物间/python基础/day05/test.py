# 娶老婆  丈母娘要求有80万的彩礼,还要一套别墅 才可以娶我女儿 你如果有80万 或者一套别墅   你可以先提亲

#money = int(input('你兜里有多少钱'))
#bie_shu = 1
while True:
    money = int(input('你兜里有多少钱'))
    bie_shu = int(input('你有别墅吗?要么输入0表示没有1表示有'))
    er_hun =int(input('你是否二婚,1表示二婚，0表示处男'))
    if money >= 80 and bie_shu == 1 :
        print('可以娶我女儿')
        break
    elif money >= 80 or bie_shu == 1:
        print('你可以提亲')
        continue
    elif money != 0 or bie_shu == 1:
        print('你可以娶我')
    elif not er_hun ==0:
        print('滚蛋')
    else:
        print('先上车后买票')
        break
