# 需求是把九九乘法表敲出来

# 定义一个行号
row = 1
# 星星最大的打印行数
while row <= 9:
    # 定义一下起始列
    col = 1
    while col <= row:
        #end='',表示输出结束后布换行
        print('%d*%d=%d'%(row,col,row*col),end='')
        # 列数+1  决定我每一列放多少颗星星多少本书
        col += 1
    print('')
#决定我需要多少行，
    row += 1
