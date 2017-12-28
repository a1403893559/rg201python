def sum2(a,b,c=7):
    print(a)
    print(b)
    print(c)

sum2.__default__ # 会调用参数的默认值

sum2(3,4,5)

