'''
志国买烟：一包烟10块钱，我让志国去买烟，结果什么？结果志国要12元 过去一趟一个棒棒糖  回来一趟一个棒棒糖  把烟带回来

'''
# 1.志国买烟
def buySmoke(money):
    if money >= 12:
        #买烟成功
        return '烟'
    else:
        # 跑回来了 老师  要12块钱才能买烟
        return money
        

# 给钱
money = int(input('给钱老师'))
maiyan  = buySmoke(money)
print(maiyan)
