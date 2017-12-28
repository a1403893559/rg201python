# 学员信息
def studentInfo(name,profession,account,passwd):
    f = open('123.txt','w')
    # 一条学员的信息 就是一个字典
    infoDict = {'n':name,'p':profession,'a':account,'pwd':passwd}
    names = [infoDict]
    f.write(names)
    f.close()
studentInfo('张嘉译','人工只能','账号','密码')

