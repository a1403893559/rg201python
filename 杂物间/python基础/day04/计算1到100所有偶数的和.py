# 需求是 求1到100之间所有的偶数和奇数

"""
1/先定两个变量，一个用来保存偶数和，一个用来保存奇数和
2、/定义一个初始值0
3、吧所有的偶数和奇数挑出来
4、sum_1   sum_2
求100以内所有能和4整除的数的和
"""
sum_1 = 0
sum_2 = 0
count = 0

while count<=100:
    #第一次进来 0
    if count%2 == 0:
        #求偶数
        sum_2 = sum_2 + count
    else:
        #求奇数
        sum_1 = sum_1 + count
    count = count + 1


